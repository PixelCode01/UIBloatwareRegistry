import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class RealmeRemover(BloatwareRemover):
    """Realme-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Realme', 'Realme/realme_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Realme bloatware configuration"""
        return {
            "categories": {
                "android_safe": [
                    {"name": "com.android.bips", "description": "Built-in Print Service", "risk": "safe"},
                    {"name": "com.android.bookmarkprovider", "description": "Browser bookmark storage", "risk": "safe"},
                    {"name": "com.android.calllogbackup", "description": "Call log backup service", "risk": "safe"},
                    {"name": "com.android.printspooler", "description": "Mobile printing service", "risk": "safe"},
                    {"name": "com.android.providers.partnerbookmarks", "description": "Chrome bookmarks", "risk": "safe"},
                    {"name": "com.android.sharedstoragebackup", "description": "Shared storage backup", "risk": "safe"},
                    {"name": "com.android.statementservice", "description": "Digital asset links", "risk": "safe"},
                    {"name": "com.android.wallpaperbackup", "description": "Wallpaper backup service", "risk": "safe"}
                ],
                "android_caution": [
                    {"name": "com.android.chrome", "description": "Google Chrome browser", "risk": "caution"},
                    {"name": "com.android.mms", "description": "SMS/MMS messaging", "risk": "caution"},
                    {"name": "com.android.mms.service", "description": "SMS/MMS service", "risk": "caution"}
                ],
                "android_dangerous": [
                    {"name": "com.android.cellbroadcastreceiver", "description": "Emergency alerts system", "risk": "dangerous"},
                    {"name": "com.android.cellbroadcastreceiver.overlay.common", "description": "Emergency alerts overlay", "risk": "dangerous"},
                    {"name": "com.android.stk", "description": "SIM Toolkit (required for carrier services)", "risk": "dangerous"}
                ],
                "realme_safe": [
                    {"name": "com.caf.fmradio", "description": "FM Radio application", "risk": "safe"},
                    {"name": "com.coloros.activation", "description": "Device activation service", "risk": "safe"},
                    {"name": "com.coloros.avastofferwall", "description": "Avast promotional content", "risk": "safe"},
                    {"name": "com.coloros.athena", "description": "System optimization service", "risk": "safe"},
                    {"name": "com.coloros.bootreg", "description": "Boot registration service", "risk": "safe"},
                    {"name": "com.coloros.childrenspace", "description": "Kids Space mode", "risk": "safe"},
                    {"name": "com.coloros.compass2", "description": "Compass application", "risk": "safe"},
                    {"name": "com.coloros.focusmode", "description": "Focus Mode for productivity", "risk": "safe"},
                    {"name": "com.coloros.gamespace", "description": "Game Space", "risk": "safe"},
                    {"name": "com.coloros.gamespaceui", "description": "Game Space UI", "risk": "safe"},
                    {"name": "com.coloros.healthcheck", "description": "Device health checker", "risk": "safe"},
                    {"name": "com.coloros.ocrscanner", "description": "OCR text scanner", "risk": "safe"},
                    {"name": "com.coloros.oppomultiapp", "description": "App cloning feature", "risk": "safe"},
                    {"name": "com.coloros.oshare", "description": "Oppo Share file sharing", "risk": "safe"},
                    {"name": "com.coloros.phonenoareainquire", "description": "Phone number area inquiry", "risk": "safe"},
                    {"name": "com.coloros.pictorial", "description": "Pictorial wallpapers", "risk": "safe"},
                    {"name": "com.coloros.resmonitor", "description": "Resource monitor", "risk": "safe"},
                    {"name": "com.coloros.safesdkproxy", "description": "Phone Cleaner (contains tracking)", "risk": "safe"},
                    {"name": "com.coloros.sauhelper", "description": "SAU helper service", "risk": "safe"},
                    {"name": "com.coloros.sceneservice", "description": "Scene recognition service", "risk": "safe"},
                    {"name": "com.coloros.screenrecorder", "description": "Screen recording app", "risk": "safe"},
                    {"name": "com.coloros.smartdrive", "description": "Smart drive service", "risk": "safe"},
                    {"name": "com.coloros.speechassist", "description": "Voice assistant", "risk": "safe"},
                    {"name": "com.coloros.translate.engine", "description": "Translation service", "risk": "safe"},
                    {"name": "com.coloros.video", "description": "Video player", "risk": "safe"},
                    {"name": "com.coloros.wallet", "description": "Digital wallet", "risk": "safe"},
                    {"name": "com.coloros.widget.smallweather", "description": "Weather widget", "risk": "safe"},
                    {"name": "com.coloros.wifibackuprestore", "description": "WiFi backup service", "risk": "safe"}
                ],
                "realme_caution": [
                    {"name": "com.coloros.appmanager", "description": "App Manager", "risk": "caution"},
                    {"name": "com.coloros.assistantscreen", "description": "Smart Assistant", "risk": "caution"},
                    {"name": "com.coloros.backuprestore", "description": "Clone Phone backup", "risk": "caution"},
                    {"name": "com.coloros.calculator", "description": "Calculator app", "risk": "caution"},
                    {"name": "com.coloros.encryption", "description": "Encryption service", "risk": "caution"},
                    {"name": "com.coloros.filemanager", "description": "File Manager", "risk": "caution"},
                    {"name": "com.coloros.floatassistant", "description": "Floating assistant", "risk": "caution"},
                    {"name": "com.coloros.phonemanager", "description": "Phone Manager", "risk": "caution"},
                    {"name": "com.coloros.securepay", "description": "Secure payment service", "risk": "caution"},
                    {"name": "com.coloros.soundrecorder", "description": "Voice recorder", "risk": "caution"}
                ],
                "facebook_bloat": [
                    {"name": "com.facebook.appmanager", "description": "Facebook App Manager", "risk": "safe"},
                    {"name": "com.facebook.services", "description": "Facebook Services", "risk": "safe"},
                    {"name": "com.facebook.system", "description": "Facebook System Service", "risk": "safe"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.docs", "description": "Google Drive", "risk": "safe"},
                    {"name": "com.google.android.apps.magazines", "description": "Google News", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.restore", "description": "Google Restore", "risk": "safe"},
                    {"name": "com.google.android.apps.tachyon", "description": "Google Duo", "risk": "safe"},
                    {"name": "com.google.android.apps.wellbeing", "description": "Digital Wellbeing", "risk": "safe"},
                    {"name": "com.google.android.apps.youtube.music", "description": "YouTube Music", "risk": "safe"},
                    {"name": "com.google.android.feedback", "description": "Google Feedback", "risk": "safe"},
                    {"name": "com.google.android.keep", "description": "Google Keep", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies & TV", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"},
                    {"name": "com.google.ar.core", "description": "Google Play Services for AR", "risk": "safe"}
                ],
                "google_caution": [
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.calendar", "description": "Google Calendar", "risk": "caution"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.googlequicksearchbox", "description": "Google Search Widget", "risk": "caution"},
                    {"name": "com.google.android.inputmethod.latin", "description": "Gboard keyboard", "risk": "caution"}
                ],
                "google_dangerous": [
                    {"name": "com.google.android.marvin.talkback", "description": "Accessibility service", "risk": "dangerous"}
                ]
            }
        }

def main():
    remover = RealmeRemover()
    
    print("Realme Bloatware Removal Tool")
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