import subprocess
import json
import os
import logging
from typing import List, Dict, Optional
from abc import ABC, abstractmethod

class BloatwareRemover(ABC):
    """Base class for brand-specific bloatware removal"""
    
    def __init__(self, brand: str, config_file: str = None):
        self.brand = brand
        self.config_file = config_file or f"{brand.lower()}_config.json"
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
        try:
            result = subprocess.run(['adb', 'devices'], 
                                  capture_output=True, text=True, check=True)
            devices = [line for line in result.stdout.split('\n') 
                      if line.strip() and not line.startswith('List')]
            
            if not devices:
                print("No devices connected. Please connect your device and enable USB debugging.")
                return False
            
            print(f"Found {len(devices)} connected device(s)")
            return True
            
        except subprocess.CalledProcessError:
            print("ADB not found. Please install Android Debug Bridge.")
            return False
        except FileNotFoundError:
            print("ADB not found in PATH. Please install Android SDK platform tools.")
            return False
    
    def get_installed_packages(self) -> List[str]:
        """Get list of installed packages on device"""
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
            backup_data = {
                'brand': self.brand,
                'packages': packages,
                'timestamp': subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
            }
            
            with open(backup_file, 'w') as f:
                json.dump(backup_data, f, indent=2)
            
            print(f"Backup created: {backup_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to create backup: {e}")
            return False
    
    def interactive_removal(self) -> None:
        """Interactive package removal with user selection"""
        if not self.check_device_connection():
            return
        
        installed_packages = self.get_installed_packages()
        
        print(f"\n{self.brand} Bloatware Removal Tool")
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
        
        print(f"Starting removal of {len(packages)} packages...")
        
        success_count = 0
        failed_count = 0
        
        for package in packages:
            if self.uninstall_package(package):
                success_count += 1
            else:
                failed_count += 1
        
        print(f"\nRemoval complete:")
        print(f"  Successfully removed: {success_count}")
        print(f"  Failed to remove: {failed_count}")
        
        if failed_count > 0:
            print("Check the log file for details on failed removals")
    
    def _get_all_packages(self) -> List[str]:
        """Get all package names from configuration"""
        all_packages = []
        categories = self.packages.get('categories', {})
        
        for package_list in categories.values():
            for package_info in package_list:
                all_packages.append(package_info['name'])
        
        return all_packages