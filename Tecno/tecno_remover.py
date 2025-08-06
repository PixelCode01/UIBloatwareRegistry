import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class TecnoRemover(BloatwareRemover):
    """Tecno-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Tecno', 'Tecno/tecno_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Tecno bloatware configuration"""
        return {
            "categories": {
                "tecno_safe": [
                    {"name": "net.bat.store", "description": "BAT Store application", "risk": "safe"},
                    {"name": "com.gallery20", "description": "Gallery 2.0 app", "risk": "safe"},
                    {"name": "com.transsion.compass", "description": "Compass application", "risk": "safe"},
                    {"name": "com.transsion.aivoiceassistant", "description": "AI Voice Assistant", "risk": "safe"},
                    {"name": "com.talpa.hibrowser", "description": "Hi Browser", "risk": "safe"},
                    {"name": "com.zaz.translate", "description": "Translation service", "risk": "safe"},
                    {"name": "com.transsion.letswitch", "description": "Phone switching tool", "risk": "safe"},
                    {"name": "com.transsion.healthlife", "description": "Health and fitness app", "risk": "safe"},
                    {"name": "com.transsion.notebook", "description": "Note-taking app", "risk": "safe"},
                    {"name": "com.transsion.scanningrecharger", "description": "Scanning recharger", "risk": "safe"},
                    {"name": "com.transsion.magicshow", "description": "Magic show app", "risk": "safe"},
                    {"name": "com.rlk.weathers", "description": "Weather application", "risk": "safe"},
                    {"name": "cn.wps.moffice_eng", "description": "WPS Office", "risk": "safe"},
                    {"name": "com.talpa.share", "description": "File sharing service", "risk": "safe"},
                    {"name": "com.transsion.tecnospot", "description": "Tecno Spot service", "risk": "safe"},
                    {"name": "com.transsnet.store", "description": "Transsnet Store", "risk": "safe"},
                    {"name": "com.transsion.filemanagerx", "description": "File Manager X", "risk": "safe"},
                    {"name": "com.tecno.appstore", "description": "Tecno App Store", "risk": "safe"},
                    {"name": "com.tecno.music", "description": "Tecno Music player", "risk": "safe"},
                    {"name": "com.tecno.video", "description": "Video player", "risk": "safe"},
                    {"name": "com.tecno.gallery", "description": "Gallery app", "risk": "safe"},
                    {"name": "com.tecno.weather", "description": "Weather app", "risk": "safe"},
                    {"name": "com.tecno.notes", "description": "Notes application", "risk": "safe"},
                    {"name": "com.tecno.scanner", "description": "QR/Barcode scanner", "risk": "safe"},
                    {"name": "com.tecno.gamepad", "description": "Game controller", "risk": "safe"},
                    {"name": "com.tecno.themes", "description": "Theme store", "risk": "safe"},
                    {"name": "com.tecno.wallpapers", "description": "Wallpaper collection", "risk": "safe"},
                    {"name": "com.tecno.launcher.theme", "description": "Launcher themes", "risk": "safe"},
                    {"name": "com.tecno.social", "description": "Social media integration", "risk": "safe"},
                    {"name": "com.tecno.backup", "description": "Backup service", "risk": "safe"},
                    {"name": "com.tecno.cleaner", "description": "Phone cleaner", "risk": "safe"},
                    {"name": "com.tecno.security", "description": "Security app", "risk": "safe"},
                    {"name": "com.tecno.boost", "description": "Performance booster", "risk": "safe"}
                ],
                "tecno_caution": [
                    {"name": "com.transsion.calculator", "description": "Calculator app", "risk": "caution"},
                    {"name": "com.transsion.calendar", "description": "Calendar application", "risk": "caution"},
                    {"name": "com.transsion.deskclock", "description": "Clock and alarm app", "risk": "caution"},
                    {"name": "com.transsion.soundrecorder", "description": "Sound recorder", "risk": "caution"},
                    {"name": "com.tecno.launcher", "description": "Tecno Launcher", "risk": "caution"},
                    {"name": "com.tecno.contacts", "description": "Contacts app", "risk": "caution"},
                    {"name": "com.tecno.dialer", "description": "Phone dialer", "risk": "caution"},
                    {"name": "com.tecno.messaging", "description": "SMS/MMS app", "risk": "caution"},
                    {"name": "com.tecno.settings", "description": "Settings extensions", "risk": "caution"},
                    {"name": "com.tecno.systemui", "description": "System UI components", "risk": "caution"}
                ],
                "tecno_dangerous": [
                    {"name": "com.tecno.framework", "description": "Tecno framework services", "risk": "dangerous"},
                    {"name": "com.tecno.core", "description": "Core system services", "risk": "dangerous"},
                    {"name": "com.tecno.system", "description": "System components", "risk": "dangerous"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.docs", "description": "Google Drive", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.youtube.music", "description": "YouTube Music", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"},
                    {"name": "com.google.android.keep", "description": "Google Keep", "risk": "safe"},
                    {"name": "com.google.android.apps.tachyon", "description": "Google Duo", "risk": "safe"},
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"}
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
                "mediatek_caution": [
                    {"name": "com.mediatek.connectivity", "description": "Connectivity service", "risk": "caution"},
                    {"name": "com.mediatek.mtklogger", "description": "System logger", "risk": "caution"},
                    {"name": "com.mediatek.settings.ext", "description": "Settings extensions", "risk": "caution"},
                    {"name": "com.mediatek.simcontacts", "description": "SIM contacts", "risk": "caution"}
                ],
                "mediatek_dangerous": [
                    {"name": "com.mediatek.ims", "description": "IMS service for calls", "risk": "dangerous"},
                    {"name": "com.mediatek.telephony", "description": "Telephony service", "risk": "dangerous"}
                ],
                "third_party_safe": [
                    {"name": "com.facebook.katana", "description": "Facebook app", "risk": "safe"},
                    {"name": "com.facebook.orca", "description": "Facebook Messenger", "risk": "safe"},
                    {"name": "com.whatsapp", "description": "WhatsApp (if pre-installed)", "risk": "safe"},
                    {"name": "com.instagram.android", "description": "Instagram", "risk": "safe"},
                    {"name": "com.twitter.android", "description": "Twitter", "risk": "safe"},
                    {"name": "com.netflix.mediaclient", "description": "Netflix", "risk": "safe"},
                    {"name": "com.spotify.music", "description": "Spotify", "risk": "safe"},
                    {"name": "com.opera.browser", "description": "Opera Browser", "risk": "safe"},
                    {"name": "com.opera.mini.native", "description": "Opera Mini", "risk": "safe"}
                ]
            }
        }

def main():
    remover = TecnoRemover()
    
    print("Tecno Bloatware Removal Tool")
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