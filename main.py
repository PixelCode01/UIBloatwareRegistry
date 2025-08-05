#!/usr/bin/env python3

import sys
import os
from device_detector import DeviceDetector

def main():
    """Main application entry point"""
    print("UIBloatwareRegistry - Android Bloatware Removal Tool")
    print("=" * 55)
    
    detector = DeviceDetector()
    
    # Check device connection and detect brand
    print("Detecting connected device...")
    device_info = detector.get_device_info()
    
    if not device_info:
        print("No device detected. Please ensure:")
        print("1. Device is connected via USB")
        print("2. USB debugging is enabled")
        print("3. ADB is installed and in PATH")
        return
    
    detector.print_device_info()
    print()
    
    # Get appropriate remover
    remover = detector.get_supported_remover()
    
    if not remover:
        print("This device brand is not currently supported.")
        print("Supported brands: Samsung, Xiaomi")
        print("More brands will be added in future updates.")
        return
    
    # Run the remover
    print(f"Starting {device_info['detected_brand'].title()} bloatware removal...")
    print()
    
    print("Available options:")
    print("1. Interactive removal (recommended for beginners)")
    print("2. Remove all configured packages (advanced users)")
    print("3. Exit")
    
    while True:
        choice = input("Select option (1-3): ").strip()
        
        if choice == '1':
            remover.interactive_removal()
            break
        elif choice == '2':
            print("WARNING: This will remove ALL configured bloatware packages.")
            print("This action cannot be easily undone.")
            confirm = input("Are you sure you want to continue? (type 'yes' to confirm): ")
            
            if confirm.lower() == 'yes':
                remover.remove_packages()
            else:
                print("Operation cancelled.")
            break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()