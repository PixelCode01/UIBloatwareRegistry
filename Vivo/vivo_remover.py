import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class VivoRemover(BloatwareRemover):
    """Vivo-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Vivo', 'Vivo/vivo_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Vivo bloatware configuration"""
        return {
            "categories": {
                "vivo_safe": [
                    {"name": "com.android.bbkcalculator", "description": "Calculator app", "risk": "safe"},
                    {"name": "com.android.bbklog", "description": "Log collection service", "risk": "safe"},
                    {"name": "com.android.bbkmusic", "description": "i Music player", "risk": "safe"},
                    {"name": "com.android.bbksoundrecorder", "description": "Sound recorder", "risk": "safe"},
                    {"name": "com.bbk.photoframewidget", "description": "Photo widget", "risk": "safe"},
                    {"name": "com.bbk.scene.indoor", "description": "My House app", "risk": "safe"},
                    {"name": "com.bbk.theme", "description": "i Theme customization", "risk": "safe"},
                    {"name": "com.bbk.theme.resources", "description": "Theme Store", "risk": "safe"},
                    {"name": "com.baidu.duersdk.opensdk", "description": "ViVoice assistant", "risk": "safe"},
                    {"name": "com.baidu.input_vivo", "description": "Chinese keyboard", "risk": "safe"},
                    {"name": "com.ibimuyu.lockscreen", "description": "Glance Lockfeed", "risk": "safe"},
                    {"name": "com.vivo.collage", "description": "Photo collage maker", "risk": "safe"},
                    {"name": "com.vivo.compass", "description": "Compass app", "risk": "safe"},
                    {"name": "com.vivo.doubleinstance", "description": "App Clone feature", "risk": "safe"},
                    {"name": "com.vivo.doubletimezoneclock", "description": "Timezone widget", "risk": "safe"},
                    {"name": "com.vivo.dream.clock", "description": "Screensaver clock", "risk": "safe"},
                    {"name": "com.vivo.dream.music", "description": "Screensaver music", "risk": "safe"},
                    {"name": "com.vivo.dream.weather", "description": "Screensaver weather", "risk": "safe"},
                    {"name": "com.vivo.easyshare", "description": "Easy Share", "risk": "safe"},
                    {"name": "com.vivo.ewarranty", "description": "E-warranty service", "risk": "safe"},
                    {"name": "com.vivo.favorite", "description": "Favorites app", "risk": "safe"},
                    {"name": "com.vivo.floatingball", "description": "Floating ball assistant", "risk": "safe"},
                    {"name": "com.vivo.FMRadio", "description": "FM Radio app", "risk": "safe"},
                    {"name": "com.vivo.fuelsummary", "description": "Fuel summary", "risk": "safe"},
                    {"name": "com.vivo.gamewatch", "description": "Game monitoring", "risk": "safe"},
                    {"name": "com.vivo.globalsearch", "description": "Global search", "risk": "safe"},
                    {"name": "com.vivo.hiboard", "description": "Hi Board service", "risk": "safe"},
                    {"name": "com.vivo.vivokaraoke", "description": "Mobile KTV", "risk": "safe"},
                    {"name": "com.vivo.livewallpaper.coffeetime", "description": "Coffee time live wallpaper", "risk": "safe"},
                    {"name": "com.vivo.livewallpaper.coralsea", "description": "Coral sea live wallpaper", "risk": "safe"},
                    {"name": "com.vivo.livewallpaper.floatingcloud", "description": "Floating cloud wallpaper", "risk": "safe"},
                    {"name": "com.vivo.livewallpaper.silk", "description": "Silk live wallpaper", "risk": "safe"},
                    {"name": "com.vivo.magazine", "description": "Lockscreen Magazine", "risk": "safe"},
                    {"name": "com.vivo.mediatune", "description": "Media tune service", "risk": "safe"},
                    {"name": "com.vivo.minscreen", "description": "Mini screen feature", "risk": "safe"},
                    {"name": "com.vivo.motormode", "description": "Motor Mode", "risk": "safe"},
                    {"name": "com.vivo.carmode", "description": "Driving Mode (older phones)", "risk": "safe"},
                    {"name": "com.vivo.numbermark", "description": "Number marking service", "risk": "safe"},
                    {"name": "com.vivo.scanner", "description": "QR/Barcode scanner", "risk": "safe"},
                    {"name": "com.vivo.smartshot", "description": "Smart screenshot", "risk": "safe"},
                    {"name": "com.vivo.translator", "description": "Translation app", "risk": "safe"},
                    {"name": "com.vivo.video.floating", "description": "Video floating widget", "risk": "safe"},
                    {"name": "com.vivo.videoeditor", "description": "Video editor", "risk": "safe"},
                    {"name": "com.vivo.website", "description": "Vivo website shortcut", "risk": "safe"},
                    {"name": "com.vivo.widget.calendar", "description": "Calendar widget", "risk": "safe"},
                    {"name": "com.vlife.vivo.wallpaper", "description": "Vivo live wallpaper", "risk": "safe"},
                    {"name": "com.kikaoem.vivo.qisiemoji.inputmethod", "description": "Emoji keyboard", "risk": "safe"}
                ],
                "vivo_caution": [
                    {"name": "com.android.BBKClock", "description": "Clock app", "risk": "caution"},
                    {"name": "com.bbk.account", "description": "Vivo account service", "risk": "caution"},
                    {"name": "com.bbk.calendar", "description": "Vivo Calendar", "risk": "caution"},
                    {"name": "com.bbk.cloud", "description": "Vivo Cloud storage", "risk": "caution"},
                    {"name": "com.bbk.SuperPowerSave", "description": "Power saver mode", "risk": "caution"},
                    {"name": "com.iqoo.engineermode", "description": "Engineering Mode", "risk": "caution"},
                    {"name": "com.iqoo.secure", "description": "i Manager security", "risk": "caution"},
                    {"name": "com.vivo.appstore", "description": "Vivo App Store", "risk": "caution"},
                    {"name": "com.vivo.assistant", "description": "Jovi Smart Scene", "risk": "caution"},
                    {"name": "com.vivo.browser", "description": "Vivo Web Browser", "risk": "caution"},
                    {"name": "com.vivo.email", "description": "Email app", "risk": "caution"},
                    {"name": "com.vivo.gallery", "description": "Gallery app", "risk": "caution"},
                    {"name": "com.vivo.safecenter", "description": "Security center", "risk": "caution"},
                    {"name": "com.vivo.setupwizard", "description": "Setup wizard", "risk": "caution"},
                    {"name": "com.vivo.sim.contacts", "description": "SIM contacts", "risk": "caution"},
                    {"name": "com.vivo.smartmultiwindow", "description": "Multi-window feature", "risk": "caution"},
                    {"name": "com.vivo.unionpay", "description": "Vivo Pay", "risk": "caution"},
                    {"name": "com.vivo.weather", "description": "Weather app", "risk": "caution"},
                    {"name": "com.vivo.weather.provider", "description": "Weather service", "risk": "caution"}
                ],
                "vivo_dangerous": [
                    {"name": "com.bbk.iqoo.logsystem", "description": "System logging", "risk": "dangerous"},
                    {"name": "com.vivo.appfilter", "description": "App filtering service", "risk": "dangerous"},
                    {"name": "com.vivo.pushservice", "description": "Push notification service", "risk": "dangerous"}
                ],
                "facebook_bloat": [
                    {"name": "com.facebook.appmanager", "description": "Facebook App Manager", "risk": "safe"},
                    {"name": "com.facebook.services", "description": "Facebook Services", "risk": "safe"},
                    {"name": "com.facebook.system", "description": "Facebook System Service", "risk": "safe"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.docs", "description": "Google Drive", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.tachyon", "description": "Google Duo", "risk": "safe"},
                    {"name": "com.google.android.feedback", "description": "Google Feedback", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.printservice.recommendation", "description": "Mobile Printing", "risk": "safe"},
                    {"name": "com.google.android.syncadapters.calendar", "description": "Calendar sync", "risk": "safe"},
                    {"name": "com.google.android.syncadapters.contacts", "description": "Contacts sync", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies & TV", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"},
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"}
                ],
                "google_caution": [
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.googlequicksearchbox", "description": "Google Search widget", "risk": "caution"}
                ],
                "google_dangerous": [
                    {"name": "com.google.android.marvin.talkback", "description": "Accessibility service", "risk": "dangerous"},
                    {"name": "com.google.android.tts", "description": "Text-to-speech engine", "risk": "dangerous"}
                ],
                "qualcomm_safe": [
                    {"name": "com.qti.qualcomm.deviceinfo", "description": "Device information", "risk": "safe"},
                    {"name": "com.qti.qualcomm.datastatusnotification", "description": "Data status notifications", "risk": "safe"},
                    {"name": "com.qualcomm.embms", "description": "Enhanced multimedia broadcast", "risk": "safe"}
                ],
                "qualcomm_caution": [
                    {"name": "com.qualcomm.qti.lpa", "description": "Local profile assistant", "risk": "caution"},
                    {"name": "com.qti.confuridialer", "description": "Conference dialer", "risk": "caution"},
                    {"name": "com.qti.dpmserviceapp", "description": "Data protection manager", "risk": "caution"},
                    {"name": "com.qualcomm.qti.autoregistration", "description": "Auto registration service", "risk": "caution"},
                    {"name": "com.qualcomm.qti.callfeaturessetting", "description": "Call features settings", "risk": "caution"},
                    {"name": "com.qualcomm.qti.uim", "description": "User identity module", "risk": "caution"}
                ],
                "qualcomm_dangerous": [
                    {"name": "com.qualcomm.qti.ims", "description": "IMS service for VoLTE calls", "risk": "dangerous"}
                ]
            }
        }

def main():
    remover = VivoRemover()
    
    print("Vivo Bloatware Removal Tool")
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