import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class XiaomiRemover(BloatwareRemover):
    """Xiaomi-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Xiaomi', 'Xiaomi/xiaomi_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Xiaomi bloatware configuration"""
        return {
            "categories": {
                "miui_apps": [
                    {"name": "com.mi.android.globalFileexplorer", "description": "Mi File Manager", "risk": "caution"},
                    {"name": "com.mi.android.globallauncher", "description": "Mi Launcher", "risk": "dangerous"},
                    {"name": "com.mi.android.globalpersonalassistant", "description": "Mi Assistant", "risk": "safe"},
                    {"name": "com.mi.globalTrendNews", "description": "Mi News", "risk": "safe"},
                    {"name": "com.mi.health", "description": "Mi Health", "risk": "safe"}
                ],
                "android_system": [
                    {"name": "com.android.bips", "description": "Built-in Print Service", "risk": "safe"},
                    {"name": "com.android.bookmarkprovider", "description": "Bookmark Provider", "risk": "safe"},
                    {"name": "com.android.browser", "description": "Android Browser", "risk": "caution"},
                    {"name": "com.android.calendar", "description": "Android Calendar", "risk": "caution"},
                    {"name": "com.android.chrome", "description": "Chrome Browser", "risk": "caution"},
                    {"name": "com.android.deskclock", "description": "Clock App", "risk": "caution"}
                ],
                "google_apps": [
                    {"name": "com.google.android.apps.docs", "description": "Google Docs", "risk": "safe"},
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.meetings", "description": "Google Meet", "risk": "safe"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "caution"}
                ],
                "system_services": [
                    {"name": "com.android.cellbroadcastreceiver", "description": "Emergency Alerts", "risk": "dangerous"},
                    {"name": "com.android.emergency", "description": "Emergency Info", "risk": "dangerous"},
                    {"name": "com.android.printspooler", "description": "Print Spooler", "risk": "safe"},
                    {"name": "com.google.android.gms", "description": "Google Play Services", "risk": "dangerous"}
                ],
                "misc_apps": [
                    {"name": "com.mfashiongallery.emag", "description": "Fashion Gallery", "risk": "safe"},
                    {"name": "com.android.dreams.basic", "description": "Basic Dreams", "risk": "safe"},
                    {"name": "com.android.dreams.phototable", "description": "Photo Screensaver", "risk": "safe"},
                    {"name": "com.android.wallpaper.livepicker", "description": "Live Wallpaper Picker", "risk": "safe"}
                ]
            }
        }

def main():
    remover = XiaomiRemover()
    
    print("Xiaomi Bloatware Removal Tool")
    print("1. Interactive removal (recommended)")
    print("2. Remove all configured packages")
    print("3. Exit")
    
    choice = input("Select option (1-3): ").strip()
    
    if choice == '1':
        remover.interactive_removal()
    elif choice == '2':
        if input("This will remove ALL configured packages. Continue? (y/n): ").lower() == 'y':
            remover.remove_packages()
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()