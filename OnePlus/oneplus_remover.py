import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class OnePlusRemover(BloatwareRemover):
    def __init__(self, test_mode: bool = False, use_registry: bool = True):
        super().__init__('OnePlus', 'OnePlus/oneplus_config.json', test_mode, use_registry=use_registry)
    
    def _get_default_packages(self):
        return {
            "categories": {
                "oneplus_safe": [
                    {"name": "com.oneplus.account", "description": "OnePlus Account service", "risk": "safe"},
                    {"name": "com.oneplus.backuprestore", "description": "OnePlus Clone Phone", "risk": "safe"},
                    {"name": "com.oneplus.brickmode", "description": "Brick mode service", "risk": "safe"},
                    {"name": "com.oneplus.calculator", "description": "OnePlus Calculator", "risk": "safe"},
                    {"name": "com.oneplus.camera", "description": "OnePlus Camera (if using alternative)", "risk": "safe"},
                    {"name": "com.oneplus.card", "description": "OnePlus Card service", "risk": "safe"},
                    {"name": "com.oneplus.cloud", "description": "OnePlus Cloud storage", "risk": "safe"},
                    {"name": "com.oneplus.compass", "description": "Compass application", "risk": "safe"},
                    {"name": "com.oneplus.deskclock", "description": "Clock and alarm app", "risk": "safe"},
                    {"name": "com.oneplus.filemanager", "description": "OnePlus File Manager", "risk": "safe"},
                    {"name": "com.oneplus.gallery", "description": "OnePlus Gallery", "risk": "safe"},
                    {"name": "com.oneplus.gamespace", "description": "Game Space", "risk": "safe"},
                    {"name": "com.oneplus.iconpack.circle", "description": "Circle icon pack", "risk": "safe"},
                    {"name": "com.oneplus.iconpack.square", "description": "Square icon pack", "risk": "safe"},
                    {"name": "com.oneplus.market", "description": "OnePlus Store", "risk": "safe"},
                    {"name": "com.oneplus.note", "description": "OnePlus Notes", "risk": "safe"},
                    {"name": "com.oneplus.opsocialnetwork", "description": "OnePlus Community", "risk": "safe"},
                    {"name": "com.oneplus.screenshot", "description": "Screenshot service", "risk": "safe"},
                    {"name": "com.oneplus.skin", "description": "OnePlus themes", "risk": "safe"},
                    {"name": "com.oneplus.soundrecorder", "description": "Sound recorder", "risk": "safe"},
                    {"name": "com.oneplus.weather", "description": "OnePlus Weather", "risk": "safe"},
                    {"name": "com.oneplus.widget", "description": "OnePlus widgets", "risk": "safe"},
                    {"name": "com.oneplus.worklife", "description": "Work Life Balance", "risk": "safe"},
                    {"name": "net.oneplus.commonlogtool", "description": "Common log tool", "risk": "safe"},
                    {"name": "net.oneplus.odm", "description": "ODM service", "risk": "safe"},
                    {"name": "net.oneplus.oemtcma", "description": "OEM TCMA service", "risk": "safe"},
                    {"name": "net.oneplus.push", "description": "OnePlus push service", "risk": "safe"},
                    {"name": "net.oneplus.weather", "description": "Weather service", "risk": "safe"}
                ],
                "oneplus_caution": [
                    {"name": "com.oneplus.contacts", "description": "OnePlus Contacts", "risk": "caution"},
                    {"name": "com.oneplus.dialer", "description": "OnePlus Phone app", "risk": "caution"},
                    {"name": "com.oneplus.launcher", "description": "OnePlus Launcher", "risk": "caution"},
                    {"name": "com.oneplus.mms", "description": "OnePlus Messages", "risk": "caution"},
                    {"name": "com.oneplus.music", "description": "OnePlus Music player", "risk": "caution"},
                    {"name": "com.oneplus.setupwizard", "description": "Setup wizard", "risk": "caution"},
                    {"name": "com.oneplus.systemui", "description": "System UI components", "risk": "caution"},
                    {"name": "net.oneplus.launcher", "description": "OxygenOS Launcher", "risk": "caution"},
                    {"name": "net.oneplus.opsystemhelper", "description": "System helper", "risk": "caution"}
                ],
                "oneplus_dangerous": [
                    {"name": "com.oneplus.framework", "description": "OnePlus framework", "risk": "dangerous"},
                    {"name": "com.oneplus.opbugreportlite", "description": "Bug reporting service", "risk": "dangerous"},
                    {"name": "com.oneplus.security", "description": "Security framework", "risk": "dangerous"},
                    {"name": "net.oneplus.opdiagnose", "description": "System diagnostics", "risk": "dangerous"}
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
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"},
                    {"name": "com.google.android.feedback", "description": "Google Feedback", "risk": "safe"}
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
                "third_party_safe": [
                    {"name": "com.netflix.mediaclient", "description": "Netflix (if pre-installed)", "risk": "safe"},
                    {"name": "com.netflix.partner.activation", "description": "Netflix activation", "risk": "safe"},
                    {"name": "com.facebook.katana", "description": "Facebook", "risk": "safe"},
                    {"name": "com.facebook.orca", "description": "Facebook Messenger", "risk": "safe"},
                    {"name": "com.facebook.services", "description": "Facebook Services", "risk": "safe"},
                    {"name": "com.facebook.system", "description": "Facebook System", "risk": "safe"},
                    {"name": "com.instagram.android", "description": "Instagram", "risk": "safe"},
                    {"name": "com.spotify.music", "description": "Spotify", "risk": "safe"}
                ],
                "qualcomm_safe": [
                    {"name": "com.qualcomm.qti.workloadclassifier", "description": "Workload classifier", "risk": "safe"},
                    {"name": "com.qualcomm.qti.poweroffalarm", "description": "Power off alarm", "risk": "safe"},
                    {"name": "com.qualcomm.qti.devicestatisticsservice", "description": "Device statistics", "risk": "safe"}
                ],
                "qualcomm_caution": [
                    {"name": "com.qualcomm.qti.callenhancement", "description": "Call enhancement", "risk": "caution"},
                    {"name": "com.qualcomm.qti.callfeaturessetting", "description": "Call features", "risk": "caution"},
                    {"name": "com.qualcomm.qti.dynamicddsservice", "description": "Dynamic DDS service", "risk": "caution"},
                    {"name": "com.qualcomm.qti.simsettings", "description": "SIM settings", "risk": "caution"}
                ],
                "qualcomm_dangerous": [
                    {"name": "com.qualcomm.qti.ims", "description": "IMS service for VoLTE", "risk": "dangerous"},
                    {"name": "com.qualcomm.qti.telephonyservice", "description": "Telephony service", "risk": "dangerous"}
                ],
                "android_safe": [
                    {"name": "com.android.bips", "description": "Built-in Print Service", "risk": "safe"},
                    {"name": "com.android.bookmarkprovider", "description": "Bookmark provider", "risk": "safe"},
                    {"name": "com.android.printspooler", "description": "Print spooler", "risk": "safe"},
                    {"name": "com.android.wallpaperbackup", "description": "Wallpaper backup", "risk": "safe"},
                    {"name": "com.android.wallpapercropper", "description": "Wallpaper cropper", "risk": "safe"}
                ],
                "android_caution": [
                    {"name": "com.android.chrome", "description": "Chrome browser", "risk": "caution"},
                    {"name": "com.android.mms.service", "description": "MMS service", "risk": "caution"}
                ],
                "android_dangerous": [
                    {"name": "com.android.cellbroadcastreceiver", "description": "Emergency alerts", "risk": "dangerous"},
                    {"name": "com.android.emergency", "description": "Emergency information", "risk": "dangerous"}
                ]
            }
        }

def main():
    remover = OnePlusRemover()
    
    print("OnePlus Bloatware Removal Tool")
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