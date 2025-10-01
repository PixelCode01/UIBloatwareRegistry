import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class XiaomiRemover(BloatwareRemover):
    def __init__(self, test_mode: bool = False, use_registry: bool = True):
        super().__init__('Xiaomi', 'Xiaomi/xiaomi_config.json', test_mode, use_registry=use_registry)
    
    def _get_default_packages(self):
        return {
            "categories": {
                "miui_apps": [
                    {"name": "com.mi.android.globalFileexplorer", "description": "Mi File Manager", "risk": "caution"},
                    {"name": "com.mi.android.globallauncher", "description": "Mi Launcher", "risk": "dangerous"},
                    {"name": "com.mi.android.globalpersonalassistant", "description": "Mi Assistant", "risk": "safe"},
                    {"name": "com.mi.globalTrendNews", "description": "Mi News", "risk": "safe"},
                    {"name": "com.mi.health", "description": "Mi Health", "risk": "safe"},
                ],
                "google_apps": [
                    {"name": "com.google.android.apps.docs", "description": "Google Docs", "risk": "safe"},
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.meetings", "description": "Google Meet", "risk": "safe"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "caution"},
                ],
                "test_category": [
                    {"name": "com.test.endtoend", "description": "End to End Test", "risk": "safe"},
                ],
            }
        }

def main():
    remover = XiaomiRemover()
    
    print("Xiaomi Bloatware Removal Tool")
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