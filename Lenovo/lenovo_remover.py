import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover


class LenovoRemover(BloatwareRemover):
    def __init__(self, test_mode: bool = False, use_registry: bool = True):
        super().__init__('Lenovo', 'Lenovo/lenovo_config.json', test_mode, use_registry=use_registry)

    def _get_default_packages(self):
        return {
            "categories": {
                "lenovo_suite": [
                    {"name": "com.lenovo.anyshare.gps", "description": "SHAREit file transfer", "risk": "safe"},
                    {"name": "com.lenovo.safecenter", "description": "Security Center", "risk": "caution"},
                    {"name": "com.lenovo.smartassistant", "description": "Smart Assistant voice app", "risk": "safe"},
                    {"name": "com.lenovo.lps", "description": "Lenovo payment services", "risk": "safe"},
                ],
                "preloads": [
                    {"name": "com.lenovo.email", "description": "Lenovo Email", "risk": "safe"},
                    {"name": "com.lenovo.calendar", "description": "Lenovo Calendar", "risk": "safe"},
                    {"name": "com.lenovo.fmradio", "description": "FM Radio", "risk": "safe"},
                ],
                "system_tools": [
                    {"name": "com.lenovo.ota", "description": "Lenovo OTA updater", "risk": "dangerous"},
                    {"name": "com.lenovo.lsf", "description": "Lenovo Service Framework", "risk": "dangerous"},
                ],
            }
        }


def main():
    remover = LenovoRemover()

    print("Lenovo Bloatware Removal Tool")
    print("1. Interactive removal (recommended)")
    print("2. List all apps and select what to remove")
    print("3. Manually remove by package or app name")
    print("4. Remove all configured packages")
    print("5. Exit")

    choice = input("Select option (1-5): ").strip()

    if choice == '1':
        remover.interactive_removal()
    elif choice == '2':
        print("This will list all installed applications on your device.")
        if input("Continue? (y/n): ").lower() == 'y':
            remover.list_all_apps_removal()
    elif choice == '3':
        remover.manual_package_removal()
    elif choice == '4':
        if input("This will remove ALL configured packages. Continue? (y/n): ").lower() == 'y':
            remover.remove_packages()
    elif choice == '5':
        print("Exiting...")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
