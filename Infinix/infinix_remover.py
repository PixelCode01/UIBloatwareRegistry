import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover


class InfinixRemover(BloatwareRemover):
    def __init__(self, test_mode: bool = False, use_registry: bool = True):
        super().__init__('Infinix', 'Infinix/infinix_config.json', test_mode, use_registry=use_registry)

    def _get_default_packages(self):
        return {
            "categories": {
                "xos_suite": [
                    {"name": "com.transsion.xclub", "description": "XClub community", "risk": "safe"},
                    {"name": "com.transsion.smartpanel", "description": "Smart panel overlay", "risk": "caution"},
                    {"name": "com.transsion.aura.gameassist", "description": "Game mode assistant", "risk": "safe"},
                    {"name": "com.transsion.aia", "description": "AIA voice assistant", "risk": "safe"},
                ],
                "preloads": [
                    {"name": "com.infinix.xshare", "description": "XShare transfer", "risk": "safe"},
                    {"name": "com.infinix.xclub", "description": "Infinix forum", "risk": "safe"},
                    {"name": "com.transsion.phoenix", "description": "Phoenix browser", "risk": "caution"},
                ],
                "ads": [
                    {"name": "com.transsion.aha.games", "description": "AHA Games hub", "risk": "safe"},
                    {"name": "com.transsion.xboom", "description": "Boomplay music", "risk": "safe"},
                    {"name": "com.transsion.calculator", "description": "Palm Calculator", "risk": "safe"},
                ],
            }
        }


def main():
    remover = InfinixRemover()

    print("Infinix Bloatware Removal Tool")
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
