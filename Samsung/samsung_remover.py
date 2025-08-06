import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class SamsungRemover(BloatwareRemover):
    """Samsung-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Samsung', 'Samsung/samsung_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Samsung bloatware configuration"""
        return {
            "categories": {
                "bixby": [
                    {"name": "com.samsung.android.bixby.wakeup", "description": "Bixby wake up service", "risk": "safe"},
                    {"name": "com.samsung.android.app.spage", "description": "Bixby homepage launcher", "risk": "safe"},
                    {"name": "com.samsung.android.app.routines", "description": "Bixby Routines", "risk": "safe"},
                    {"name": "com.samsung.android.bixby.service", "description": "Bixby features", "risk": "safe"},
                    {"name": "com.samsung.android.visionintelligence", "description": "Bixby Vision", "risk": "safe"},
                    {"name": "com.samsung.android.bixby.agent", "description": "Bixby Voice", "risk": "safe"}
                ],
                "samsung_apps": [
                    {"name": "com.samsung.android.messaging", "description": "Samsung Messages", "risk": "caution"},
                    {"name": "com.sec.android.app.sbrowser", "description": "Samsung Internet", "risk": "caution"},
                    {"name": "com.samsung.android.email.provider", "description": "Samsung Email", "risk": "safe"},
                    {"name": "com.samsung.android.calendar", "description": "Samsung Calendar", "risk": "caution"},
                    {"name": "com.sec.android.app.voicenote", "description": "Voice Recorder", "risk": "safe"},
                    {"name": "com.sec.android.app.popupcalculator", "description": "Samsung Calculator", "risk": "caution"}
                ],
                "samsung_services": [
                    {"name": "com.samsung.android.scloud", "description": "Samsung Cloud", "risk": "safe"},
                    {"name": "com.samsung.android.oneconnect", "description": "SmartThings", "risk": "safe"},
                    {"name": "com.samsung.android.voc", "description": "Samsung Members", "risk": "safe"},
                    {"name": "com.samsung.ecomm.global", "description": "Samsung Shop", "risk": "safe"},
                    {"name": "com.samsung.android.spay", "description": "Samsung Pay", "risk": "dangerous"},
                    {"name": "com.samsung.android.samsungpass", "description": "Samsung Pass", "risk": "caution"}
                ],
                "carrier_bloat": [
                    {"name": "com.vzw.hss.myverizon", "description": "My Verizon", "risk": "safe"},
                    {"name": "com.att.myWireless", "description": "myAT&T", "risk": "safe"},
                    {"name": "com.samsung.vvm", "description": "Visual Voicemail", "risk": "caution"}
                ],
                "google_apps": [
                    {"name": "com.google.android.apps.docs", "description": "Google Docs", "risk": "safe"},
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "caution"}
                ]
            }
        }

def main():
    remover = SamsungRemover()
    
    print("Samsung Bloatware Removal Tool")
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