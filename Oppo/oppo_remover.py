import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.bloatware_remover import BloatwareRemover

class OppoRemover(BloatwareRemover):
    """Oppo-specific bloatware remover"""
    
    def __init__(self, test_mode: bool = False):
        super().__init__('Oppo', 'Oppo/oppo_config.json', test_mode)
    
    def _get_default_packages(self):
        """Default Oppo bloatware configuration"""
        return {
            "categories": {
                "android_safe": [
                    {"name": "com.android.bips", "description": "Built-in Print Service", "risk": "safe"},
                    {"name": "com.android.bookmarkprovider", "description": "Browser bookmark storage", "risk": "safe"},
                    {"name": "com.android.egg", "description": "Android Easter Egg", "risk": "safe"},
                    {"name": "com.android.printspooler", "description": "Mobile printing service", "risk": "safe"},
                    {"name": "com.android.wallpaper.livepicker", "description": "Live wallpaper selector", "risk": "safe"},
                    {"name": "com.android.wallpaperbackup", "description": "Wallpaper backup service", "risk": "safe"},
                    {"name": "com.android.wallpapercropper", "description": "Wallpaper cropping tool", "risk": "safe"},
                    {"name": "com.caf.fmradio", "description": "FM Radio service", "risk": "safe"}
                ],
                "android_caution": [
                    {"name": "com.android.chrome", "description": "Google Chrome browser", "risk": "caution"},
                    {"name": "com.android.mms.service", "description": "SMS/MMS messaging service", "risk": "caution"},
                    {"name": "com.android.providers.calendar", "description": "Calendar data provider", "risk": "caution"},
                    {"name": "com.android.providers.partnerbookmarks", "description": "Chrome bookmarks", "risk": "caution"},
                    {"name": "com.android.providers.userdictionary", "description": "Keyboard dictionary", "risk": "caution"}
                ],
                "android_dangerous": [
                    {"name": "com.android.cellbroadcastreceiver", "description": "Emergency alerts system", "risk": "dangerous"},
                    {"name": "com.android.cellbroadcastreceiver.overlay.common", "description": "Emergency alerts overlay", "risk": "dangerous"},
                    {"name": "com.android.vpndialogs", "description": "VPN connection dialogs", "risk": "dangerous"}
                ],
                "coloros_safe": [
                    {"name": "com.coloros.aftersalesservice", "description": "After-sales service app", "risk": "safe"},
                    {"name": "com.coloros.childrenspace", "description": "Kids Space mode", "risk": "safe"},
                    {"name": "com.coloros.compass2", "description": "Compass application", "risk": "safe"},
                    {"name": "com.coloros.focusmode", "description": "Focus Mode for productivity", "risk": "safe"},
                    {"name": "com.coloros.gamespace", "description": "Game Center", "risk": "safe"},
                    {"name": "com.coloros.healthcheck", "description": "Device health checker", "risk": "safe"},
                    {"name": "com.coloros.healthservice", "description": "Device health service", "risk": "safe"},
                    {"name": "com.coloros.musiclink", "description": "Music Party sharing", "risk": "safe"},
                    {"name": "com.coloros.safesdkproxy", "description": "Phone Cleaner (contains tracking)", "risk": "safe"},
                    {"name": "com.coloros.screenrecorder", "description": "Screen recording app", "risk": "safe"},
                    {"name": "com.coloros.speechassist", "description": "Voice assistant (Chinese)", "risk": "safe"},
                    {"name": "com.coloros.translate.engine", "description": "Translation service", "risk": "safe"},
                    {"name": "com.coloros.video", "description": "Video player", "risk": "safe"},
                    {"name": "com.coloros.wallpapers", "description": "Wallpaper collection", "risk": "safe"},
                    {"name": "com.coloros.widget.smallweather", "description": "Weather widget", "risk": "safe"}
                ],
                "coloros_caution": [
                    {"name": "com.coloros.alarmclock", "description": "Alarm and clock app", "risk": "caution"},
                    {"name": "com.coloros.assistantscreen", "description": "Smart Assistant", "risk": "caution"},
                    {"name": "com.coloros.backuprestore", "description": "Clone Phone backup", "risk": "caution"},
                    {"name": "com.coloros.calculator", "description": "Calculator app", "risk": "caution"},
                    {"name": "com.coloros.cloud", "description": "Oppo Cloud storage", "risk": "caution"},
                    {"name": "com.coloros.filemanager", "description": "File Manager", "risk": "caution"},
                    {"name": "com.coloros.floatassistant", "description": "Floating window assistant", "risk": "caution"},
                    {"name": "com.coloros.gallery3d", "description": "Gallery app", "risk": "caution"},
                    {"name": "com.coloros.securepay", "description": "Secure payment service", "risk": "caution"},
                    {"name": "com.coloros.smartsidebar", "description": "Smart Sidebar", "risk": "caution"},
                    {"name": "com.coloros.soundrecorder", "description": "Voice recorder", "risk": "caution"},
                    {"name": "com.coloros.weather.service", "description": "Weather service", "risk": "caution"}
                ],
                "google_safe": [
                    {"name": "com.google.android.apps.googleassistant", "description": "Google Assistant", "risk": "safe"},
                    {"name": "com.google.android.apps.nbu.files", "description": "Files by Google", "risk": "safe"},
                    {"name": "com.google.android.apps.nbu.paisa.user", "description": "Google Pay", "risk": "safe"},
                    {"name": "com.google.android.apps.photos", "description": "Google Photos", "risk": "safe"},
                    {"name": "com.google.android.apps.wellbeing", "description": "Digital Wellbeing", "risk": "safe"},
                    {"name": "com.google.android.feedback", "description": "Google Feedback", "risk": "safe"},
                    {"name": "com.google.android.keep", "description": "Google Keep notes", "risk": "safe"},
                    {"name": "com.google.android.music", "description": "Google Play Music", "risk": "safe"},
                    {"name": "com.google.android.projection.gearhead", "description": "Android Auto", "risk": "safe"},
                    {"name": "com.google.android.soundpicker", "description": "Sound picker", "risk": "safe"},
                    {"name": "com.google.android.talk", "description": "Google Talk", "risk": "safe"},
                    {"name": "com.google.android.videos", "description": "Google Play Movies", "risk": "safe"},
                    {"name": "com.google.android.youtube", "description": "YouTube", "risk": "safe"},
                    {"name": "com.google.ar.core", "description": "Google ARCore", "risk": "safe"},
                    {"name": "com.google.ar.lens", "description": "Google Lens", "risk": "safe"}
                ],
                "google_caution": [
                    {"name": "com.google.android.apps.maps", "description": "Google Maps", "risk": "caution"},
                    {"name": "com.google.android.apps.messaging", "description": "Google Messages", "risk": "caution"},
                    {"name": "com.google.android.calendar", "description": "Google Calendar", "risk": "caution"},
                    {"name": "com.google.android.documentsui", "description": "Files app", "risk": "caution"},
                    {"name": "com.google.android.gm", "description": "Gmail", "risk": "caution"},
                    {"name": "com.google.android.googlequicksearchbox", "description": "Google Search", "risk": "caution"},
                    {"name": "com.google.android.inputmethod.latin", "description": "Gboard keyboard", "risk": "caution"},
                    {"name": "com.google.android.contacts", "description": "Google Contacts", "risk": "caution"}
                ],
                "hardware_safe": [
                    {"name": "com.qualcomm.qti.optinoverlay", "description": "Qualcomm opt-in overlay", "risk": "safe"},
                    {"name": "com.qualcomm.qti.simcontacts", "description": "SIM contact management", "risk": "safe"}
                ],
                "hardware_caution": [
                    {"name": "com.mediatek.atci.service", "description": "AT command interface", "risk": "caution"},
                    {"name": "com.mediatek.connectivity", "description": "Connectivity service", "risk": "caution"},
                    {"name": "com.mediatek.dm", "description": "Device management", "risk": "caution"},
                    {"name": "com.mediatek.mtklogger", "description": "System logger", "risk": "caution"},
                    {"name": "com.mediatek.omacp", "description": "OMA client provisioning", "risk": "caution"},
                    {"name": "com.mediatek.simcontacts", "description": "SIM contacts", "risk": "caution"},
                    {"name": "com.mediatek.selftest", "description": "Hardware self-test", "risk": "caution"},
                    {"name": "com.mediatek.settings.ext", "description": "Settings extensions", "risk": "caution"},
                    {"name": "com.mediatek.voicecommand", "description": "Voice command service", "risk": "caution"}
                ],
                "hardware_dangerous": [
                    {"name": "com.qualcomm.qti.ims", "description": "IMS service for calls", "risk": "dangerous"},
                    {"name": "com.qualcomm.qti.telephonyservice", "description": "Telephony service", "risk": "dangerous"},
                    {"name": "com.google.android.marvin.talkback", "description": "Accessibility service", "risk": "dangerous"},
                    {"name": "com.google.android.tts", "description": "Text-to-speech engine", "risk": "dangerous"}
                ]
            }
        }

def main():
    remover = OppoRemover()
    
    print("Oppo Bloatware Removal Tool")
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