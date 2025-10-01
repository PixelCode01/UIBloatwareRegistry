#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from device_detector import DeviceDetector
from core.adb_utils import DEFAULT_TCPIP_PORT

try:
    from version import get_version
    VERSION = get_version()
except ImportError:
    VERSION = "1.0.0"

def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Android Bloatware Remover")
    parser.add_argument("--test", "-t", action="store_true", help="Run without executing adb commands")
    parser.add_argument("--wifi", action="store_true", help="Prompt for Wi-Fi ADB connection before detection")
    parser.add_argument("--wifi-endpoint", help="Connect to a Wi-Fi ADB endpoint (IP:port)")
    parser.add_argument("--wifi-pair", help="Pairing IP:port for Wi-Fi debugging")
    parser.add_argument("--wifi-code", help="Pairing code for Wi-Fi debugging")
    parser.add_argument("--enable-tcpip", action="store_true", help="Enable TCP/IP mode on the detected device")
    parser.add_argument(
        "--tcpip-port",
        type=int,
        default=DEFAULT_TCPIP_PORT,
        help=f"Port to use when enabling TCP/IP mode (default {DEFAULT_TCPIP_PORT})"
    )
    return parser.parse_args(argv)


def main():
    args = parse_args(sys.argv[1:])

    print("Android Bloatware Remover")
    print(f"Version {VERSION}")
    print("=" * 55)
    
    if args.test:
        print("Running in TEST MODE - no actual changes will be made")
        print("=" * 55)
    
    detector = DeviceDetector(test_mode=args.test)

    if args.wifi_endpoint:
        detector.connect_via_wifi(
            endpoint=args.wifi_endpoint,
            pairing_host=args.wifi_pair,
            pairing_code=args.wifi_code
        )
    elif args.wifi and not args.test:
        detector.connect_via_wifi()
    
    if not args.test:
        print("Detecting connected device...")
    device_info = detector.get_device_info()
    
    if not device_info:
        if not args.test:
            print("No device detected. Please ensure:")
            print("1. Device is connected via USB")
            print("2. USB debugging is enabled")
            print("3. ADB is installed and in PATH")
            print("\nTip: Use --test flag to run in test mode without a device")
        return
    
    detector.print_device_info()
    print()
    
    if args.enable_tcpip and not args.test:
        if detector.enable_tcpip_on_current_device(port=args.tcpip_port):
            print(f"TCP/IP debugging enabled on port {args.tcpip_port}.")
            print("You can now connect from the same network using the device's IP address.")

    remover = detector.get_supported_remover()
    
    if not remover:
        print("This device brand is not currently supported.")
        print("Supported brands: Samsung, Xiaomi, Oppo, Vivo, Realme, Tecno, OnePlus, Huawei, Honor, Motorola, Nothing")
        print("More brands will be added in future updates.")
        return
    
    if args.test:
        remover.test_mode = True
    
    brand_name = device_info.get('detected_brand', 'Unknown').title()
    mode_text = " (TEST MODE)" if args.test else ""
    print(f"Starting {brand_name} bloatware removal{mode_text}...")
    print()
    
    print("Available options:")
    print("1. Interactive removal (recommended for beginners)")
    print("2. List all apps and select what to remove")
    print("3. Manually remove by package or app name")
    print("4. Remove all configured packages (advanced users)")
    print("5. Exit")
    
    while True:
        choice = input("Select option (1-5): ").strip()
        
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
            remover.manual_package_removal()
            break
        elif choice == '4':
            warning_text = "TEST MODE: This will simulate removing" if args.test else "WARNING: This will remove"
            print(f"{warning_text} ALL configured bloatware packages.")
            if not args.test:
                print("This action cannot be easily undone.")
            
            confirm_text = "yes" if not args.test else "y"
            confirm = input(f"Are you sure you want to continue? (type '{confirm_text}' to confirm): ")
            
            if (args.test and confirm.lower() == 'y') or (not args.test and confirm.lower() == 'yes'):
                remover.remove_packages()
            else:
                print("Operation cancelled.")
            break
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()