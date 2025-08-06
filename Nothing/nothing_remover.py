import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class NothingRemover(BloatwareRemover):
    """Nothing-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Nothing', 'Nothing/nothing_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Nothing bloatware configuration"""
        return {
            "categories": {
                "nothing_safe": [
                    {"name": "com.nothing.camera", "description": "Nothing Camera (if using alternative)", "risk": "safe"},
                    {"name": "com.nothing.gallery", "description": "Nothing Gallery (if using alternative)", "risk": "safe"},
                    {"name": "com.nothing.launcher", "description": "Nothing Launcher (if using alternative)", "risk": "safe"},
                    {"name": "com.nothing.recorder", "description": "Nothing Recorder", "risk": "safe"},
                    {"name": "com.nothing.weather", "description": "Nothing Weather", "risk": "safe"},
                    {"name": "com.nothing.widgets", "description": "Nothing Widgets", "risk": "safe"},
                    {"name": "com.nothing.wallpapers", "description": "Nothing Wallpapers", "risk": "safe"},
                    {"name": "com.nothing.icons", "description": "Nothing Icon Pack", "risk": "safe"},
                    {"name": "com.nothing.sounds", "description": "Nothing Sounds", "risk": "safe"},
                    {"name": "com.nothing.ringtones", "description": "Nothing Ringtones", "risk": "safe"},
                    {"name": "com.nothing.customization", "description": "Nothing Customization", "risk": "safe"},
                    {"name": "com.nothing.themes", "description": "Nothing Themes", "risk": "safe"},
                    {"name": "com.nothing.fonts", "description": "Nothing Fonts", "risk": "safe"},
                    {"name": "com.nothing.animations", "description": "Nothing Animations", "risk": "safe"},
                    {"name": "com.nothing.bootanimation", "description": "Boot Animation", "risk": "safe"},
                    {"name": "com.nothing.lockscreen", "description": "Lock Screen Customization", "risk": "safe"}
                ],
                "nothing_caution": [
                    {"name": "com.nothing.smartcenter", "description": "Nothing Smart Center", "risk": "caution"},
                    {"name": "com.nothing.glyph", "description": "Glyph Interface", "risk": "caution"},
                    {"name": "com.nothing.settings", "description": "Nothing Settings Extensions", "risk": "caution"},
                    {"name": "com.nothing.assistant", "description": "Nothing Assistant", "risk": "caution"},
                    {"name": "com.nothing.optimization", "description": "System Optimization", "risk": "caution"},
                    {"name": "com.nothing.security", "description": "Nothing Security", "risk": "caution"}
                ],
                "nothing_dangerous": [
                    {"name": "com.nothing.framework", "description": "Nothing Framework", "risk": "dangerous"},
                    {"name": "com.nothing.systemui", "description": "Nothing System UI", "risk": "dangerous"},
                    {"name": "com.nothing.core", "description": "Nothing Core Services", "risk": "dangerous"},
                    {"name": "com.nothing.system", "description": "Nothing System Services", "risk": "dangerous"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.docs", "description": "Google Drive", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.youtube.music", "description": "YouTube Music", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"},
                    {"name": "com.google.android.keep", "description": "Google Keep", "risk": "safe"},
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"},
                    {"name": "com.google.android.apps.wellbeing", "description": "Digital Wellbeing", "risk": "safe"}
                ],
                "google_caution": [
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.googlequicksearchbox", "description": "Google Search", "risk": "caution"},
                    {"name": "com.google.android.inputmethod.latin", "description": "Gboard", "risk": "caution"},
                    {"name": "com.google.android.calendar", "description": "Google Calendar", "risk": "caution"}
                ],
                "google_dangerous": [
                    {"name": "com.google.android.gms", "description": "Google Play Services", "risk": "dangerous"},
                    {"name": "com.google.android.gsf", "description": "Google Services Framework", "risk": "dangerous"},
                    {"name": "com.google.android.tts", "description": "Text-to-speech", "risk": "dangerous"}
                ],
                "android_safe": [
                    {"name": "com.android.bips", "description": "Built-in Print Service", "risk": "safe"},
                    {"name": "com.android.bookmarkprovider", "description": "Bookmark Provider", "risk": "safe"},
                    {"name": "com.android.printspooler", "description": "Print Spooler", "risk": "safe"},
                    {"name": "com.android.wallpaperbackup", "description": "Wallpaper Backup", "risk": "safe"},
                    {"name": "com.android.wallpapercropper", "description": "Wallpaper Cropper", "risk": "safe"}
                ],
                "android_caution": [
                    {"name": "com.android.chrome", "description": "Chrome Browser", "risk": "caution"},
                    {"name": "com.android.mms.service", "description": "MMS Service", "risk": "caution"}
                ],
                "android_dangerous": [
                    {"name": "com.android.cellbroadcastreceiver", "description": "Emergency Alerts", "risk": "dangerous"},
                    {"name": "com.android.emergency", "description": "Emergency Information", "risk": "dangerous"}
                ],
                "third_party_safe": [
                    {"name": "com.facebook.katana", "description": "Facebook (if pre-installed)", "risk": "safe"},
                    {"name": "com.facebook.orca", "description": "Facebook Messenger (if pre-installed)", "risk": "safe"},
                    {"name": "com.instagram.android", "description": "Instagram (if pre-installed)", "risk": "safe"},
                    {"name": "com.netflix.mediaclient", "description": "Netflix (if pre-installed)", "risk": "safe"},
                    {"name": "com.spotify.music", "description": "Spotify (if pre-installed)", "risk": "safe"},
                    {"name": "com.twitter.android", "description": "Twitter (if pre-installed)", "risk": "safe"}
                ]
            }
        }

def main():
    remover = NothingRemover()
    
    print("Nothing Bloatware Removal Tool")
    print("1. Interactive removal (recommended)")
    print("2. List all apps and select what to remove")
    print("3. Remove all configured packages")
    print("4. Exit")
    
    choice = input("Select option (1-4): ").strip()
    
    if choice == '1':
        remover.interactive_removal()
    elif choice == '2':
        print("This will list all installed applications on your device.")
        if input("Continue? (y/n): ").lower() == 'y':
            remover.list_all_apps_removal()
    elif choice == '3':
        if input("This will remove ALL configured packages. Continue? (y/n): ").lower() == 'y':
            remover.remove_packages()
    elif choice == '4':
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()