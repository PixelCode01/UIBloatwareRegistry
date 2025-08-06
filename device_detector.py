import subprocess
import re
from typing import Optional

class DeviceDetector:
    """Detect connected Android device brand and model"""
    
    BRAND_PATTERNS = {
        'samsung': [r'samsung', r'sm-', r'galaxy'],
        'xiaomi': [r'xiaomi', r'redmi', r'poco', r'mi '],
        'oppo': [r'oppo', r'cph', r'realme'],
        'vivo': [r'vivo', r'v\d+'],
        'realme': [r'realme', r'rmx'],
        'tecno': [r'tecno', r'spark', r'camon']
    }
    
    def __init__(self, test_mode: bool = False):
        self.device_info = None
        self.test_mode = test_mode
    
    def get_device_info(self) -> Optional[dict]:
        """Get device brand and model information"""
        if self.test_mode:
            # Return mock device info for testing
            print("TEST MODE: Using mock device information")
            self.device_info = {
                'brand': 'test_brand',
                'model': 'test_model',
                'manufacturer': 'test_manufacturer',
                'detected_brand': 'samsung'  # Default to Samsung for testing
            }
            return self.device_info
            
        try:
            # Get device properties
            brand_result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.brand'], 
                                        capture_output=True, text=True, check=True)
            model_result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.model'], 
                                        capture_output=True, text=True, check=True)
            manufacturer_result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.manufacturer'], 
                                               capture_output=True, text=True, check=True)
            
            brand = brand_result.stdout.strip().lower()
            model = model_result.stdout.strip().lower()
            manufacturer = manufacturer_result.stdout.strip().lower()
            
            detected_brand = self._detect_brand(brand, model, manufacturer)
            
            self.device_info = {
                'brand': brand,
                'model': model,
                'manufacturer': manufacturer,
                'detected_brand': detected_brand
            }
            
            return self.device_info
            
        except subprocess.CalledProcessError:
            print("Failed to get device information. Make sure device is connected.")
            choice = input("Do you want to run in test mode anyway? (y/n): ").lower().strip()
            if choice == 'y':
                self.test_mode = True
                return self.get_device_info()
            return None
        except FileNotFoundError:
            print("ADB not found. Please install Android SDK platform tools.")
            choice = input("Do you want to run in test mode anyway? (y/n): ").lower().strip()
            if choice == 'y':
                self.test_mode = True
                return self.get_device_info()
            return None
    
    def _detect_brand(self, brand: str, model: str, manufacturer: str) -> Optional[str]:
        """Detect brand based on device properties"""
        search_text = f"{brand} {model} {manufacturer}".lower()
        
        for brand_name, patterns in self.BRAND_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, search_text):
                    return brand_name
        
        return None
    
    def get_supported_remover(self):
        """Get appropriate remover class for detected device"""
        if not self.device_info:
            self.get_device_info()
        
        if not self.device_info or not self.device_info['detected_brand']:
            if self.test_mode:
                # Allow user to choose brand in test mode
                print("\nAvailable brands for testing:")
                print("1. Samsung")
                print("2. Xiaomi")
                choice = input("Select brand for testing (1-2): ").strip()
                
                if choice == '1':
                    brand = 'samsung'
                elif choice == '2':
                    brand = 'xiaomi'
                else:
                    print("Invalid choice")
                    return None
            else:
                return None
        else:
            brand = self.device_info['detected_brand']
        
        try:
            if brand == 'samsung':
                from Samsung.samsung_remover import SamsungRemover
                return SamsungRemover()
            elif brand == 'xiaomi':
                from Xiaomi.xiaomi_remover import XiaomiRemover
                return XiaomiRemover()
            # Add other brands as they are implemented
            else:
                print(f"Brand '{brand}' is not yet supported")
                return None
                
        except ImportError as e:
            print(f"Failed to load remover for {brand}: {e}")
            return None
    
    def print_device_info(self):
        """Print detected device information"""
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