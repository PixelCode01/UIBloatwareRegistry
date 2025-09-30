import re
from typing import Optional, List

from core.adb_utils import (
    ADBCommandError,
    ADBNotFoundError,
    DeviceState,
    list_devices,
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
    
    def get_device_info(self) -> Optional[dict]:
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
                if self._prompt_enable_test_mode():
                    return self.get_device_info()
                return None

        try:
            devices = list_devices(self.adb_path)
        except ADBCommandError as exc:
            print("Failed to communicate with adb. Ensure the platform tools are installed and your device is connected.")
            if exc.stderr:
                print(exc.stderr.strip())
            if self._prompt_enable_test_mode():
                return self.get_device_info()
            return None

        if not devices:
            print("No devices detected. Ensure USB debugging is enabled and the device is unlocked.")
            if self._prompt_enable_test_mode():
                return self.get_device_info()
            return None

        authorized = [device for device in devices if device.state == 'device']
        unauthorized = [device for device in devices if device.state != 'device']

        if unauthorized:
            print("Detected devices that are not ready:")
            for device in unauthorized:
                print(f"  - {device.summary()}")
            print("Unlock your device and accept the USB debugging prompt, then try again.")

        if not authorized:
            if self._prompt_enable_test_mode():
                return self.get_device_info()
            return None

        selected = self._select_device(authorized)
        if not selected:
            return None

        self.device_serial = selected.serial

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
            if self._prompt_enable_test_mode():
                return self.get_device_info()
            return None

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

    def _prompt_enable_test_mode(self) -> bool:
        choice = input("Do you want to run in test mode anyway? (y/n): ").lower().strip()
        if choice == 'y':
            self.test_mode = True
            print("Continuing in test mode - adb commands will be mocked")
            return True
        return False

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