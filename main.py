#!/usr/bin/env python3
import sys
import os
from device_detector import DeviceDetector

try:
    from version import get_version
    VERSION = get_version()
except ImportError:
    VERSION = "1.0.0"

def main():
    """Main application entry point"""
    print("Android Bloatware Remover")
    print(f"Version {VERSION}")
    print("=" * 55)
    
    # Check for test mode argument
    test_mode = '--test' in sys.argv or '-t' in sys.argv
    
    if test_mode:
        print("Running in TEST MODE - no actual changes will be made")
        print("=" * 55)
    
    detector = DeviceDetector(test_mode=test_mode)
    
    if not test_mode:
        print("Detecting connected device...")
    device_info = detector.get_device_info()
    
    if not device_info:
        if not test_mode:
            print("No device detected. Please ensure:")
            print("1. Device is connected via USB")
            print("2. USB debugging is enabled")
            print("3. ADB is installed and in PATH")
            print("\nTip: Use --test flag to run in test mode without a device")
        return
    
    detector.print_device_info()
    print()
    
    # Get appropriate remover
    remover = detector.get_supported_remover()
    
    if not remover:
        print("This device brand is not currently supported.")
        print("Supported brands: Samsung, Xiaomi, Oppo, Vivo, Realme, Tecno, OnePlus, Huawei, Honor, Motorola, Nothing")
        print("More brands will be added in future updates.")
        return
    
    # Set test mode on remover if needed
    if test_mode:
        remover.test_mode = True
    
    # Run the remover
    brand_name = device_info.get('detected_brand', 'Unknown').title()
    mode_text = " (TEST MODE)" if test_mode else ""
    print(f"Starting {brand_name} bloatware removal{mode_text}...")
    print()
    
    print("Available options:")
    print("1. Interactive removal (recommended for beginners)")
    print("2. List all apps and select what to remove")
    print("3. Remove all configured packages (advanced users)")
    print("4. Exit")
    
    while True:
        choice = input("Select option (1-4): ").strip()
        
        if choice == '1':
            remover.interactive_removal()
            break
        elif choice == '2':
            print("This will list all installed applications on your device.")
            print("You can then select which ones to remove.")
            if input("Continue? (y/n): ").lower().strip() == 'y':
                remover.list_all_apps_removal()
            break
        elif choice == '3':
            warning_text = "TEST MODE: This will simulate removing" if test_mode else "WARNING: This will remove"
            print(f"{warning_text} ALL configured bloatware packages.")
            if not test_mode:
                print("This action cannot be easily undone.")
            
            confirm_text = "yes" if not test_mode else "y"
            confirm = input(f"Are you sure you want to continue? (type '{confirm_text}' to confirm): ")
            
            if (test_mode and confirm.lower() == 'y') or (not test_mode and confirm.lower() == 'yes'):
                remover.remove_packages()
            else:
                print("Operation cancelled.")
            break
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()