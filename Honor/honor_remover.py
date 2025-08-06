import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class HonorRemover(BloatwareRemover):
    """Honor-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Honor', 'Honor/honor_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Honor bloatware configuration"""
        return {
            "categories": {
                "honor_safe": [
                    {"name": "com.hihonor.appmarket", "description": "Honor AppGallery", "risk": "safe"},
                    {"name": "com.hihonor.browser", "description": "Honor Browser", "risk": "safe"},
                    {"name": "com.hihonor.calculator", "description": "Honor Calculator", "risk": "safe"},
                    {"name": "com.hihonor.camera", "description": "Honor Camera (if using alternative)", "risk": "safe"},
                    {"name": "com.hihonor.compass", "description": "Compass app", "risk": "safe"},
                    {"name": "com.hihonor.filemanager", "description": "File Manager", "risk": "safe"},
                    {"name": "com.hihonor.gameassistant", "description": "Game Assistant", "risk": "safe"},
                    {"name": "com.hihonor.gamecenter", "description": "Game Center", "risk": "safe"},
                    {"name": "com.hihonor.health", "description": "Honor Health", "risk": "safe"},
                    {"name": "com.hihonor.himovie", "description": "Honor Video", "risk": "safe"},
                    {"name": "com.hihonor.music", "description": "Honor Music", "risk": "safe"},
                    {"name": "com.hihonor.notepad", "description": "Notepad", "risk": "safe"},
                    {"name": "com.hihonor.parentcontrol", "description": "Parental Control", "risk": "safe"},
                    {"name": "com.hihonor.scanner", "description": "AI Scanner", "risk": "safe"},
                    {"name": "com.hihonor.screenrecorder", "description": "Screen Recorder", "risk": "safe"},
                    {"name": "com.hihonor.search", "description": "Honor Search", "risk": "safe"},
                    {"name": "com.hihonor.tips", "description": "Tips app", "risk": "safe"},
                    {"name": "com.hihonor.translator", "description": "Translator", "risk": "safe"},
                    {"name": "com.hihonor.vassistant", "description": "Voice Assistant", "risk": "safe"},
                    {"name": "com.hihonor.wallet", "description": "Honor Wallet", "risk": "safe"},
                    {"name": "com.hihonor.weather", "description": "Weather app", "risk": "safe"},
                    {"name": "com.hihonor.yoyo", "description": "YOYO Assistant", "risk": "safe"},
                    {"name": "com.hihonor.android.chr", "description": "User Experience Program", "risk": "safe"},
                    {"name": "com.hihonor.android.karaoke", "description": "Karaoke feature", "risk": "safe"},
                    {"name": "com.hihonor.android.thememanager", "description": "Theme Manager", "risk": "safe"},
                    {"name": "com.hihonor.bd", "description": "Big Data service", "risk": "safe"},
                    {"name": "com.hihonor.hiaction", "description": "HiAction automation", "risk": "safe"},
                    {"name": "com.hihonor.hicard", "description": "HiCard service", "risk": "safe"},
                    {"name": "com.hihonor.hifolder", "description": "HiFolder", "risk": "safe"},
                    {"name": "com.hihonor.hitouch", "description": "HiTouch", "risk": "safe"},
                    {"name": "com.hihonor.livewallpaper", "description": "Live wallpapers", "risk": "safe"},
                    {"name": "com.hihonor.motionservice", "description": "Motion service", "risk": "safe"},
                    {"name": "com.hihonor.nearby", "description": "Honor Share", "risk": "safe"},
                    {"name": "com.hihonor.stylus", "description": "Stylus support", "risk": "safe"},
                    {"name": "com.hihonor.magicui.smartcare", "description": "Smart Care", "risk": "safe"},
                    {"name": "com.hihonor.magicui.optimization", "description": "System Optimization", "risk": "safe"}
                ],
                "honor_caution": [
                    {"name": "com.hihonor.android.launcher", "description": "Honor Launcher", "risk": "caution"},
                    {"name": "com.hihonor.contacts", "description": "Contacts app", "risk": "caution"},
                    {"name": "com.hihonor.deskclock", "description": "Clock app", "risk": "caution"},
                    {"name": "com.hihonor.gallery", "description": "Gallery app", "risk": "caution"},
                    {"name": "com.hihonor.mms", "description": "Messages app", "risk": "caution"},
                    {"name": "com.hihonor.phone", "description": "Phone app", "risk": "caution"},
                    {"name": "com.hihonor.fastapp", "description": "Quick App Center", "risk": "caution"},
                    {"name": "com.hihonor.intelligent", "description": "HiAssistant", "risk": "caution"},
                    {"name": "com.hihonor.powergenie", "description": "Power Genie", "risk": "caution"},
                    {"name": "com.hihonor.magicui.assistant", "description": "Magic UI Assistant", "risk": "caution"}
                ],
                "honor_dangerous": [
                    {"name": "com.hihonor.android.hms", "description": "Honor Mobile Services", "risk": "dangerous"},
                    {"name": "com.hihonor.hwid", "description": "Honor ID", "risk": "dangerous"},
                    {"name": "com.hihonor.systemserver", "description": "System Server", "risk": "dangerous"},
                    {"name": "com.hihonor.android.pushagent", "description": "Push service", "risk": "dangerous"},
                    {"name": "com.hihonor.hwid.core", "description": "Honor ID Core", "risk": "dangerous"},
                    {"name": "com.hihonor.systemmanager", "description": "System Manager", "risk": "dangerous"}
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
                    {"name": "com.whatsapp", "description": "WhatsApp (if pre-installed)", "risk": "safe"},
                    {"name": "com.booking", "description": "Booking.com", "risk": "safe"},
                    {"name": "com.tripadvisor.tripadvisor", "description": "TripAdvisor", "risk": "safe"}
                ]
            }
        }

def main():
    remover = HonorRemover()
    
    print("Honor Bloatware Removal Tool")
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