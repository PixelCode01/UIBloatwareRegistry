import subprocess
import json
import os
import logging
from typing import List, Dict, Optional
from abc import ABC, abstractmethod

class BloatwareRemover(ABC):
    """Base class for brand-specific bloatware removal"""
    
    def __init__(self, brand: str, config_file: str = None, test_mode: bool = False):
        self.brand = brand
        self.config_file = config_file or f"{brand.lower()}_config.json"
        self.test_mode = test_mode
        self.logger = self._setup_logging()
        self.packages = self._load_packages()
        
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
        """Load package configuration from JSON file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            else:
                return self._get_default_packages()
        except Exception as e:
            self.logger.error(f"Failed to load config: {e}")
            return self._get_default_packages()
    
    @abstractmethod
    def _get_default_packages(self) -> Dict:
        """Return default package configuration for the brand"""
        pass
    
    def check_device_connection(self) -> bool:
        """Check if device is connected via ADB"""
        if self.test_mode:
            print("Running in test mode - skipping device connection check")
            return True
            
        try:
            result = subprocess.run(['adb', 'devices'], 
                                  capture_output=True, text=True, check=True)
            devices = [line for line in result.stdout.split('\n') 
                      if line.strip() and not line.startswith('List')]
            
            if not devices:
                print("No devices connected. Please connect your device and enable USB debugging.")
                
                # Ask user if they want to continue in test mode
                choice = input("Do you want to run in test mode anyway? (y/n): ").lower().strip()
                if choice == 'y':
                    print("Continuing in test mode - no actual changes will be made")
                    self.test_mode = True
                    return True
                return False
            
            print(f"Found {len(devices)} connected device(s)")
            return True
            
        except subprocess.CalledProcessError:
            print("ADB not found. Please install Android Debug Bridge.")
            choice = input("Do you want to run in test mode anyway? (y/n): ").lower().strip()
            if choice == 'y':
                print("Continuing in test mode - no actual changes will be made")
                self.test_mode = True
                return True
            return False
        except FileNotFoundError:
            print("ADB not found in PATH. Please install Android SDK platform tools.")
            choice = input("Do you want to run in test mode anyway? (y/n): ").lower().strip()
            if choice == 'y':
                print("Continuing in test mode - no actual changes will be made")
                self.test_mode = True
                return True
            return False
    
    def get_installed_packages(self) -> List[str]:
        """Get list of installed packages on device"""
        if self.test_mode:
            # Return all configured packages for testing
            return self._get_all_packages()
            
        try:
            result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], 
                                  capture_output=True, text=True, check=True)
            packages = [line.replace('package:', '').strip() 
                       for line in result.stdout.split('\n') if line.startswith('package:')]
            return packages
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to get installed packages: {e}")
            return []
    
    def uninstall_package(self, package: str) -> bool:
        """Uninstall a single package"""
        if self.test_mode:
            print(f"TEST MODE: Would remove package: {package}")
            self.logger.info(f"TEST MODE: Would remove package: {package}")
            return True
            
        try:
            result = subprocess.run(['adb', 'shell', 'pm', 'uninstall', '--user', '0', package], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f"Successfully removed: {package}")
                return True
            else:
                self.logger.warning(f"Failed to remove: {package} - {result.stderr.strip()}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error removing {package}: {e}")
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
        if self.test_mode:
            # Return mock app names for testing
            app_names = {
                'com.android.chrome': 'Chrome',
                'com.google.android.gm': 'Gmail',
                'com.facebook.katana': 'Facebook',
                'com.instagram.android': 'Instagram'
            }
            return app_names.get(package_name, f"Test App ({package_name.split('.')[-1]})")
        
        try:
            result = subprocess.run(['adb', 'shell', 'pm', 'dump', package_name], 
                                  capture_output=True, text=True, timeout=5)
            
            # Parse the dump output to find the app label
            for line in result.stdout.split('\n'):
                if 'applicationLabel=' in line:
                    label = line.split('applicationLabel=')[1].strip()
                    return label
                elif 'labelRes=' in line and 'labelRes=0x0' not in line:
                    # Try to get the label from resources
                    result2 = subprocess.run(['adb', 'shell', 'dumpsys', 'package', package_name], 
                                           capture_output=True, text=True, timeout=5)
                    for line2 in result2.stdout.split('\n'):
                        if 'versionName=' in line2:
                            break
                        if package_name in line2 and '=' in line2:
                            continue
            
            # Fallback: try to get from package manager
            result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages', '-f', package_name], 
                                  capture_output=True, text=True, timeout=5)
            if result.stdout.strip():
                return package_name.split('.')[-1].title()
                
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
            pass
        
        # Final fallback: use package name
        return package_name.split('.')[-1].title()

    def list_all_apps_removal(self) -> None:
        """List all installed apps and let user select which to remove"""
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
        
        # Filter out system packages that shouldn't be shown
        system_packages = [
            'android', 'com.android.systemui', 'com.android.settings',
            'com.android.launcher', 'com.android.phone', 'com.android.contacts'
        ]
        
        # Get app info for all packages
        print("Loading app information...")
        app_info = []
        
        for i, package in enumerate(installed_packages):
            if any(sys_pkg in package for sys_pkg in system_packages):
                continue
                
            if i % 50 == 0:  # Show progress every 50 apps
                print(f"Processed {i}/{len(installed_packages)} packages...")
            
            app_name = self.get_app_name(package)
            
            # Determine risk level from our configuration
            risk_level = 'unknown'
            description = 'User installed or system app'
            
            # Check if this package is in our known bloatware list
            categories = self.packages.get('categories', {})
            for category, package_list in categories.items():
                for package_info in package_list:
                    if package_info['name'] == package:
                        risk_level = package_info.get('risk', 'safe')
                        description = package_info.get('description', 'No description')
                        break
                if risk_level != 'unknown':
                    break
            
            app_info.append({
                'package': package,
                'name': app_name,
                'risk': risk_level,
                'description': description
            })
        
        # Sort apps by name for easier browsing
        app_info.sort(key=lambda x: x['name'].lower())
        
        print(f"\nFound {len(app_info)} applications")
        print("=" * 50)
        
        # Display apps with selection
        selected_packages = []
        risk_colors = {
            'safe': '[SAFE]',
            'caution': '[CAUTION]', 
            'dangerous': '[DANGER]',
            'unknown': '[UNKNOWN]'
        }
        
        print("Select apps to remove (y/n/s=skip category/q=quit):")
        print("-" * 50)
        
        for i, app in enumerate(app_info, 1):
            risk_indicator = risk_colors.get(app['risk'], '[UNKNOWN]')
            print(f"\n{i:3d}. {risk_indicator} {app['name']}")
            print(f"     Package: {app['package']}")
            print(f"     Description: {app['description']}")
            
            while True:
                choice = input("     Remove this app? (y/n/q=quit): ").lower().strip()
                
                if choice == 'q':
                    print("Quitting app selection...")
                    break
                elif choice == 'y':
                    selected_packages.append(app['package'])
                    print("     Added to removal list")
                    break
                elif choice == 'n':
                    break
                else:
                    print("     Please enter 'y' for yes, 'n' for no, or 'q' to quit")
            
            if choice == 'q':
                break
        
        # Process selected packages
        if selected_packages:
            print(f"\nSelected {len(selected_packages)} apps for removal:")
            for pkg in selected_packages:
                app_name = next((app['name'] for app in app_info if app['package'] == pkg), pkg)
                print(f"  - {app_name} ({pkg})")
            
            print()
            if input("Create backup before removal? (y/n): ").lower().strip() == 'y':
                self.backup_packages(selected_packages)
            
            confirm_text = "yes" if not self.test_mode else "y"
            warning_text = "This will remove the selected apps" if not self.test_mode else "TEST MODE: This will simulate removing the selected apps"
            print(f"\n{warning_text}")
            
            if input(f"Proceed with removal? (type '{confirm_text}' to confirm): ").lower().strip() == confirm_text:
                self.remove_packages(selected_packages)
            else:
                print("Removal cancelled")
        else:
            print("No apps selected for removal")

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
    
    def remove_packages(self, packages: List[str] = None) -> None:
        """Remove specified packages or all configured packages"""
        if not self.check_device_connection():
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