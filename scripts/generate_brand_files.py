#!/usr/bin/env python3

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.package_registry import PackageRegistry


def generate_python_remover(brand: str, brand_data: Dict, packages_by_category: Dict) -> str:
    brand_name = brand_data.get('name', brand.title())
    brand_lower = brand.lower()
    brand_class = ''.join(word.title() for word in brand_lower.split('_'))
    
    lines = []
    lines.append("import sys")
    lines.append("import os")
    lines.append("sys.path.append(os.path.join(os.path.dirname(__file__), '..'))")
    lines.append("")
    lines.append("from core.bloatware_remover import BloatwareRemover")
    lines.append("")
    lines.append(f"class {brand_class}Remover(BloatwareRemover):")
    lines.append(f'    """{brand_name}-specific bloatware remover"""')
    lines.append("    ")
    lines.append("    def __init__(self, test_mode: bool = False, use_registry: bool = True):")
    lines.append(f"        super().__init__('{brand_name}', '{brand.title()}/{brand_lower}_config.json', test_mode, use_registry=use_registry)")
    lines.append("    ")
    lines.append("    def _get_default_packages(self):")
    lines.append(f'        """{brand_name} bloatware configuration (fallback if registry unavailable)"""')
    lines.append("        return {")
    lines.append('            "categories": {')
    
    # Add all categories and packages
    for cat_id, packages in packages_by_category.items():
        lines.append(f'                "{cat_id}": [')
        for pkg in packages:
            lines.append(f'                    {{"name": "{pkg["name"]}", "description": "{pkg["description"]}", "risk": "{pkg["risk"]}"}},')
        lines.append("                ],")
    
    lines.append("            }")
    lines.append("        }")
    lines.append("")
    lines.append("def main():")
    lines.append(f"    remover = {brand_class}Remover()")
    lines.append("    ")
    lines.append(f'    print("{brand_name} Bloatware Removal Tool")')
    lines.append('    print("1. Interactive removal (recommended)")')
    lines.append('    print("2. List all apps and select what to remove")')
    lines.append('    print("3. Manually remove by package or app name")')
    lines.append('    print("4. Remove all configured packages")')
    lines.append('    print("5. Exit")')
    lines.append("    ")
    lines.append('    choice = input("Select option (1-5): ").strip()')
    lines.append("    ")
    lines.append("    if choice == '1':")
    lines.append("        remover.interactive_removal()")
    lines.append("    elif choice == '2':")
    lines.append('        print("This will list all installed applications on your device.")')
    lines.append('        if input("Continue? (y/n): ").lower() == \'y\':')
    lines.append("            remover.list_all_apps_removal()")
    lines.append("    elif choice == '3':")
    lines.append("        remover.manual_package_removal()")
    lines.append("    elif choice == '4':")
    lines.append('        if input("This will remove ALL configured packages. Continue? (y/n): ").lower() == \'y\':')
    lines.append("            remover.remove_packages()")
    lines.append("    elif choice == '5':")
    lines.append('        print("Exiting...")')
    lines.append("    else:")
    lines.append('        print("Invalid choice")')
    lines.append("")
    lines.append('if __name__ == "__main__":')
    lines.append("    main()")
    
    return "\n".join(lines)


def generate_shell_script(brand: str, brand_data: Dict, packages_by_category: Dict) -> str:
    brand_name = brand_data.get('name', brand.title())
    
    # Group packages by risk level
    safe_packages = []
    caution_packages = []
    dangerous_packages = []
    
    for cat_id, packages in packages_by_category.items():
        for pkg in packages:
            entry = f'{pkg["name"]}:{pkg["description"]}'
            risk = pkg["risk"]
            if risk == "safe":
                safe_packages.append(entry)
            elif risk == "caution":
                caution_packages.append(entry)
            elif risk == "dangerous":
                dangerous_packages.append(entry)
    
    lines = []
    lines.append("#!/system/bin/sh")
    lines.append("# Auto-generated from packages_registry.json")
    lines.append("")
    lines.append("RED='\\033[0;31m'")
    lines.append("GREEN='\\033[0;32m'")
    lines.append("YELLOW='\\033[1;33m'")
    lines.append("BLUE='\\033[0;34m'")
    lines.append("NC='\\033[0m'")
    lines.append("")
    lines.append("print_colored() {")
    lines.append("    local color=$1")
    lines.append("    local text=$2")
    lines.append('    printf "${color}${text}${NC}\\n"')
    lines.append("}")
    lines.append("")
    lines.append("print_header() {")
    lines.append('    echo "=================================================="')
    lines.append(f'    print_colored $BLUE "{brand_name} Bloatware Remover for Shizuku"')
    lines.append('    print_colored $BLUE "Version 1.0"')
    lines.append('    echo "=================================================="')
    lines.append('    echo ""')
    lines.append('    print_colored $YELLOW "WARNING: This script will remove applications from your device."')
    lines.append('    print_colored $YELLOW "Always create a backup before proceeding."')
    lines.append('    echo ""')
    lines.append("}")
    lines.append("")
    lines.append('SAFE_PACKAGES="')
    for pkg in safe_packages:
        lines.append(pkg)
    lines.append('"')
    lines.append("")
    lines.append('CAUTION_PACKAGES="')
    for pkg in caution_packages:
        lines.append(pkg)
    lines.append('"')
    lines.append("")
    lines.append('DANGEROUS_PACKAGES="')
    for pkg in dangerous_packages:
        lines.append(pkg)
    lines.append('"')
    lines.append("")
    lines.append("remove_packages() {")
    lines.append("    local packages=\"$1\"")
    lines.append("    local category=\"$2\"")
    lines.append('    print_colored $BLUE "Removing $category packages..."')
    lines.append('    echo "$packages" | while IFS=\':\'  read -r package desc; do')
    lines.append('        if [ -n "$package" ] && [ "$package" != "" ]; then')
    lines.append('            echo "Removing: $desc ($package)"')
    lines.append('            pm uninstall --user 0 "$package" 2>/dev/null')
    lines.append('            if [ $? -eq 0 ]; then')
    lines.append('                print_colored $GREEN "Uninstalled: $package"')
    lines.append('            else')
    lines.append('                pm disable-user --user 0 "$package" 2>/dev/null')
    lines.append('                if [ $? -eq 0 ]; then')
    lines.append('                    print_colored $YELLOW "Disabled: $package"')
    lines.append('                else')
    lines.append('                    print_colored $RED "Failed: $package"')
    lines.append('                fi')
    lines.append('            fi')
    lines.append('        fi')
    lines.append('    done')
    lines.append('    echo ""')
    lines.append("}")
    lines.append("")
    lines.append("interactive_removal() {")
    lines.append('    print_colored $BLUE "=== INTERACTIVE PACKAGE REMOVAL ==="')
    lines.append('    echo ""')
    lines.append('    read -p "Remove SAFE packages? (y/n): " choice')
    lines.append('    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then')
    lines.append('        remove_packages "$SAFE_PACKAGES" "SAFE"')
    lines.append('    fi')
    lines.append('    read -p "Remove CAUTION packages? (y/n): " choice')
    lines.append('    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then')
    lines.append('        remove_packages "$CAUTION_PACKAGES" "CAUTION"')
    lines.append('    fi')
    lines.append('    read -p "Remove DANGEROUS packages? (y/n): " choice')
    lines.append('    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then')
    lines.append('        print_colored $RED "WARNING: This may break device functionality!"')
    lines.append('        read -p "Are you sure? (yes/no): " confirm')
    lines.append('        if [ "$confirm" = "yes" ]; then')
    lines.append('            remove_packages "$DANGEROUS_PACKAGES" "DANGEROUS"')
    lines.append('        fi')
    lines.append('    fi')
    lines.append("}")
    lines.append("")
    lines.append("main() {")
    lines.append("    print_header")
    lines.append("    interactive_removal")
    lines.append("}")
    lines.append("")
    lines.append("main")
    
    return "\n".join(lines)


def generate_markdown(brand: str, brand_data: Dict, packages_by_category: Dict, categories: Dict) -> str:
    brand_name = brand_data.get('name', brand.title())
    
    lines = []
    lines.append(f"# {brand_name} Bloatware Package List")
    lines.append("")
    lines.append(f"This document contains a comprehensive list of bloatware packages found on {brand_name} devices.")
    lines.append("Each package is categorized by risk level and includes descriptions to help you make informed removal decisions.")
    lines.append("")
    lines.append("**Auto-generated from packages_registry.json**")
    lines.append("")
    lines.append("## Risk Levels")
    lines.append("- **SAFE**: Can be removed without affecting core functionality")
    lines.append("- **CAUTION**: May affect some features, remove with care")
    lines.append("- **DANGEROUS**: Critical system components, removal may cause instability")
    lines.append("")
    
    # Group by category
    for cat_id, cat_data in categories.items():
        if cat_id not in packages_by_category or not packages_by_category[cat_id]:
            continue
            
        cat_name = cat_data.get('name', cat_id.replace('_', ' ').title())
        cat_desc = cat_data.get('description', '')
        
        lines.append(f"## {cat_name}")
        lines.append("")
        if cat_desc:
            lines.append(f"*{cat_desc}*")
            lines.append("")
        
        # Group packages by risk within category
        packages = packages_by_category[cat_id]
        safe = [p for p in packages if p['risk'] == 'safe']
        caution = [p for p in packages if p['risk'] == 'caution']
        dangerous = [p for p in packages if p['risk'] == 'dangerous']
        
        if safe:
            lines.append("### Safe to Remove")
            for pkg in safe:
                lines.append(f"- `{pkg['name']}` - {pkg['description']}")
            lines.append("")
        
        if caution:
            lines.append("### Use Caution")
            for pkg in caution:
                lines.append(f"- `{pkg['name']}` - {pkg['description']}")
            lines.append("")
        
        if dangerous:
            lines.append("### Dangerous to Remove")
            for pkg in dangerous:
                lines.append(f"- `{pkg['name']}` - {pkg['description']}")
            lines.append("")
    
    lines.append("## Removal Notes")
    lines.append("")
    lines.append("- Always create a backup before removing any packages")
    lines.append("- Test removals on a non-primary device first")
    lines.append("- Some apps may reinstall after system updates")
    lines.append("- Factory reset will restore all removed applications")
    lines.append("- Use the interactive removal mode for safer operation")
    lines.append("")
    
    return "\n".join(lines)


def generate_all_files_for_brand(brand: str, output_dir: Path = None):
    if output_dir is None:
        output_dir = Path(__file__).parent.parent
    
    registry = PackageRegistry()
    
    # Get brand data
    brand_data = registry.registry_data.get('brands', {}).get(brand.lower(), {})
    if not brand_data:
        print(f"Brand '{brand}' not found in registry")
        return False
    
    categories = brand_data.get('categories', {})
    packages_by_category = {}
    
    for cat_id, cat_data in categories.items():
        packages_by_category[cat_id] = cat_data.get('packages', [])
    
    # Create brand directory
    brand_dir = output_dir / brand.title()
    brand_dir.mkdir(parents=True, exist_ok=True)
    
    brand_lower = brand.lower()
    
    # Generate Python file
    print(f"Generating {brand.title()}/{brand_lower}_remover.py...")
    python_content = generate_python_remover(brand, brand_data, packages_by_category)
    python_file = brand_dir / f"{brand_lower}_remover.py"
    python_file.write_text(python_content, encoding='utf-8')
    
    # Generate shell script
    print(f"Generating {brand.title()}/{brand_lower}_remover.sh...")
    shell_content = generate_shell_script(brand, brand_data, packages_by_category)
    shell_file = brand_dir / f"{brand_lower}_remover.sh"
    shell_file.write_text(shell_content, encoding='utf-8')
    
    # Generate markdown
    print(f"Generating {brand.title()}/{brand_lower}-bloatware-list.md...")
    markdown_content = generate_markdown(brand, brand_data, packages_by_category, categories)
    markdown_file = brand_dir / f"{brand_lower}-bloatware-list.md"
    markdown_file.write_text(markdown_content, encoding='utf-8')
    
    print(f"Successfully generated files for {brand_data.get('name')}")
    return True


def generate_all_brands(output_dir: Path = None):
    if output_dir is None:
        output_dir = Path(__file__).parent.parent
    
    registry = PackageRegistry()
    brands = registry.get_brands()
    
    print(f"Found {len(brands)} brands in registry")
    print("=" * 60)
    
    success_count = 0
    for brand in brands:
        if generate_all_files_for_brand(brand, output_dir):
            success_count += 1
        print()
    
    print("=" * 60)
    print(f"Generated files for {success_count}/{len(brands)} brands")


def main():
    parser = argparse.ArgumentParser(
        description="Generate brand files from packages_registry.json"
    )
    parser.add_argument('--all', action='store_true',
                       help='Generate files for all brands')
    parser.add_argument('--brand', type=str,
                       help='Generate files for specific brand')
    parser.add_argument('--output', type=Path,
                       help='Output directory (default: project root)')
    
    args = parser.parse_args()
    
    if args.all:
        generate_all_brands(args.output)
    elif args.brand:
        generate_all_files_for_brand(args.brand, args.output)
    else:
        parser.print_help()
        print("\nExample usage:")
        print("  python generate_brand_files.py --all")
        print("  python generate_brand_files.py --brand oppo")


if __name__ == '__main__':
    main()
