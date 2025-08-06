import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class MotorolaRemover(BloatwareRemover):
    """Motorola-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Motorola', 'Motorola/motorola_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Motorola bloatware configuration"""
        return {
            "categories": {
                "motorola_safe": [
                    {"name": "com.motorola.camera3", "description": "Motorola Camera (if using alternative)", "risk": "safe"},
                    {"name": "com.motorola.ccc.notification", "description": "CCC Notification", "risk": "safe"},
                    {"name": "com.motorola.demo", "description": "Demo mode", "risk": "safe"},
                    {"name": "com.motorola.faceunlock", "description": "Face Unlock", "risk": "safe"},
                    {"name": "com.motorola.gamemode", "description": "Game Mode", "risk": "safe"},
                    {"name": "com.motorola.help", "description": "Motorola Help", "risk": "safe"},
                    {"name": "com.motorola.launcher3", "description": "Motorola Launcher (if using alternative)", "risk": "safe"},
                    {"name": "com.motorola.moto", "description": "Moto app", "risk": "safe"},
                    {"name": "com.motorola.motocare", "description": "Moto Care", "risk": "safe"},
                    {"name": "com.motorola.motodisplay", "description": "Moto Display", "risk": "safe"},
                    {"name": "com.motorola.motovoice", "description": "Moto Voice", "risk": "safe"},
                    {"name": "com.motorola.personalize", "description": "Moto Personalize", "risk": "safe"},
                    {"name": "com.motorola.scanner", "description": "Moto Scanner", "risk": "safe"},
                    {"name": "com.motorola.timeweatherwidget", "description": "Time Weather Widget", "risk": "safe"},
                    {"name": "com.motorola.visualizer", "description": "Audio Visualizer", "risk": "safe"},
                    {"name": "com.motorola.wallpaper", "description": "Motorola Wallpapers", "risk": "safe"},
                    {"name": "com.motorola.weather", "description": "Weather app", "risk": "safe"},
                    {"name": "com.motorola.actions", "description": "Moto Actions", "risk": "safe"},
                    {"name": "com.motorola.audiomonitor", "description": "Audio Monitor", "risk": "safe"},
                    {"name": "com.motorola.cameraone", "description": "Camera One", "risk": "safe"},
                    {"name": "com.motorola.dolby.dolbyui", "description": "Dolby Audio", "risk": "safe"},
                    {"name": "com.motorola.gestureservice", "description": "Gesture Service", "risk": "safe"},
                    {"name": "com.motorola.moto.checkin", "description": "Moto Check-in", "risk": "safe"},
                    {"name": "com.motorola.notification", "description": "Moto Notification", "risk": "safe"},
                    {"name": "com.motorola.omadm.service", "description": "OMA DM Service", "risk": "safe"},
                    {"name": "com.motorola.slpc", "description": "SLPC Service", "risk": "safe"},
                    {"name": "com.motorola.targetnotif", "description": "Target Notification", "risk": "safe"}
                ],
                "motorola_caution": [
                    {"name": "com.motorola.android.providers.imei", "description": "IMEI provider", "risk": "caution"},
                    {"name": "com.motorola.contacts", "description": "Motorola Contacts", "risk": "caution"},
                    {"name": "com.motorola.gallery", "description": "Motorola Gallery", "risk": "caution"},
                    {"name": "com.motorola.messaging", "description": "Motorola Messages", "risk": "caution"},
                    {"name": "com.motorola.motocare.internal", "description": "Moto Care Internal", "risk": "caution"},
                    {"name": "com.motorola.motosignature.app", "description": "Moto Signature", "risk": "caution"},
                    {"name": "com.motorola.android.settings.intelligence", "description": "Settings Intelligence", "risk": "caution"},
                    {"name": "com.motorola.ccc.ota", "description": "OTA Updates", "risk": "caution"},
                    {"name": "com.motorola.devicestatistics", "description": "Device Statistics", "risk": "caution"},
                    {"name": "com.motorola.modservice", "description": "Mod Service", "risk": "caution"}
                ],
                "motorola_dangerous": [
                    {"name": "com.motorola.android.providers.settings", "description": "Settings provider", "risk": "dangerous"},
                    {"name": "com.motorola.frameworks.core.addon", "description": "Motorola Framework", "risk": "dangerous"},
                    {"name": "com.motorola.service.main", "description": "Motorola Main Service", "risk": "dangerous"},
                    {"name": "com.motorola.bootquiet", "description": "Boot Service", "risk": "dangerous"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.docs", "description": "Google Drive", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.youtube.music", "description": "YouTube Music", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"},
                    {"name": "com.google.android.keep", "description": "Google Keep", "risk": "safe"},
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"}
                ],
                "google_caution": [
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.googlequicksearchbox", "description": "Google Search", "risk": "caution"},
                    {"name": "com.google.android.inputmethod.latin", "description": "Gboard", "risk": "caution"}
                ],
                "google_dangerous": [
                    {"name": "com.google.android.gms", "description": "Google Play Services", "risk": "dangerous"},
                    {"name": "com.google.android.gsf", "description": "Google Services Framework", "risk": "dangerous"},
                    {"name": "com.google.android.tts", "description": "Text-to-speech", "risk": "dangerous"}
                ],
                "carrier_verizon": [
                    {"name": "com.verizon.mips.services", "description": "Verizon Services", "risk": "safe"},
                    {"name": "com.verizon.obdm", "description": "Verizon Device Management", "risk": "safe"},
                    {"name": "com.verizon.services", "description": "Verizon Services", "risk": "safe"},
                    {"name": "com.vzw.apnlib", "description": "Verizon APN Library", "risk": "safe"},
                    {"name": "com.vzw.hss.myverizon", "description": "My Verizon", "risk": "safe"},
                    {"name": "com.vcast.mediamanager", "description": "Verizon Media Manager", "risk": "safe"}
                ],
                "carrier_att": [
                    {"name": "com.att.android.attsmartwifi", "description": "AT&T Smart Wi-Fi", "risk": "safe"},
                    {"name": "com.att.dh", "description": "AT&T Device Help", "risk": "safe"},
                    {"name": "com.att.dtv.shaderemote", "description": "AT&T TV Remote", "risk": "safe"},
                    {"name": "com.att.myWireless", "description": "myAT&T", "risk": "safe"},
                    {"name": "com.att.tv", "description": "AT&T TV", "risk": "safe"}
                ],
                "third_party_safe": [
                    {"name": "com.facebook.katana", "description": "Facebook", "risk": "safe"},
                    {"name": "com.facebook.orca", "description": "Facebook Messenger", "risk": "safe"},
                    {"name": "com.facebook.services", "description": "Facebook Services", "risk": "safe"},
                    {"name": "com.facebook.system", "description": "Facebook System", "risk": "safe"},
                    {"name": "com.instagram.android", "description": "Instagram", "risk": "safe"},
                    {"name": "com.netflix.mediaclient", "description": "Netflix", "risk": "safe"},
                    {"name": "com.spotify.music", "description": "Spotify", "risk": "safe"},
                    {"name": "com.twitter.android", "description": "Twitter", "risk": "safe"},
                    {"name": "com.amazon.mShop.android.shopping", "description": "Amazon Shopping", "risk": "safe"},
                    {"name": "com.amazon.mp3", "description": "Amazon Music", "risk": "safe"},
                    {"name": "com.amazon.venezia", "description": "Amazon Prime Video", "risk": "safe"},
                    {"name": "com.audible.application", "description": "Audible", "risk": "safe"},
                    {"name": "com.microsoft.office.excel", "description": "Microsoft Excel", "risk": "safe"},
                    {"name": "com.microsoft.office.powerpoint", "description": "Microsoft PowerPoint", "risk": "safe"},
                    {"name": "com.microsoft.office.word", "description": "Microsoft Word", "risk": "safe"},
                    {"name": "com.microsoft.skydrive", "description": "OneDrive", "risk": "safe"},
                    {"name": "com.skype.raider", "description": "Skype", "risk": "safe"}
                ]
            }
        }

def main():
    remover = MotorolaRemover()
    
    print("Motorola Bloatware Removal Tool")
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