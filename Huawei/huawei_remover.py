import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class HuaweiRemover(BloatwareRemover):
    """Huawei-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Huawei', 'Huawei/huawei_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Huawei bloatware configuration"""
        return {
            "categories": {
                "huawei_safe": [
                    {"name": "com.huawei.appmarket", "description": "Huawei AppGallery", "risk": "safe"},
                    {"name": "com.huawei.browser", "description": "Huawei Browser", "risk": "safe"},
                    {"name": "com.huawei.calculator", "description": "Huawei Calculator", "risk": "safe"},
                    {"name": "com.huawei.camera", "description": "Huawei Camera (if using alternative)", "risk": "safe"},
                    {"name": "com.huawei.compass", "description": "Compass app", "risk": "safe"},
                    {"name": "com.huawei.desktop.explorer", "description": "File Manager", "risk": "safe"},
                    {"name": "com.huawei.gameassistant", "description": "Game Assistant", "risk": "safe"},
                    {"name": "com.huawei.gamebox", "description": "Game Center", "risk": "safe"},
                    {"name": "com.huawei.health", "description": "Huawei Health", "risk": "safe"},
                    {"name": "com.huawei.himovie", "description": "Huawei Video", "risk": "safe"},
                    {"name": "com.huawei.hmusic", "description": "Huawei Music", "risk": "safe"},
                    {"name": "com.huawei.magazine", "description": "Magazine Unlock", "risk": "safe"},
                    {"name": "com.huawei.mirror", "description": "Mirror app", "risk": "safe"},
                    {"name": "com.huawei.notepad", "description": "Notepad", "risk": "safe"},
                    {"name": "com.huawei.parentcontrol", "description": "Parental Control", "risk": "safe"},
                    {"name": "com.huawei.scanner", "description": "AI Scanner", "risk": "safe"},
                    {"name": "com.huawei.screenrecorder", "description": "Screen Recorder", "risk": "safe"},
                    {"name": "com.huawei.search", "description": "Huawei Search", "risk": "safe"},
                    {"name": "com.huawei.tips", "description": "Tips app", "risk": "safe"},
                    {"name": "com.huawei.translator", "description": "Translator", "risk": "safe"},
                    {"name": "com.huawei.vassistant", "description": "Voice Assistant", "risk": "safe"},
                    {"name": "com.huawei.wallet", "description": "Huawei Wallet", "risk": "safe"},
                    {"name": "com.huawei.weather", "description": "Weather app", "risk": "safe"},
                    {"name": "com.huawei.works", "description": "Docs app", "risk": "safe"},
                    {"name": "com.huawei.android.chr", "description": "User Experience Program", "risk": "safe"},
                    {"name": "com.huawei.android.karaoke", "description": "Karaoke feature", "risk": "safe"},
                    {"name": "com.huawei.android.thememanager", "description": "Theme Manager", "risk": "safe"},
                    {"name": "com.huawei.bd", "description": "Big Data service", "risk": "safe"},
                    {"name": "com.huawei.hiaction", "description": "HiAction automation", "risk": "safe"},
                    {"name": "com.huawei.hicard", "description": "HiCard service", "risk": "safe"},
                    {"name": "com.huawei.hifolder", "description": "HiFolder", "risk": "safe"},
                    {"name": "com.huawei.hitouch", "description": "HiTouch", "risk": "safe"},
                    {"name": "com.huawei.livewallpaper.paradise", "description": "Live wallpapers", "risk": "safe"},
                    {"name": "com.huawei.motionservice", "description": "Motion service", "risk": "safe"},
                    {"name": "com.huawei.nearby", "description": "Huawei Share", "risk": "safe"},
                    {"name": "com.huawei.stylus", "description": "Stylus support", "risk": "safe"}
                ],
                "huawei_caution": [
                    {"name": "com.huawei.android.launcher", "description": "Huawei Launcher", "risk": "caution"},
                    {"name": "com.huawei.contacts", "description": "Contacts app", "risk": "caution"},
                    {"name": "com.huawei.deskclock", "description": "Clock app", "risk": "caution"},
                    {"name": "com.huawei.gallery", "description": "Gallery app", "risk": "caution"},
                    {"name": "com.huawei.mms", "description": "Messages app", "risk": "caution"},
                    {"name": "com.huawei.phoneservice", "description": "Phone app", "risk": "caution"},
                    {"name": "com.huawei.android.internal.app", "description": "Internal apps", "risk": "caution"},
                    {"name": "com.huawei.fastapp", "description": "Quick App Center", "risk": "caution"},
                    {"name": "com.huawei.intelligent", "description": "HiAssistant", "risk": "caution"},
                    {"name": "com.huawei.powergenie", "description": "Power Genie", "risk": "caution"}
                ],
                "huawei_dangerous": [
                    {"name": "com.huawei.android.hwaps", "description": "Huawei Mobile Services", "risk": "dangerous"},
                    {"name": "com.huawei.hwid.core", "description": "Huawei ID Core", "risk": "dangerous"},
                    {"name": "com.huawei.systemserver", "description": "System Server", "risk": "dangerous"},
                    {"name": "com.huawei.android.pushagent", "description": "Push service", "risk": "dangerous"},
                    {"name": "com.huawei.hwid", "description": "Huawei ID (required for many features)", "risk": "dangerous"},
                    {"name": "com.huawei.systemmanager", "description": "System Manager", "risk": "dangerous"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.docs", "description": "Google Drive", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"}
                ],
                "google_caution": [
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.googlequicksearchbox", "description": "Google Search", "risk": "caution"}
                ],
                "google_dangerous": [
                    {"name": "com.google.android.gms", "description": "Google Play Services (if present)", "risk": "dangerous"}
                ],
                "third_party_safe": [
                    {"name": "com.facebook.katana", "description": "Facebook", "risk": "safe"},
                    {"name": "com.facebook.orca", "description": "Facebook Messenger", "risk": "safe"},
                    {"name": "com.instagram.android", "description": "Instagram", "risk": "safe"},
                    {"name": "com.netflix.mediaclient", "description": "Netflix", "risk": "safe"},
                    {"name": "com.spotify.music", "description": "Spotify", "risk": "safe"},
                    {"name": "com.twitter.android", "description": "Twitter", "risk": "safe"},
                    {"name": "com.whatsapp", "description": "WhatsApp (if pre-installed)", "risk": "safe"}
                ]
            }
        }

def main():
    remover = HuaweiRemover()
    
    print("Huawei Bloatware Removal Tool")
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