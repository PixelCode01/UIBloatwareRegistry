import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover


class AsusRemover(BloatwareRemover):
    def __init__(self, test_mode: bool = False, use_registry: bool = True):
        super().__init__('Asus', 'Asus/asus_config.json', test_mode, use_registry=use_registry)

    def _get_default_packages(self):
        return {
            "categories": {
                "zen_ui": [
                    {"name": "com.asus.launcher", "description": "ZenUI launcher", "risk": "caution"},
                    {"name": "com.asus.mobilemanager", "description": "Mobile Manager optimizer", "risk": "caution"},
                    {"name": "com.asus.filemanager", "description": "Asus File Manager", "risk": "safe"},
                    {"name": "com.asus.weather", "description": "Asus Weather widgets", "risk": "safe"},
                ],
                "gaming": [
                    {"name": "com.asus.gamecenter", "description": "ROG Game Center hub", "risk": "safe"},
                    {"name": "com.asus.gamingfan", "description": "ROG gaming fan control", "risk": "dangerous"},
                    {"name": "com.asus.rogtheme", "description": "ROG theming pack", "risk": "safe"},
                ],
                "preloads": [
                    {"name": "com.facebook.katana", "description": "Facebook client", "risk": "safe"},
                    {"name": "com.instagram.android", "description": "Instagram client", "risk": "safe"},
                    {"name": "com.netflix.partner.activation", "description": "Netflix activation", "risk": "caution"},
                ],
            }
        }


def main():
    remover = AsusRemover()

    print("Asus Bloatware Removal Tool")
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
