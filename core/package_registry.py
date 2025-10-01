"""
Package Registry Manager

This module provides utilities for managing the centralized bloatware package registry.
It allows loading, querying, and modifying package data from the registry file.
"""

import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path


class PackageRegistry:
    """Manager for the centralized package registry"""
    
    def __init__(self, registry_file: str = None):
        """
        Initialize the package registry
        
        Args:
            registry_file: Path to the registry JSON file. If None, uses default location.
        """
        if registry_file is None:
            # Default to packages_registry.json in the root directory
            root_dir = Path(__file__).parent.parent
            registry_file = root_dir / 'packages_registry.json'
        
        self.registry_file = Path(registry_file)
        self.registry_data: Dict = {}
        self._load_registry()
    
    def _load_registry(self) -> None:
        """Load the registry from the JSON file"""
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
        """Save the current registry data back to the file"""
        try:
            with open(self.registry_file, 'w', encoding='utf-8') as f:
                json.dump(self.registry_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise RuntimeError(f"Failed to save registry: {e}")
    
    def get_brands(self) -> List[str]:
        """Get list of all supported brands"""
        return list(self.registry_data.get('brands', {}).keys())
    
    def get_brand_name(self, brand_id: str) -> Optional[str]:
        """Get the display name for a brand"""
        brand_data = self.registry_data.get('brands', {}).get(brand_id)
        if brand_data:
            return brand_data.get('name', brand_id.title())
        return None
    
    def get_brand_categories(self, brand: str) -> Dict[str, Dict]:
        """Get all categories for a specific brand"""
        brand_data = self.registry_data.get('brands', {}).get(brand.lower(), {})
        return brand_data.get('categories', {})
    
    def get_packages_for_brand(self, brand: str) -> Dict[str, List[Dict]]:
        """
        Get all packages for a specific brand, organized by category
        
        Args:
            brand: Brand identifier (e.g., 'samsung', 'xiaomi')
            
        Returns:
            Dictionary mapping category names to lists of package dictionaries
        """
        categories = self.get_brand_categories(brand)
        result = {}
        
        for category_id, category_data in categories.items():
            result[category_id] = category_data.get('packages', [])
        
        return result
    
    def get_all_packages_flat(self, brand: str) -> List[Dict]:
        """
        Get all packages for a brand as a flat list
        
        Args:
            brand: Brand identifier
            
        Returns:
            List of package dictionaries with added 'category' field
        """
        packages = []
        categories = self.get_packages_for_brand(brand)
        
        for category_id, package_list in categories.items():
            for package in package_list:
                package_copy = package.copy()
                package_copy['category'] = category_id
                packages.append(package_copy)
        
        return packages
    
    def get_package_info(self, brand: str, package_name: str) -> Optional[Dict]:
        """
        Get information about a specific package
        
        Args:
            brand: Brand identifier
            package_name: Full package name (e.g., 'com.samsung.android.bixby.agent')
            
        Returns:
            Package dictionary or None if not found
        """
        all_packages = self.get_all_packages_flat(brand)
        for package in all_packages:
            if package.get('name') == package_name:
                return package
        return None
    
    def add_package(self, brand: str, category: str, package_data: Dict) -> bool:
        """
        Add a new package to the registry
        
        Args:
            brand: Brand identifier
            category: Category identifier
            package_data: Dictionary with 'name', 'description', and 'risk' keys
            
        Returns:
            True if successful, False otherwise
        """
        try:
            brand = brand.lower()
            
            # Ensure brand exists
            if brand not in self.registry_data.get('brands', {}):
                self.registry_data.setdefault('brands', {})[brand] = {
                    'name': brand.title(),
                    'categories': {}
                }
            
            # Ensure category exists
            brand_data = self.registry_data['brands'][brand]
            if category not in brand_data.get('categories', {}):
                brand_data.setdefault('categories', {})[category] = {
                    'name': category.replace('_', ' ').title(),
                    'description': f'{category.replace("_", " ").title()} applications',
                    'packages': []
                }
            
            # Add package
            packages = brand_data['categories'][category]['packages']
            
            # Check for duplicates
            for existing in packages:
                if existing['name'] == package_data['name']:
                    return False  # Package already exists
            
            # Validate package data
            required_fields = ['name', 'description', 'risk']
            if not all(field in package_data for field in required_fields):
                raise ValueError(f"Package data must contain: {', '.join(required_fields)}")
            
            packages.append(package_data)
            return True
            
        except Exception as e:
            print(f"Error adding package: {e}")
            return False
    
    def remove_package(self, brand: str, package_name: str) -> bool:
        """
        Remove a package from the registry
        
        Args:
            brand: Brand identifier
            package_name: Full package name to remove
            
        Returns:
            True if successful, False otherwise
        """
        try:
            brand = brand.lower()
            categories = self.get_brand_categories(brand)
            
            for category_id, category_data in categories.items():
                packages = category_data.get('packages', [])
                for i, package in enumerate(packages):
                    if package['name'] == package_name:
                        packages.pop(i)
                        return True
            
            return False  # Package not found
            
        except Exception as e:
            print(f"Error removing package: {e}")
            return False
    
    def update_package(self, brand: str, package_name: str, updates: Dict) -> bool:
        """
        Update a package's information
        
        Args:
            brand: Brand identifier
            package_name: Full package name
            updates: Dictionary of fields to update
            
        Returns:
            True if successful, False otherwise
        """
        try:
            brand = brand.lower()
            categories = self.get_brand_categories(brand)
            
            for category_id, category_data in categories.items():
                packages = category_data.get('packages', [])
                for package in packages:
                    if package['name'] == package_name:
                        package.update(updates)
                        return True
            
            return False  # Package not found
            
        except Exception as e:
            print(f"Error updating package: {e}")
            return False
    
    def get_risk_level_info(self, risk_level: str) -> Optional[Dict]:
        """Get information about a risk level"""
        return self.registry_data.get('risk_levels', {}).get(risk_level)
    
    def get_all_risk_levels(self) -> Dict[str, Dict]:
        """Get all risk level definitions"""
        return self.registry_data.get('risk_levels', {})
    
    def convert_to_legacy_format(self, brand: str) -> Dict:
        """
        Convert registry data to the legacy format used by BloatwareRemover
        
        Args:
            brand: Brand identifier
            
        Returns:
            Dictionary in the old format with 'categories' key
        """
        categories_data = self.get_brand_categories(brand)
        legacy_format = {'categories': {}}
        
        for category_id, category_data in categories_data.items():
            packages = category_data.get('packages', [])
            legacy_format['categories'][category_id] = packages
        
        return legacy_format
    
    def search_packages(self, query: str, brand: Optional[str] = None) -> List[Dict]:
        """
        Search for packages by name or description
        
        Args:
            query: Search query (case-insensitive)
            brand: Optional brand to limit search to
            
        Returns:
            List of matching packages with brand and category information
        """
        results = []
        query_lower = query.lower()
        
        brands_to_search = [brand.lower()] if brand else self.get_brands()
        
        for brand_id in brands_to_search:
            packages = self.get_all_packages_flat(brand_id)
            for package in packages:
                if (query_lower in package.get('name', '').lower() or 
                    query_lower in package.get('description', '').lower()):
                    package_copy = package.copy()
                    package_copy['brand'] = brand_id
                    results.append(package_copy)
        
        return results


def get_registry() -> PackageRegistry:
    """Get the default package registry instance"""
    return PackageRegistry()
