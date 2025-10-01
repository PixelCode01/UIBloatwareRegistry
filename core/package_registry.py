import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path


class PackageRegistry:
    def __init__(self, registry_file: str = None):
        if registry_file is None:
            root_dir = Path(__file__).parent.parent
            registry_file = root_dir / 'packages_registry.json'
        
        self.registry_file = Path(registry_file)
        self.registry_data: Dict = {}
        self._load_registry()
    
    def _load_registry(self) -> None:
        try:
            if self.registry_file.exists():
                with open(self.registry_file, 'r', encoding='utf-8') as f:
                    self.registry_data = json.load(f)
            else:
                raise FileNotFoundError(f"Registry file not found: {self.registry_file}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in registry file: {e}")
        except Exception as e:
            raise RuntimeError(f"Failed to load registry: {e}")
    
    def save_registry(self) -> None:
        try:
            with open(self.registry_file, 'w', encoding='utf-8') as f:
                json.dump(self.registry_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise RuntimeError(f"Failed to save registry: {e}")
    
    def get_brands(self) -> List[str]:
        return list(self.registry_data.get('brands', {}).keys())
    
    def get_brand_name(self, brand_id: str) -> Optional[str]:
        brand_data = self.registry_data.get('brands', {}).get(brand_id)
        if brand_data:
            return brand_data.get('name', brand_id.title())
        return None
    
    def get_brand_categories(self, brand: str) -> Dict[str, Dict]:
        brand_data = self.registry_data.get('brands', {}).get(brand.lower(), {})
        return brand_data.get('categories', {})
    
    def get_packages_for_brand(self, brand: str) -> Dict[str, List[Dict]]:
        categories = self.get_brand_categories(brand)
        result = {}
        
        for category_id, category_data in categories.items():
            result[category_id] = category_data.get('packages', [])
        
        return result
    
    def get_all_packages_flat(self, brand: str) -> List[Dict]:
        packages = []
        categories = self.get_packages_for_brand(brand)
        
        for category_id, package_list in categories.items():
            for package in package_list:
                package_copy = package.copy()
                package_copy['category'] = category_id
                packages.append(package_copy)
        
        return packages
    
    def get_package_info(self, brand: str, package_name: str) -> Optional[Dict]:
        all_packages = self.get_all_packages_flat(brand)
        for package in all_packages:
            if package.get('name') == package_name:
                return package
        return None
    
    def add_package(self, brand: str, category: str, package_data: Dict) -> bool:
        try:
            brand = brand.lower()
            
            if brand not in self.registry_data.get('brands', {}):
                self.registry_data.setdefault('brands', {})[brand] = {
                    'name': brand.title(),
                    'categories': {}
                }
            
            brand_data = self.registry_data['brands'][brand]
            if category not in brand_data.get('categories', {}):
                brand_data.setdefault('categories', {})[category] = {
                    'name': category.replace('_', ' ').title(),
                    'description': f'{category.replace("_", " ").title()} applications',
                    'packages': []
                }
            
            packages = brand_data['categories'][category]['packages']
            
            for existing in packages:
                if existing['name'] == package_data['name']:
                    return False
            
            required_fields = ['name', 'description', 'risk']
            if not all(field in package_data for field in required_fields):
                raise ValueError(f"Package data must contain: {', '.join(required_fields)}")
            
            packages.append(package_data)
            return True
            
        except Exception as e:
            print(f"Error adding package: {e}")
            return False
    
    def remove_package(self, brand: str, package_name: str) -> bool:
        try:
            brand = brand.lower()
            categories = self.get_brand_categories(brand)
            
            for category_id, category_data in categories.items():
                packages = category_data.get('packages', [])
                for i, package in enumerate(packages):
                    if package['name'] == package_name:
                        packages.pop(i)
                        return True
            
            return False
            
        except Exception as e:
            print(f"Error removing package: {e}")
            return False
    
    def update_package(self, brand: str, package_name: str, updates: Dict) -> bool:
        try:
            brand = brand.lower()
            categories = self.get_brand_categories(brand)
            
            for category_id, category_data in categories.items():
                packages = category_data.get('packages', [])
                for package in packages:
                    if package['name'] == package_name:
                        package.update(updates)
                        return True
            
            return False
            
        except Exception as e:
            print(f"Error updating package: {e}")
            return False
    
    def get_risk_level_info(self, risk_level: str) -> Optional[Dict]:
        return self.registry_data.get('risk_levels', {}).get(risk_level)
    
    def get_all_risk_levels(self) -> Dict[str, Dict]:
        return self.registry_data.get('risk_levels', {})
    
    def convert_to_legacy_format(self, brand: str) -> Dict:
        categories_data = self.get_brand_categories(brand)
        legacy_format = {'categories': {}}
        
        for category_id, category_data in categories_data.items():
            packages = category_data.get('packages', [])
            legacy_format['categories'][category_id] = packages
        
        return legacy_format
    
    def search_packages(self, query: str, brand: Optional[str] = None) -> List[Dict]:
        results = []
        query_lower = query.lower()
        
        brands_to_search = [brand.lower()] if brand else self.get_brands()
        
        for brand_id in brands_to_search:
            packages = self.get_all_packages_flat(brand_id)
            for package in packages:
                package_name = package.get('name', '').lower()
                description = package.get('description', '').lower()
                category = package.get('category', '').lower()
                
                # Search in multiple fields: name, description, category
                # Also search in package name parts (split by dots)
                name_parts = package_name.split('.')
                
                if (query_lower in package_name or 
                    query_lower in description or
                    query_lower in category or
                    any(query_lower in part for part in name_parts)):
                    package_copy = package.copy()
                    package_copy['brand'] = brand_id
                    results.append(package_copy)
        
        return results
    
    def get_common_search_terms(self) -> List[str]:
        """Get a list of common search terms from the registry"""
        terms = set()
        
        for brand_id in self.get_brands():
            packages = self.get_all_packages_flat(brand_id)
            for package in packages:
                # Extract key terms from descriptions
                desc = package.get('description', '')
                # Split on spaces and common separators
                words = desc.lower().replace(',', ' ').replace('-', ' ').split()
                for word in words:
                    if len(word) > 3:  # Only words longer than 3 chars
                        terms.add(word)
        
        # Sort and return top terms
        return sorted(list(terms))[:20]


def get_registry() -> PackageRegistry:
    return PackageRegistry()
