#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))

from core.package_registry import PackageRegistry


class ContributionTool:
    def __init__(self):
        self.registry = PackageRegistry()
    
    def run_interactive(self):
        print("=" * 60)
        print("Bloatware Package Contribution Tool")
        print("=" * 60)
        print("\nThis tool helps you contribute new packages to the registry.")
        print("You can add, update, or remove packages easily.\n")
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a new package")
            print("2. Update an existing package")
            print("3. Remove a package")
            print("4. Search for packages")
            print("5. View all brands")
            print("6. View risk level guidelines")
            print("7. Exit")
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                self.add_package_interactive()
            elif choice == '2':
                self.update_package_interactive()
            elif choice == '3':
                self.remove_package_interactive()
            elif choice == '4':
                self.search_packages_interactive()
            elif choice == '5':
                self.view_brands()
            elif choice == '6':
                self.view_risk_guidelines()
            elif choice == '7':
                print("\nThank you for contributing!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_package_interactive(self):
        print("\n" + "=" * 60)
        print("Add New Package")
        print("=" * 60)
        
        brands = self.registry.get_brands()
        print("\nAvailable brands:")
        for i, brand in enumerate(brands, 1):
            brand_name = self.registry.get_brand_name(brand)
            print(f"{i}. {brand_name} ({brand})")
        
        print(f"{len(brands) + 1}. Add a new brand")
        
        try:
            brand_choice = int(input("\nSelect brand number: ").strip())
            if brand_choice == len(brands) + 1:
                brand = input("Enter new brand ID (lowercase, e.g., 'google'): ").strip().lower()
                if not brand:
                    print("Brand ID cannot be empty.")
                    return
            elif 1 <= brand_choice <= len(brands):
                brand = brands[brand_choice - 1]
            else:
                print("Invalid brand selection.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        categories = self.registry.get_brand_categories(brand)
        if categories:
            print(f"\nAvailable categories for {brand}:")
            cat_list = list(categories.keys())
            for i, cat_id in enumerate(cat_list, 1):
                cat_data = categories[cat_id]
                print(f"{i}. {cat_data.get('name', cat_id)} ({cat_id})")
            print(f"{len(cat_list) + 1}. Create a new category")
            
            try:
                cat_choice = int(input("\nSelect category number: ").strip())
                if cat_choice == len(cat_list) + 1:
                    category = input("Enter new category ID (lowercase with underscores, e.g., 'system_apps'): ").strip().lower()
                elif 1 <= cat_choice <= len(cat_list):
                    category = cat_list[cat_choice - 1]
                else:
                    print("Invalid category selection.")
                    return
            except ValueError:
                print("Invalid input.")
                return
        else:
            category = input("Enter category ID (lowercase with underscores, e.g., 'system_apps'): ").strip().lower()
        
        if not category:
            print("Category cannot be empty.")
            return
        
        print("\n" + "-" * 60)
        print("Package Information")
        print("-" * 60)
        
        package_name = input("Package name (e.g., com.example.app): ").strip()
        if not package_name:
            print("Package name cannot be empty.")
            return
        
        existing = self.registry.get_package_info(brand, package_name)
        if existing:
            print(f"\nWarning: Package '{package_name}' already exists for {brand}!")
            print(f"Current info: {existing}")
            if input("Do you want to update it instead? (y/n): ").strip().lower() != 'y':
                return
            self.update_package_interactive(brand, package_name)
            return
        
        description = input("Description (brief, user-friendly): ").strip()
        if not description:
            print("Description cannot be empty.")
            return
        
        print("\n" + "-" * 60)
        print("Risk Level Guidelines:")
        self.view_risk_guidelines()
        print("-" * 60)
        
        risk_levels = list(self.registry.get_all_risk_levels().keys())
        print("\nAvailable risk levels:")
        for i, risk in enumerate(risk_levels, 1):
            print(f"{i}. {risk}")
        
        try:
            risk_choice = int(input("\nSelect risk level number: ").strip())
            if 1 <= risk_choice <= len(risk_levels):
                risk = risk_levels[risk_choice - 1]
            else:
                print("Invalid risk level selection.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        package_data = {
            'name': package_name,
            'description': description,
            'risk': risk
        }
        
        print("\n" + "=" * 60)
        print("Package Summary:")
        print("=" * 60)
        print(f"Brand: {brand}")
        print(f"Category: {category}")
        print(f"Package: {package_name}")
        print(f"Description: {description}")
        print(f"Risk: {risk}")
        print("=" * 60)
        
        if input("\nConfirm addition? (y/n): ").strip().lower() == 'y':
            if self.registry.add_package(brand, category, package_data):
                self.registry.save_registry()
                print("\nPackage added successfully!")
                
                # Auto-regenerate brand files
                print(f"\nRegenerating files for {brand}...")
                try:
                    from scripts.generate_brand_files import generate_all_files_for_brand
                    if generate_all_files_for_brand(brand):
                        print("Brand files regenerated successfully!")
                except Exception as e:
                    print(f"Warning: Could not regenerate files: {e}")
                    print(f"Please run manually: python scripts/generate_brand_files.py --brand {brand}")
                
                print("\nNext steps:")
                print("1. Test the package removal on a device")
                print("2. Commit your changes")
                print("3. Create a pull request")
            else:
                print("\nFailed to add package.")
        else:
            print("\nAddition cancelled.")
    
    def update_package_interactive(self, brand: Optional[str] = None, package_name: Optional[str] = None):
        print("\n" + "=" * 60)
        print("Update Package")
        print("=" * 60)
        
        # Get brand if not provided
        if not brand:
            brands = self.registry.get_brands()
            print("\nAvailable brands:")
            for i, b in enumerate(brands, 1):
                brand_name = self.registry.get_brand_name(b)
                print(f"{i}. {brand_name} ({b})")
            
            try:
                brand_choice = int(input("\nSelect brand number: ").strip())
                if 1 <= brand_choice <= len(brands):
                    brand = brands[brand_choice - 1]
                else:
                    print("Invalid brand selection.")
                    return
            except ValueError:
                print("Invalid input.")
                return
        
        # Get package name if not provided
        if not package_name:
            package_name = input("\nEnter package name to update: ").strip()
        
        # Get current package info
        current = self.registry.get_package_info(brand, package_name)
        if not current:
            print(f"\nPackage '{package_name}' not found for {brand}.")
            return
        
        print("\nCurrent package information:")
        print(f"Name: {current.get('name')}")
        print(f"Description: {current.get('description')}")
        print(f"Risk: {current.get('risk')}")
        print(f"Category: {current.get('category')}")
        
        print("\n" + "-" * 60)
        print("Enter new values (press Enter to keep current value)")
        print("-" * 60)
        
        updates = {}
        
        new_desc = input(f"Description [{current.get('description')}]: ").strip()
        if new_desc:
            updates['description'] = new_desc
        
        # Show risk level options
        self.view_risk_guidelines()
        risk_levels = list(self.registry.get_all_risk_levels().keys())
        print("\nAvailable risk levels:")
        for i, risk in enumerate(risk_levels, 1):
            marker = "*" if risk == current.get('risk') else " "
            print(f"{i}. [{marker}] {risk}")
        
        new_risk_input = input(f"\nRisk level number [current: {current.get('risk')}]: ").strip()
        if new_risk_input:
            try:
                risk_choice = int(new_risk_input)
                if 1 <= risk_choice <= len(risk_levels):
                    updates['risk'] = risk_levels[risk_choice - 1]
            except ValueError:
                print("Invalid risk level selection.")
        
        if not updates:
            print("\nNo changes to make.")
            return
        
        print("\n" + "=" * 60)
        print("Changes Summary:")
        print("=" * 60)
        for key, value in updates.items():
            print(f"{key}: {current.get(key)} → {value}")
        print("=" * 60)
        
        if input("\nConfirm update? (y/n): ").strip().lower() == 'y':
            if self.registry.update_package(brand, package_name, updates):
                self.registry.save_registry()
                print("\nPackage updated successfully!")
                
                # Auto-regenerate brand files
                print(f"\nRegenerating files for {brand}...")
                try:
                    from scripts.generate_brand_files import generate_all_files_for_brand
                    if generate_all_files_for_brand(brand):
                        print("Brand files regenerated successfully!")
                except Exception as e:
                    print(f"Warning: Could not regenerate files: {e}")
                    print(f"Please run manually: python scripts/generate_brand_files.py --brand {brand}")
            else:
                print("\nFailed to update package.")
        else:
            print("\nUpdate cancelled.")
    
    def remove_package_interactive(self):
        print("\n" + "=" * 60)
        print("Remove Package")
        print("=" * 60)
        
        # Select brand
        brands = self.registry.get_brands()
        print("\nAvailable brands:")
        for i, brand in enumerate(brands, 1):
            brand_name = self.registry.get_brand_name(brand)
            print(f"{i}. {brand_name} ({brand})")
        
        try:
            brand_choice = int(input("\nSelect brand number: ").strip())
            if 1 <= brand_choice <= len(brands):
                brand = brands[brand_choice - 1]
            else:
                print("Invalid brand selection.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        package_name = input("\nEnter package name to remove: ").strip()
        
        # Check if package exists
        current = self.registry.get_package_info(brand, package_name)
        if not current:
            print(f"\nPackage '{package_name}' not found for {brand}.")
            return
        
        print("\nPackage to remove:")
        print(f"Name: {current.get('name')}")
        print(f"Description: {current.get('description')}")
        print(f"Risk: {current.get('risk')}")
        print(f"Category: {current.get('category')}")
        
        if input("\nConfirm removal? (type 'yes' to confirm): ").strip().lower() == 'yes':
            if self.registry.remove_package(brand, package_name):
                self.registry.save_registry()
                print("\nPackage removed successfully!")
                
                # Auto-regenerate brand files
                print(f"\nRegenerating files for {brand}...")
                try:
                    from scripts.generate_brand_files import generate_all_files_for_brand
                    if generate_all_files_for_brand(brand):
                        print("Brand files regenerated successfully!")
                except Exception as e:
                    print(f"Warning: Could not regenerate files: {e}")
                    print(f"Please run manually: python scripts/generate_brand_files.py --brand {brand}")
            else:
                print("\nFailed to remove package.")
        else:
            print("\nRemoval cancelled.")
    
    def search_packages_interactive(self):
        print("\n" + "=" * 60)
        print("Search Packages")
        print("=" * 60)
        
        query = input("\nEnter search query: ").strip()
        if not query:
            print("Search query cannot be empty.")
            return
        
        results = self.registry.search_packages(query)
        
        if not results:
            print(f"\nNo packages found matching '{query}'.")
            
            # Provide helpful suggestions
            print("\nSearch tips:")
            print("  - Search covers package names, descriptions, and categories")
            print("  - Try partial words (e.g., 'bix' for Bixby)")
            print("  - Try package name parts (e.g., 'spay', 'ecomm')")
            print("  - Try brand names (samsung, xiaomi, google, etc.)")
            
            # Show some popular search examples
            print("\nPopular search terms:")
            examples = ['google', 'bixby', 'pay', 'shop', 'maps', 'samsung', 'voice', 'email']
            print("  " + ", ".join(examples))
            
            return
        
        print(f"\nFound {len(results)} package(s):")
        print("-" * 60)
        
        for i, package in enumerate(results, 1):
            print(f"\n{i}. {package.get('name')}")
            print(f"   Brand: {package.get('brand')}")
            print(f"   Category: {package.get('category')}")
            print(f"   Description: {package.get('description')}")
            print(f"   Risk: {package.get('risk')}")
    
    def view_brands(self):
        print("\n" + "=" * 60)
        print("Supported Brands")
        print("=" * 60)
        
        brands = self.registry.get_brands()
        for brand in brands:
            brand_name = self.registry.get_brand_name(brand)
            categories = self.registry.get_brand_categories(brand)
            package_count = sum(len(cat.get('packages', [])) for cat in categories.values())
            
            print(f"\n{brand_name} ({brand})")
            print(f"  Categories: {len(categories)}")
            print(f"  Packages: {package_count}")
    
    def view_risk_guidelines(self):
        print("\n" + "=" * 60)
        print("Risk Level Guidelines")
        print("=" * 60)
        
        risk_levels = self.registry.get_all_risk_levels()
        for risk_id, risk_info in risk_levels.items():
            print(f"\n{risk_id.upper()}")
            print(f"  {risk_info.get('description')}")
            print(f"  Recommendation: {risk_info.get('recommendation')}")
    
    def add_package_cli(self, brand: str, category: str, package_name: str,
                       description: str, risk: str):
        package_data = {
            'name': package_name,
            'description': description,
            'risk': risk
        }
        
        if self.registry.add_package(brand, category, package_data):
            self.registry.save_registry()
            print(f"Successfully added {package_name} to {brand}/{category}")
            
            # Auto-regenerate brand files
            try:
                from scripts.generate_brand_files import generate_all_files_for_brand
                generate_all_files_for_brand(brand)
            except Exception as e:
                print(f"Warning: Could not regenerate files: {e}")
            
            return True
        else:
            print(f"Failed to add {package_name}")
            return False
    
    def remove_package_cli(self, brand: str, package_name: str):
        if self.registry.remove_package(brand, package_name):
            self.registry.save_registry()
            print(f"Successfully removed {package_name} from {brand}")
            
            # Auto-regenerate brand files
            try:
                from scripts.generate_brand_files import generate_all_files_for_brand
                generate_all_files_for_brand(brand)
            except Exception as e:
                print(f"Warning: Could not regenerate files: {e}")
            
            return True
        else:
            print(f"Failed to remove {package_name}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Bloatware Package Contribution Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (recommended)
  python contribute.py

  # Add a package via CLI
  python contribute.py add --brand samsung --category bixby \\
    --package com.samsung.android.bixby.test \\
    --description "Bixby Test Service" --risk safe

  # Remove a package via CLI
  python contribute.py remove --brand samsung --package com.samsung.android.bixby.test

  # Search for packages
  python contribute.py search --query "bixby"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new package')
    add_parser.add_argument('--brand', required=True, help='Brand ID (e.g., samsung)')
    add_parser.add_argument('--category', required=True, help='Category ID (e.g., bixby)')
    add_parser.add_argument('--package', required=True, help='Package name (e.g., com.example.app)')
    add_parser.add_argument('--description', required=True, help='Package description')
    add_parser.add_argument('--risk', required=True, choices=['safe', 'caution', 'dangerous', 'unknown'],
                          help='Risk level')
    
    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a package')
    remove_parser.add_argument('--brand', required=True, help='Brand ID')
    remove_parser.add_argument('--package', required=True, help='Package name to remove')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search for packages')
    search_parser.add_argument('--query', required=True, help='Search query')
    search_parser.add_argument('--brand', help='Limit search to specific brand')
    
    args = parser.parse_args()
    
    tool = ContributionTool()
    
    if args.command == 'add':
        tool.add_package_cli(args.brand, args.category, args.package,
                            args.description, args.risk)
    elif args.command == 'remove':
        tool.remove_package_cli(args.brand, args.package)
    elif args.command == 'search':
        results = tool.registry.search_packages(args.query, args.brand)
        if results:
            print(f"\nFound {len(results)} package(s):")
            for package in results:
                print(f"\n{package.get('name')}")
                print(f"  Brand: {package.get('brand')}")
                print(f"  Category: {package.get('category')}")
                print(f"  Description: {package.get('description')}")
                print(f"  Risk: {package.get('risk')}")
        else:
            print(f"\nNo packages found matching '{args.query}'")
    else:
        # Interactive mode
        tool.run_interactive()


if __name__ == "__main__":
    main()
