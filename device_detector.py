import re
from typing import Optional, List

from core.adb_utils import (
    ADBCommandError,
    ADBNotFoundError,
    DeviceSelectionError,
    DeviceState,
    DEFAULT_TCPIP_PORT,
    activate_tcpip_mode,
    connect_wifi_device,
    is_wifi_serial,
    list_devices,
    pair_device,
    resolve_adb_path,
    run_command,
)

class DeviceDetector:
    
    BRAND_PATTERNS = {
        'samsung': [r'samsung', r'sm-', r'galaxy'],
        'xiaomi': [r'xiaomi', r'redmi', r'poco', r'mi '],
        'oppo': [r'oppo', r'cph'],
        'vivo': [r'vivo', r'v\d+', r'iqoo'],
        'realme': [r'realme', r'rmx'],
        'tecno': [r'tecno', r'spark', r'camon', r'transsion'],
        'oneplus': [r'oneplus', r'op', r'1\+', r'nord'],
        'huawei': [r'huawei', r'honor', r'hma', r'lya', r'eva'],
        'honor': [r'honor', r'hry', r'bkl', r'col'],
        'motorola': [r'motorola', r'moto', r'xt\d+'],
        'nothing': [r'nothing', r'phone'],
        'asus': [r'asus', r'zenfone', r'rog'],
        'google': [r'google', r'pixel'],
        'infinix': [r'infinix', r'hot', r'note', r'zero'],
        'lenovo': [r'lenovo', r'zuk', r'vibe']
    }
    
    def __init__(self, test_mode: bool = False):
        self.device_info = None
        self.test_mode = test_mode
        self.adb_path: Optional[str] = None
        self.device_serial: Optional[str] = None
        self._last_wifi_endpoint: Optional[str] = None
    
    def get_device_info(self) -> Optional[dict]:
        while True:
            if self.test_mode:
                print("TEST MODE: Using mock device information")
                self.device_info = {
                    'brand': 'test_brand',
                    'model': 'test_model',
                    'manufacturer': 'test_manufacturer',
                    'detected_brand': 'samsung'
                }
                self.device_serial = None
                return self.device_info

            if not self.adb_path:
                try:
                    self.adb_path = resolve_adb_path()
                except ADBNotFoundError as exc:
                    print(str(exc))
                    decision = self._prompt_enable_test_mode()
                    if decision == 'test':
                        continue
                    if decision == 'quit':
                        return None
                    continue

            try:
                devices = list_devices(self.adb_path)
            except ADBCommandError as exc:
                print("Failed to communicate with adb. Ensure the platform tools are installed and your device is connected.")
                if exc.stderr:
                    print(exc.stderr.strip())
                if self._prompt_wifi_connection("Attempt to reconnect over Wi-Fi ADB?"):
                    continue
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    continue
                if decision == 'quit':
                    return None
                continue

            if not devices:
                print("No devices detected. Ensure USB debugging is enabled and the device is unlocked.")
                if self._prompt_wifi_connection("Would you like to try Wi-Fi ADB instead?"):
                    continue
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    continue
                if decision == 'quit':
                    return None
                continue

            authorized = [device for device in devices if device.state == 'device']
            unauthorized = [device for device in devices if device.state != 'device']

            if unauthorized:
                print("Detected devices that are not ready:")
                for device in unauthorized:
                    print(f"  - {device.summary()}")
                print("Unlock your device and accept the USB debugging prompt, then try again.")
                if self._prompt_wifi_connection("Switch to Wi-Fi debugging?"):
                    continue

            if not authorized:
                if self._prompt_wifi_connection("No authorised devices detected. Try Wi-Fi ADB?"):
                    continue
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    continue
                if decision == 'quit':
                    return None
                continue

            selected = self._select_device(authorized)
            if not selected:
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    continue
                if decision == 'quit':
                    return None
                continue

            self.device_serial = selected.serial
            if is_wifi_serial(self.device_serial):
                self._last_wifi_endpoint = self.device_serial

            try:
                brand = self._get_prop('ro.product.brand')
                model = self._get_prop('ro.product.model')
                manufacturer = self._get_prop('ro.product.manufacturer')
            except ADBCommandError as exc:
                print("Failed to read device information via adb.")
                if exc.stderr:
                    print(exc.stderr.strip())
                if 'unauthorized' in (exc.stderr or exc.stdout or '').lower():
                    print("Authorize this computer on your device and try again.")
                decision = self._prompt_enable_test_mode()
                if decision == 'test':
                    continue
                if decision == 'quit':
                    return None
                continue

            brand = brand.lower()
            model = model.lower()
            manufacturer = manufacturer.lower()

            detected_brand = self._detect_brand(brand, model, manufacturer)

            self.device_info = {
                'brand': brand,
                'model': model,
                'manufacturer': manufacturer,
                'detected_brand': detected_brand
            }

            return self.device_info
    
    def _detect_brand(self, brand: str, model: str, manufacturer: str) -> Optional[str]:
        search_text = f"{brand} {model} {manufacturer}".lower()
        
        for brand_name, patterns in self.BRAND_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, search_text):
                    return brand_name
        
        return None
    
    def get_supported_remover(self):
        if not self.device_info:
            self.get_device_info()
        
        if not self.device_info or not self.device_info['detected_brand']:
            if self.test_mode:
                print("\nAvailable brands for testing:")
                print("1. Samsung")
                print("2. Xiaomi")
                print("3. Oppo")
                print("4. Vivo")
                print("5. Realme")
                print("6. Tecno")
                print("7. OnePlus")
                print("8. Huawei")
                print("9. Honor")
                print("10. Motorola")
                print("11. Nothing")
                print("12. Asus")
                print("13. Google Pixel")
                print("14. Infinix")
                print("15. Lenovo")
                choice = input("Select brand for testing (1-15): ").strip()
                
                brand_map = {
                    '1': 'samsung',
                    '2': 'xiaomi',
                    '3': 'oppo',
                    '4': 'vivo',
                    '5': 'realme',
                    '6': 'tecno',
                    '7': 'oneplus',
                    '8': 'huawei',
                    '9': 'honor',
                    '10': 'motorola',
                    '11': 'nothing',
                    '12': 'asus',
                    '13': 'google',
                    '14': 'infinix',
                    '15': 'lenovo'
                }
                
                brand = brand_map.get(choice)
                if not brand:
                    print("Invalid choice")
                    return None
            else:
                return None
        else:
            brand = self.device_info['detected_brand']
        
        try:
            if brand == 'samsung':
                from Samsung.samsung_remover import SamsungRemover
                remover = SamsungRemover(test_mode=self.test_mode)
            elif brand == 'xiaomi':
                from Xiaomi.xiaomi_remover import XiaomiRemover
                remover = XiaomiRemover(test_mode=self.test_mode)
            elif brand == 'oppo':
                from Oppo.oppo_remover import OppoRemover
                remover = OppoRemover(test_mode=self.test_mode)
            elif brand == 'vivo':
                from Vivo.vivo_remover import VivoRemover
                remover = VivoRemover(test_mode=self.test_mode)
            elif brand == 'realme':
                from Realme.realme_remover import RealmeRemover
                remover = RealmeRemover(test_mode=self.test_mode)
            elif brand == 'tecno':
                from Tecno.tecno_remover import TecnoRemover
                remover = TecnoRemover(test_mode=self.test_mode)
            elif brand == 'oneplus':
                from OnePlus.oneplus_remover import OnePlusRemover
                remover = OnePlusRemover(test_mode=self.test_mode)
            elif brand == 'huawei':
                from Huawei.huawei_remover import HuaweiRemover
                remover = HuaweiRemover(test_mode=self.test_mode)
            elif brand == 'honor':
                from Honor.honor_remover import HonorRemover
                remover = HonorRemover(test_mode=self.test_mode)
            elif brand == 'motorola':
                from Motorola.motorola_remover import MotorolaRemover
                remover = MotorolaRemover(test_mode=self.test_mode)
            elif brand == 'nothing':
                from Nothing.nothing_remover import NothingRemover
                remover = NothingRemover(test_mode=self.test_mode)
            elif brand == 'asus':
                from Asus.asus_remover import AsusRemover
                remover = AsusRemover(test_mode=self.test_mode)
            elif brand == 'google':
                from Google.google_remover import GoogleRemover
                remover = GoogleRemover(test_mode=self.test_mode)
            elif brand == 'infinix':
                from Infinix.infinix_remover import InfinixRemover
                remover = InfinixRemover(test_mode=self.test_mode)
            elif brand == 'lenovo':
                from Lenovo.lenovo_remover import LenovoRemover
                remover = LenovoRemover(test_mode=self.test_mode)
            else:
                print(f"Brand '{brand}' is not yet supported")
                return None

            remover.configure_adb(self.adb_path, self.device_serial)
            return remover

        except ImportError as e:
            print(f"Failed to load remover for {brand}: {e}")
            return None
    
    def print_device_info(self):
        if not self.device_info:
            self.get_device_info()
        
        if self.device_info:
            mode_text = " (TEST MODE)" if self.test_mode else ""
            print(f"Device Information{mode_text}:")
            print(f"  Brand: {self.device_info['brand']}")
            print(f"  Model: {self.device_info['model']}")
            print(f"  Manufacturer: {self.device_info['manufacturer']}")
            print(f"  Detected Brand: {self.device_info['detected_brand'] or 'Unknown'}")
        else:
            print("No device information available")

    def _prompt_enable_test_mode(self) -> str:
        while True:
            choice = input(
                "Do you want to run in test mode anyway? (y/n or 'quit' to cancel): "
            ).lower().strip()

            if choice in {'y', 'yes'}:
                self.test_mode = True
                print("Continuing in test mode - adb commands will be mocked")
                return 'test'

            if choice in {'n', 'no'}:
                print("Okay, we'll keep trying to detect the device normally.")
                return 'retry'

            if choice in {'quit', 'q', 'exit', 'cancel'}:
                print("Cancelling device detection.")
                return 'quit'

            print("Please respond with 'y', 'n', or type 'quit' to cancel.")

    def _prompt_connection_retry(self) -> str:
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

    def _select_device(self, devices: List[DeviceState]) -> Optional[DeviceState]:
        if not devices:
            return None

        if len(devices) == 1:
            device = devices[0]
            print(f"Using device: {device.summary()}")
            return device

        print("Multiple authorised devices detected:")
        for index, device in enumerate(devices, start=1):
            print(f"  {index}. {device.summary()}")

        while True:
            selection = input(f"Select device (1-{len(devices)}) or 'c' to cancel: ").strip().lower()
            if selection in {'c', 'cancel', 'q', 'quit'}:
                print("Device selection cancelled")
                return None

            try:
                idx = int(selection)
            except ValueError:
                print("Invalid selection. Please try again.")
                continue

            if 1 <= idx <= len(devices):
                device = devices[idx - 1]
                print(f"Using device: {device.summary()}")
                return device

            print("Selection out of range. Please try again.")

    def _get_prop(self, property_name: str) -> str:
        if not self.adb_path or not self.device_serial:
            raise ADBCommandError("ADB context not initialised")

        result = run_command(
            self.adb_path,
            ['shell', 'getprop', property_name],
            device_serial=self.device_serial,
            timeout=10,
            check=True,
        )
        return result.stdout.strip()

    def enable_tcpip_on_current_device(self, port: int = DEFAULT_TCPIP_PORT) -> bool:
        if not self.adb_path or not self.device_serial:
            return False

        try:
            activate_tcpip_mode(
                self.adb_path,
                device_serial=self.device_serial,
                port=port,
            )
            return True
        except ADBCommandError as exc:
            print("Failed to enable TCP/IP mode on the connected device.")
            if exc.stderr:
                print(exc.stderr.strip())
            return False

    def connect_via_wifi(
        self,
        endpoint: Optional[str] = None,
        *,
        pairing_host: Optional[str] = None,
        pairing_code: Optional[str] = None,
    ) -> bool:
        if endpoint:
            if ':' not in endpoint:
                endpoint = f"{endpoint}:{DEFAULT_TCPIP_PORT}"
            pairing_host = pairing_host or endpoint
            try:
                if pairing_code:
                    pair_device(self.adb_path or resolve_adb_path(), pairing_host, pairing_code)
                device = connect_wifi_device(self.adb_path or resolve_adb_path(), endpoint)
            except (ADBCommandError, DeviceSelectionError) as exc:
                print("Failed to connect over Wi-Fi.")
                if isinstance(exc, ADBCommandError) and exc.stderr:
                    print(exc.stderr.strip())
                if isinstance(exc, DeviceSelectionError) and exc.devices:
                    print("Currently visible devices:")
                    for dev in exc.devices:
                        print(f"  - {dev.summary()}")
                return False

            self.adb_path = self.adb_path or resolve_adb_path()
            self.device_serial = device.serial
            self._last_wifi_endpoint = endpoint
            print(f"Connected to {device.summary()} over Wi-Fi.")
            return True

        return self._connect_via_wifi()

    def _prompt_wifi_connection(self, prompt: str) -> bool:
        while True:
            answer = input(f"{prompt} (y/n): ").strip().lower()
            if answer in {'y', 'yes'}:
                return self._connect_via_wifi()
            if answer in {'n', 'no', 'skip', 's'}:
                return False
            print("Please answer with 'y' or 'n'.")

    def _connect_via_wifi(self) -> bool:
        if not self.adb_path:
            try:
                self.adb_path = resolve_adb_path()
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
            print("No address entered. Skipping Wi-Fi connection.")
            return False

        if ':' not in endpoint:
            endpoint = f"{endpoint}:{DEFAULT_TCPIP_PORT}"

        needs_pairing: Optional[bool] = None
        while needs_pairing is None:
            decision = input("Does the device show a pairing code? (y/n): ").strip().lower()
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
                pair_device(self.adb_path, pair_host, pairing_code)
                print(f"Paired with {pair_host}.")
            except ADBCommandError as exc:
                print("Failed to pair with the device.")
                if exc.stderr:
                    print(exc.stderr.strip())
                return False

        try:
            device = connect_wifi_device(self.adb_path, endpoint)
        except ADBCommandError as exc:
            print("Failed to connect over Wi-Fi.")
            if exc.stderr:
                print(exc.stderr.strip())
            return False
        except DeviceSelectionError as exc:
            print("Connected but the device did not appear in the adb list.")
            if exc.devices:
                print("Currently visible devices:")
                for device in exc.devices:
                    print(f"  - {device.summary()}")
            return False

        self.device_serial = device.serial
        self._last_wifi_endpoint = endpoint
        print(f"Connected to {device.summary()} over Wi-Fi.")
        return True
