import subprocess
import json
import os
import logging
from typing import List, Dict, Optional
from abc import ABC, abstractmethod

from .adb_utils import (
    ADBCommandError,
    ADBNotFoundError,
    DEFAULT_TCPIP_PORT,
    DeviceSelectionError,
    DeviceState,
    connect_wifi_device,
    list_devices,
    pair_device,
    resolve_adb_path,
    run_command,
    is_wifi_serial,
)

try:
    from .package_registry import PackageRegistry
    REGISTRY_AVAILABLE = True
except ImportError:
    REGISTRY_AVAILABLE = False

class BloatwareRemover(ABC):
    """Base class for brand-specific bloatware removal"""
    
    def __init__(self, brand: str, config_file: str = None, test_mode: bool = False, use_registry: bool = True):
        self.brand = brand
        self.config_file = config_file or f"{brand.lower()}_config.json"
        self.test_mode = test_mode
        self.use_registry = use_registry and REGISTRY_AVAILABLE
        self.logger = self._setup_logging()
        self.packages = self._load_packages()
        self._app_name_cache = {}
        self.adb_path = None
        self.device_serial = None
        self._last_wifi_endpoint = None
        
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'{self.brand.lower()}_removal.log'),
                logging.StreamHandler()
            ]
        )
        return logging.getLogger(f'{self.brand}Remover')
    
    def _load_packages(self) -> Dict:
        """Load package configuration from JSON file or centralized registry"""
        # Try loading from centralized registry first
        if self.use_registry and REGISTRY_AVAILABLE:
            try:
                registry = PackageRegistry()
                brand_data = registry.get_brand_packages(self.brand.lower())
                if brand_data:
                    self.logger.info(f"Loaded packages from centralized registry for {self.brand}")
                    return self._convert_registry_format(brand_data)
            except Exception as e:
                self.logger.warning(f"Failed to load from registry: {e}, falling back to legacy config")
        
        # Fall back to legacy config file
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            else:
                return self._get_default_packages()
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
            return self._get_default_packages()
    
    def _convert_registry_format(self, brand_data: Dict) -> Dict:
        """Convert centralized registry format to the format expected by the remover"""
        categories = {}
        for category_id, category_data in brand_data.get('categories', {}).items():
            package_list = []
            for package in category_data.get('packages', []):
                package_list.append({
                    'name': package['name'],
                    'description': package['description'],
                    'risk': package['risk']
                })
            categories[category_id] = package_list
        return {'categories': categories}
    
    @abstractmethod
    def _get_default_packages(self) -> Dict:
        """Return default package configuration for the brand"""
        pass
    
    def check_device_connection(self) -> bool:
        """Check if a device is connected via ADB, retrying as needed."""

        while True:
            if self.test_mode:
                print("Running in test mode - skipping device connection check")
                return True

            try:
                adb_path = self._ensure_adb_path()
            except ADBNotFoundError as exc:
                print(str(exc))
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    return True
                if decision == 'quit':
                    return False
                continue

            try:
                devices = list_devices(adb_path)
            except ADBCommandError as exc:
                self.logger.error("Failed to query devices: %s", exc)
                print("\nADB could not communicate with the device.")
                print("Please make sure Developer options and USB debugging are enabled, then reconnect the cable.")
                print("   Enable Developer options: Settings  About phone  tap 'Build number' seven times.")
                print("   Enable USB debugging: Settings  System  Developer options  toggle USB debugging on.")
                print("   Reconnect the device and accept the USB debugging prompt if shown.")
                if self._prompt_wifi_connection("Attempt to connect over Wi-Fi ADB instead?"):
                    continue
                action = self._prompt_connection_retry()
                if action == "retry":
                    continue
                if action == "test":
                    decision = self._prompt_enable_test_mode()
                    if decision == 'test':
                        return True
                    if decision == 'quit':
                        return False
                    continue
                return False

            if not devices:
                print("\nNo devices detected.")
                print("Connect your phone and enable USB debugging:")
                print("  1. Unlock the device and connect it via USB.")
                print("  2. If Developer options aren't visible, enable them by tapping 'Build number' seven times.")
                print("  3. Open Developer options and enable USB debugging.")
                print("  4. Confirm the 'Allow USB debugging' prompt on the device.")
                if self._prompt_wifi_connection("Would you like to try Wi-Fi debugging instead?"):
                    continue
                action = self._prompt_connection_retry()
                if action == "retry":
                    continue
                if action == "test":
                    decision = self._prompt_enable_test_mode()
                    if decision == 'test':
                        return True
                    if decision == 'quit':
                        return False
                    continue
                return False

            authorized = [device for device in devices if device.state == 'device']
            pending = [device for device in devices if device.state != 'device']

            if pending:
                print("\nDetected devices that still need attention:")
                for device in pending:
                    self._show_device_state_instructions(device)
                if self._prompt_wifi_connection("Switch to Wi-Fi debugging?"):
                    continue
                action = self._prompt_connection_retry()
                if action == "retry":
                    continue
                if action == "test":
                    decision = self._prompt_enable_test_mode()
                    if decision == 'test':
                        return True
                    if decision == 'quit':
                        return False
                    continue
                return False

            if self.device_serial:
                for device in authorized:
                    if device.serial == self.device_serial:
                        return True
                print("Previously selected device is no longer connected. Please select a device again.")
                self.device_serial = None

            if not authorized:
                print("No authorised devices were detected after reconnection attempts.")
                if self._prompt_wifi_connection("Try connecting via Wi-Fi ADB?"):
                    continue
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    return True
                if decision == 'quit':
                    return False
                continue

            selected_device = self._select_device(authorized)
            if selected_device:
                self.device_serial = selected_device.serial
                return True

            print("Device selection cancelled. You can resolve the issue and try again.")
            action = self._prompt_connection_retry()
            if action == "retry":
                continue
            if action == "test":
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    return True
                if decision == 'quit':
                    return False
                continue
            return False
    
    def get_installed_packages(self) -> List[str]:
        """Get list of installed packages on device"""
        if self.test_mode:
            return self._get_all_packages()

        if not self.device_serial and not self.check_device_connection():
            return []

        try:
            result = self._run_adb(['shell', 'pm', 'list', 'packages'], timeout=60)
        except (ADBCommandError, DeviceSelectionError) as exc:
            self.logger.error("Failed to get installed packages: %s", exc)
            print("Unable to retrieve the package list. Ensure the device stays unlocked and USB debugging remains enabled.")
            return []

        packages = [
            line.replace('package:', '').strip()
            for line in result.stdout.split('\n')
            if line.startswith('package:')
        ]
        return packages
    
    def uninstall_package(self, package: str) -> bool:
        """Uninstall a single package"""
        if self.test_mode:
            print(f"TEST MODE: Would remove package: {package}")
            self.logger.info(f"TEST MODE: Would remove package: {package}")
            return True

        if not self.device_serial and not self.check_device_connection():
            return False

        try:
            result = self._run_adb(
                ['shell', 'pm', 'uninstall', '--user', '0', package],
                check=False,
                timeout=60,
            )
        except (ADBCommandError, DeviceSelectionError) as exc:
            self.logger.error("Error removing %s: %s", package, exc)
            return False

        stdout = (result.stdout or "").strip().lower()
        stderr = (result.stderr or "").strip()

        if result.returncode == 0 and ('success' in stdout or not stdout):
            self.logger.info("Successfully removed: %s", package)
            return True

        self.logger.warning("Failed to remove %s - %s", package, stderr or stdout or "Unknown error")
        return False
    
    def backup_packages(self, packages: List[str]) -> bool:
        """Create backup of packages before removal"""
        backup_file = f"{self.brand.lower()}_backup.json"
        try:
            import datetime
            backup_data = {
                'brand': self.brand,
                'packages': packages,
                'timestamp': datetime.datetime.now().isoformat(),
                'test_mode': self.test_mode
            }
            
            with open(backup_file, 'w') as f:
                json.dump(backup_data, f, indent=2)
            
            mode_text = "TEST MODE: " if self.test_mode else ""
            print(f"{mode_text}Backup created: {backup_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create backup: {e}")
            return False
    
    def get_app_name(self, package_name: str) -> str:
        """Get human-readable app name from package name"""
        if package_name in self._app_name_cache:
            return self._app_name_cache[package_name]

        if self.test_mode:
            app_names = {
                'com.android.chrome': 'Chrome',
                'com.google.android.gm': 'Gmail',
                'com.facebook.katana': 'Facebook',
                'com.instagram.android': 'Instagram'
            }
            app_label = app_names.get(package_name, f"Test App ({package_name.split('.')[-1]})")
            self._app_name_cache[package_name] = app_label
            return app_label
        
        try:
            result = self._run_adb(['shell', 'pm', 'dump', package_name], timeout=10, check=False)

            for line in result.stdout.split('\n'):
                if 'applicationLabel=' in line:
                    label = line.split('applicationLabel=')[1].strip()
                    if label:
                        self._app_name_cache[package_name] = label
                        return label

            if 'labelRes=' in result.stdout and 'labelRes=0x0' not in result.stdout:
                alt = self._run_adb(['shell', 'dumpsys', 'package', package_name], timeout=10, check=False)
                for line in alt.stdout.split('\n'):
                    if 'applicationLabel=' in line:
                        label = line.split('applicationLabel=')[1].strip()
                        if label:
                            self._app_name_cache[package_name] = label
                            return label

            lookup = self._run_adb(['shell', 'pm', 'list', 'packages', '-f', package_name], timeout=10, check=False)
            if lookup.stdout.strip():
                fallback = package_name.split('.')[-1].title()
                self._app_name_cache[package_name] = fallback
                return fallback

        except (ADBCommandError, DeviceSelectionError):
            pass

        fallback = package_name.split('.')[-1].title()
        self._app_name_cache[package_name] = fallback
        return fallback

    def get_package_metadata(self, package_name: str) -> Dict[str, str]:
        """Retrieve risk and description metadata for a package"""
        categories = self.packages.get('categories', {})
        for category, package_list in categories.items():
            for package_info in package_list:
                if package_info['name'] == package_name:
                    return {
                        'risk': package_info.get('risk', 'safe'),
                        'description': package_info.get('description', 'No description'),
                        'category': category
                    }
        return {
            'risk': 'unknown',
            'description': 'Not listed in curated bloatware configuration',
            'category': 'unknown'
        }

    def list_all_apps_removal(self) -> None:
        if not self.check_device_connection():
            return

        print("Fetching all installed applications...")
        installed_packages = self.get_installed_packages()

        if not installed_packages:
            print("No packages found or failed to retrieve package list")
            return

        mode_text = " (TEST MODE)" if self.test_mode else ""
        print(f"\n{self.brand} - All Apps Removal Tool{mode_text}")
        print("=" * 50)

        if self.test_mode:
            print("Running in test mode - no actual changes will be made")
            print("=" * 50)

        system_packages = {
            'android',
            'com.android.systemui',
            'com.android.settings',
            'com.android.launcher',
            'com.android.phone',
            'com.android.contacts',
        }

        print("Loading app information...")
        app_info: List[Dict[str, str]] = []

        for index, package in enumerate(installed_packages):
            if any(token in package for token in system_packages):
                continue

            if index % 50 == 0:
                print(f"Processed {index}/{len(installed_packages)} packages...")

            app_name = self.get_app_name(package)
            metadata = self.get_package_metadata(package)

            app_info.append(
                {
                    'package': package,
                    'name': app_name,
                    'risk': metadata['risk'],
                    'description': metadata['description'],
                }
            )

        app_info.sort(key=lambda entry: entry['name'].lower())

        print(f"\nFound {len(app_info)} applications")
        print("=" * 50)

        risk_labels = {
            'safe': '[SAFE]',
            'caution': '[CAUTION]',
            'dangerous': '[DANGER]',
            'unknown': '[UNKNOWN]',
        }

        print("All installed applications:")
        print("-" * 50)

        for position, app in enumerate(app_info, 1):
            risk_indicator = risk_labels.get(app['risk'], '[UNKNOWN]')
            print(f"{position:3d}. {risk_indicator} {app['name']}")
            print(f"     Package: {app['package']}")
            print(f"     Description: {app['description']}")
            print()

        print("=" * 50)
        print("Now select which apps to remove:")
        print("Enter app numbers separated by commas (e.g., 1,3,5-8,12)")
        print("Or enter 'all' to select all apps")
        print("Or enter 'none' to cancel")
        print("-" * 50)

        while True:
            selection = input("Enter your selection: ").strip().lower()

            if selection == 'none':
                print("No apps selected for removal")
                return

            if selection == 'all':
                indices = list(range(1, len(app_info) + 1))
            else:
                try:
                    indices = []
                    for chunk in selection.split(','):
                        chunk = chunk.strip()
                        if '-' in chunk:
                            start, end = map(int, chunk.split('-'))
                            indices.extend(range(start, end + 1))
                        else:
                            indices.append(int(chunk))
                except ValueError:
                    print("Invalid format. Please use numbers, ranges (1-5), or commas (1,3,5)")
                    print("Example: 1,3,5-8,12")
                    continue

            valid = []
            for index in indices:
                if 1 <= index <= len(app_info):
                    valid.append(index)
                else:
                    print(f"Warning: Index {index} is out of range (1-{len(app_info)})")

            if not valid:
                print("No valid indices provided. Please try again.")
                continue

            indices = sorted(set(valid))
            break

        selected_packages = []
        selected_apps = []

        for index in indices:
            app = app_info[index - 1]
            selected_packages.append(app['package'])
            selected_apps.append(app)

        print(f"\nSelected {len(selected_packages)} apps for removal:")
        print("-" * 50)

        for position, app in enumerate(selected_apps, 1):
            risk_indicator = risk_labels.get(app['risk'], '[UNKNOWN]')
            print(f"{position:3d}. {risk_indicator} {app['name']}")
            print(f"     Package: {app['package']}")
            print(f"     Description: {app['description']}")
            print()

        print("=" * 50)
        if input("Create backup before removal? (y/n): ").lower().strip() == 'y':
            self.backup_packages(selected_packages)

        confirm_text = "yes" if not self.test_mode else "y"
        message = (
            "TEST MODE: This will simulate removing the selected apps"
            if self.test_mode
            else "This will remove the selected apps from the current user"
        )
        print(f"\n{message}")

        if input(f"Proceed with removal? (type '{confirm_text}' to confirm): ").lower().strip() == confirm_text:
            self.remove_packages(selected_packages)
        else:
            print("Removal cancelled")

    def interactive_removal(self) -> None:
        """Interactive package removal with user selection"""
        if not self.check_device_connection():
            return
        
        installed_packages = self.get_installed_packages()
        
        mode_text = " (TEST MODE)" if self.test_mode else ""
        print(f"\n{self.brand} Bloatware Removal Tool{mode_text}")
        print("-" * 40)
        
        if self.test_mode:
            print("Running in test mode - no actual changes will be made")
            print("-" * 40)
        
        categories = self.packages.get('categories', {})
        selected_packages = []
        
        for category, package_list in categories.items():
            print(f"\n{category.upper()} PACKAGES:")
            
            for package_info in package_list:
                package_name = package_info['name']
                description = package_info.get('description', 'No description')
                risk_level = package_info.get('risk', 'safe')
                
                if package_name in installed_packages:
                    risk_indicator = {'safe': '[SAFE]', 'caution': '[CAUTION]', 'dangerous': '[DANGER]'}
                    print(f"  {risk_indicator.get(risk_level, '[UNKNOWN]')} {package_name}")
                    print(f"    {description}")
                    
                    choice = input(f"    Remove this package? (y/n): ").lower().strip()
                    if choice == 'y':
                        selected_packages.append(package_name)
        
        if selected_packages:
            print(f"\nSelected {len(selected_packages)} packages for removal")
            
            if input("Create backup before removal? (y/n): ").lower().strip() == 'y':
                self.backup_packages(selected_packages)
            
            if input("Proceed with removal? (y/n): ").lower().strip() == 'y':
                self.remove_packages(selected_packages)
        else:
            print("No packages selected for removal")
    
    def remove_packages(self, packages: List[str] = None, skip_connection_check: bool = False) -> None:
        """Remove specified packages or all configured packages"""
        if not skip_connection_check and not self.check_device_connection():
            return
        
        if packages is None:
            packages = self._get_all_packages()
        
        mode_text = "TEST MODE: " if self.test_mode else ""
        print(f"{mode_text}Starting removal of {len(packages)} packages...")
        
        success_count = 0
        failed_count = 0
        
        for package in packages:
            if self.uninstall_package(package):
                success_count += 1
            else:
                failed_count += 1
        
        print(f"\n{mode_text}Removal complete:")
        print(f"  Successfully removed: {success_count}")
        print(f"  Failed to remove: {failed_count}")
        
        if failed_count > 0 and not self.test_mode:
            print("Check the log file for details on failed removals")
        elif self.test_mode:
            print("No actual changes were made - this was a test run")
    
    def _get_all_packages(self) -> List[str]:
        """Get all package names from configuration"""
        all_packages = []
        categories = self.packages.get('categories', {})
        
        for package_list in categories.values():
            for package_info in package_list:
                all_packages.append(package_info['name'])
        
        return all_packages

    def configure_adb(self, adb_path: Optional[str], device_serial: Optional[str]) -> None:
        """Persist adb context provided by the device detector."""

        if adb_path:
            self.adb_path = adb_path
        if device_serial:
            self.device_serial = device_serial
            if is_wifi_serial(device_serial):
                self._last_wifi_endpoint = device_serial

    def _ensure_adb_path(self) -> str:
        """Resolve and cache the adb executable path."""

        if self.adb_path:
            return self.adb_path

        self.adb_path = resolve_adb_path()
        return self.adb_path

    def _prompt_enable_test_mode(self) -> str:
        """Ask the user for the next step after a connection failure.

        Returns one of 'test', 'retry', or 'quit'."""

        while True:
            choice = input(
                "Do you want to run in test mode anyway? (y/n or 'quit' to cancel): "
            ).lower().strip()

            if choice in {'y', 'yes'}:
                print("Continuing in test mode - no actual changes will be made")
                self.test_mode = True
                return 'test'

            if choice in {'n', 'no'}:
                print("Okay, we'll keep trying with the connected device.")
                return 'retry'

            if choice in {'quit', 'q', 'exit', 'cancel'}:
                print("Cancelling device operations.")
                return 'quit'

            print("Please respond with 'y', 'n', or type 'quit' to cancel.")

    def _prompt_connection_retry(self) -> str:
        """Prompt the user to retry, switch to test mode, or cancel connection attempts."""

        while True:
            response = (
                input("Type 'retry' once the issue is fixed, 'test' to continue in test mode, or 'quit' to cancel: ")
                .strip()
                .lower()
            )
            if response in {'retry', 'r', 'yes', 'y'}:
                return 'retry'
            if response in {'test', 't'}:
                return 'test'
            if response in {'quit', 'q', 'exit', 'cancel'}:
                return 'quit'
            print("Invalid option. Please type 'retry', 'test', or 'quit'.")

    def _prompt_wifi_connection(self, message: str) -> bool:
        while True:
            reply = input(f"{message} (y/n): ").strip().lower()
            if reply in {'y', 'yes'}:
                return self._connect_via_wifi()
            if reply in {'n', 'no', 'skip', 's'}:
                return False
            print("Please answer with 'y' or 'n'.")

    def _connect_via_wifi(self) -> bool:
        try:
            adb_path = self._ensure_adb_path()
        except ADBNotFoundError as exc:
            print(str(exc))
            return False

        default_host = self._last_wifi_endpoint or ""
        prompt = "Enter the device IP address (append :port if not using 5555): "
        if default_host:
            prompt = f"Enter the device IP address (press Enter for {default_host}): "

        endpoint = input(prompt).strip()
        if not endpoint and default_host:
            endpoint = default_host

        if not endpoint:
            print("No address provided. Skipping Wi-Fi connection.")
            return False

        if ':' not in endpoint:
            endpoint = f"{endpoint}:{DEFAULT_TCPIP_PORT}"

        needs_pairing = None
        while needs_pairing is None:
            decision = input("Does the device display a pairing code? (y/n): ").strip().lower()
            if decision in {'y', 'yes'}:
                needs_pairing = True
            elif decision in {'n', 'no'}:
                needs_pairing = False
            else:
                print("Please answer with 'y' or 'n'.")

        if needs_pairing:
            pair_host = input(
                "Enter the pairing IP:port shown on the device (leave blank to reuse the same host): "
            ).strip()
            if not pair_host:
                pair_host = endpoint

            pairing_code = input("Enter the six-digit pairing code: ").strip()
            if not pairing_code:
                print("Pairing code missing. Cannot continue with Wi-Fi pairing.")
                return False

            try:
                pair_device(adb_path, pair_host, pairing_code)
                print(f"Paired with {pair_host}.")
            except ADBCommandError as exc:
                print("Failed to pair with the device.")
                if exc.stderr:
                    print(exc.stderr.strip())
                return False

        try:
            device = connect_wifi_device(adb_path, endpoint)
        except ADBCommandError as exc:
            print("Failed to connect over Wi-Fi.")
            if exc.stderr:
                print(exc.stderr.strip())
            return False
        except DeviceSelectionError as exc:
            print("Connected but the device did not appear in the adb list.")
            if exc.devices:
                print("Currently visible devices:")
                for device_state in exc.devices:
                    print(f"  - {device_state.summary()}")
            return False

        self.adb_path = adb_path
        self.device_serial = device.serial
        self._last_wifi_endpoint = endpoint
        print(f"Connected to {device.summary()} over Wi-Fi.")
        return True

    def _show_device_state_instructions(self, device: DeviceState) -> None:
        """Display guidance for resolving common device connection states."""

        print(f"  - {device.summary()}")
        state = device.state.lower().strip()

        if state == 'unauthorized':
            print("     Unlock the device and ensure USB debugging is enabled in Developer options.")
            print("     When prompted, tap 'Allow' to trust this computer for USB debugging.")
        elif state == 'offline':
            print("     Reconnect the USB cable and toggle USB debugging off and on again.")
            print("     Ensure the device screen stays awake and unlocked.")
        elif state == 'recovery':
            print("     The device is in recovery mode. Boot into Android before running the remover.")
        else:
            print("     Check the USB connection and confirm the device is unlocked with USB debugging enabled.")

    def _select_device(self, authorized_devices: List[DeviceState]) -> Optional[DeviceState]:
        """Select a device from the authorised list, prompting when needed."""

        if not authorized_devices:
            return None

        if len(authorized_devices) == 1:
            device = authorized_devices[0]
            print(f"Using device: {device.summary()}")
            return device

        print("Multiple authorised devices detected:")
        for idx, device in enumerate(authorized_devices, start=1):
            print(f"  {idx}. {device.summary()}")

        while True:
            selection = input(f"Select device (1-{len(authorized_devices)}) or 'c' to cancel: ").strip().lower()
            if selection in {'c', 'cancel', 'q', 'quit'}:
                print("Device selection cancelled")
                return None

            try:
                index = int(selection)
            except ValueError:
                print("Invalid selection. Please try again.")
                continue

            if 1 <= index <= len(authorized_devices):
                device = authorized_devices[index - 1]
                print(f"Using device: {device.summary()}")
                return device

            print("Selection out of range. Please try again.")

    def _run_adb(self, args: List[str], *, timeout: int = 15, check: bool = True) -> subprocess.CompletedProcess:
        """Run an adb command for the selected device."""

        if self.test_mode:
            raise ADBCommandError("Attempted to execute adb command while in test mode")

        adb_path = self._ensure_adb_path()

        if not self.device_serial:
            raise DeviceSelectionError(
                "No authorised device selected for adb operations", devices=[]
            )

        return run_command(
            adb_path,
            args,
            device_serial=self.device_serial,
            timeout=timeout,
            check=check,
        )

    def manual_package_removal(self) -> None:
        """Allow users to remove a package by typing its name or app label"""
        if not self.check_device_connection():
            return

        installed_packages = self.get_installed_packages()

        if not installed_packages:
            print("No packages found or failed to retrieve package list")
            return

        print("\nManual Package Removal")
        print("=" * 50)
        if self.test_mode:
            print("Running in test mode - no actual changes will be made")
            print("-" * 50)

        print("Type the full package name (e.g., com.android.chrome) or part of the app name.")
        print("Type 'back' to return to the previous menu.")

        risk_colors = {
            'safe': '[SAFE]',
            'caution': '[CAUTION]',
            'dangerous': '[DANGER]',
            'unknown': '[UNKNOWN]'
        }

        while True:
            query = input("\nEnter package or app name: ").strip()

            if not query:
                print("Please enter a value or type 'back' to exit.")
                continue

            if query.lower() in {'back', 'exit', 'quit', 'q'}:
                print("Returning to main menu.")
                return

            matches = []
            seen = set()
            lowered_query = query.lower()

            for package in installed_packages:
                app_label = self.get_app_name(package)
                if lowered_query in package.lower() or lowered_query in app_label.lower():
                    if package in seen:
                        continue
                    seen.add(package)
                    metadata = self.get_package_metadata(package)
                    matches.append({
                        'package': package,
                        'name': app_label,
                        'risk': metadata['risk'],
                        'description': metadata['description']
                    })

            if not matches:
                print(f"No packages found matching '{query}'. Try again.")
                continue

            matches.sort(key=lambda x: x['name'].lower())

            print("\nMatches found:")
            print("-" * 50)
            for idx, app in enumerate(matches, 1):
                risk_indicator = risk_colors.get(app['risk'], '[UNKNOWN]')
                print(f"{idx:3d}. {risk_indicator} {app['name']}")
                print(f"     Package: {app['package']}")
                print(f"     Description: {app['description']}")
                print()

            if len(matches) == 1:
                selected_packages = [matches[0]['package']]
            else:
                print("Select apps to remove by entering numbers, ranges (1-3), or 'all'.")
                print("Type 'back' to search again without removing anything.")

                while True:
                    selection = input("Selection: ").strip().lower()

                    if not selection:
                        print("Please enter a selection or 'back'.")
                        continue

                    if selection in {'back', 'cancel', 'q'}:
                        selected_packages = []
                        break

                    if selection == 'all':
                        selected_packages = [app['package'] for app in matches]
                        break

                    try:
                        selected_indices = []
                        for part in selection.split(','):
                            part = part.strip()
                            if '-' in part:
                                start, end = map(int, part.split('-'))
                                selected_indices.extend(range(start, end + 1))
                            else:
                                selected_indices.append(int(part))

                        valid_indices = []
                        for idx in selected_indices:
                            if 1 <= idx <= len(matches):
                                valid_indices.append(idx)
                            else:
                                print(f"Warning: Index {idx} is out of range (1-{len(matches)})")

                        if valid_indices:
                            selected_packages = [matches[idx - 1]['package'] for idx in sorted(set(valid_indices))]
                            break
                        else:
                            print("No valid selections detected. Try again.")
                    except ValueError:
                        print("Invalid format. Use numbers (1,2,5) or ranges (2-4).")

            if not selected_packages:
                print("No packages selected for removal.")
                continue

            print("=" * 50)
            if input("Create backup before removal? (y/n): ").lower().strip() == 'y':
                self.backup_packages(selected_packages)

            confirm_text = "yes" if not self.test_mode else "y"
            warning_text = (
                "TEST MODE: This will simulate removing the selected apps"
                if self.test_mode else
                "This will remove the selected apps from the current user"
            )
            print(f"\n{warning_text}")
            if input(f"Proceed with removal? (type '{confirm_text}' to confirm): ").lower().strip() == confirm_text:
                self.remove_packages(selected_packages, skip_connection_check=True)

                if input("Remove another app? (y/n): ").lower().strip() == 'y':
                    installed_packages = [pkg for pkg in installed_packages if pkg not in selected_packages]
                    for pkg in selected_packages:
                        self._app_name_cache.pop(pkg, None)
                    if not self.test_mode:
                        installed_packages = self.get_installed_packages()
                        if not installed_packages:
                            print("No additional packages detected on the device.")
                            return
                    continue
                else:
                    print("Manual removal complete.")
                    return
            else:
                print("Removal cancelled for the selected apps.")

