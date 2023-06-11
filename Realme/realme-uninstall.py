import subprocess

# List of package names to uninstall

package_names = [

    "com.realme.safetynet",

    "com.coloros.oppomusic",

    "com.oppo.nearme.gamecenter",

    "com.coloros.backuprestore",

    "com.coloros.childrenspace",
  
    "com.coloros.calendar.sns",

    "com.coloros.compass2",

    "com.coloros.engmodeinstall",

    "com.coloros.eyesprotect",

    "com.coloros.filemanager",

    "com.coloros.gallery3d",

    "com.coloros.gamespace",

    "com.coloros.musicparty",

    "com.coloros.sauhelper",

    "com.coloros.screencast",

    "com.coloros.screenrecorder",

    "com.coloros.smartdrive",

    "com.coloros.weather.service",

    "com.oppo.community",

    "com.oppo.market",

    "com.oppo.quicksearchbox",

    "com.oppo.reader",

    "com.oppo.record",

    "com.oppo.usercenter",

    "com.oppo.widget.pkgsafety",

    "com.oppo.widget.smallweather",

    "com.oppo.yellowpage",

    "com.realme.gamecenter",

    "com.realme.linkservice",

    "com.realme.pay",

    "com.realme.smartdrive",

    "com.realme.store",

    "com.realme.weather",

    "com.heytap.browser",

    "com.heytap.cloud",

    "com.heytap.habit.analysis",

    "com.heytap.mcs",

    "com.heytap.usercenter",

    "com.heytap.video",

    "com.heytap.yoli",

    "com.oppo.launcher",

    "com.android.bookmarkprovider",

    "com.android.browser",

    "com.coloros.alarmclock",

    "com.coloros.bootreg",

    "com.coloros.childrenspaceagent",

    "com.coloros.colormoservice",

    "com.coloros.oppopowermonitor",

    "com.coloros.personalassistant",

    "com.coloros.phonemanager",

    "com.coloros.recents",

    "com.coloros.smarttask",

    "com.coloros.theme.default",

    "com.coloros.assistantscreen",

    "com.coloros.backuprestore.remoteservice",

    "com.coloros.calculator",

    "com.coloros.findmyphone",

    "com.coloros.gamespaceui",

    "com.coloros.note",

    "com.coloros.soundrecorder",

    "com.coloros.speechassist",

    "com.coloros.video",

    "com.coloros.wallet",

    "com.oppo.afterservice",

    "com.oppo.auth",

    "com.oppo.coolbooster",

    "com.oppo.engineermode",

    "com.oppo.favorite",

    "com.oppo.fingerprints.service",

    "com.oppo.flashlight",

    "com.oppo.hifisystem",

    "com.oppo.oppopowermonitor",

    "com.oppo.reader.global",

    "com.oppo.regional.prerecord",

    "com.oppo.safe",

    "com.oppo.securepay.token",

    "com.oppo.simsettings",

    "com.oppo.usercenter.overlay",

    "com.oppo.wallpaperbackup",

    "com.realme.customwatch",

    "com.realme.font",

    "com.realme.screenshot",

    "com.realme.wifiassistant",

    "com.realme.album",

    "com.realme.coolu",

    "com.realme.customization",

    "com.realme.desktopbackup",

    "com.realme.filemanager",

    "com.realme.gamespace",

    "com.realme.smartlifecycle",

    "com.realme.themestore",

    "com.realme.voiceassistant",

    "com.realme.weather2",

    "com.heytap.livewallpaper",

    "com.heytap.pictorial",

    "com.heytap.screenclear",

    "com.heytap.yoliu",

    "com.coloros.breathlight",

    "com.coloros.calculator2",

    "com.coloros.directservice",

    "com.coloros.oppopowermonitor2",

    "com.coloros.oshare",

    "com.coloros.pictorial",

    "com.coloros.smartdriveassistant",

    "com.coloros.widget.smallweather",

    "com.heytap.camera",

    "com.heytap.cloudsync",

    "com.heytap.datamigration",

    "com.heytap.feedback",

    "com.heytap.i18n"

]

# Function to uninstall an app using ADB

def uninstall_app(package_name):

    command = f"adb shell pm uninstall --user 0 {package_name}"

    subprocess.run(command, shell=True, check=True)

# Uninstall all the apps

for package_name in package_names:

    try:

        uninstall_app(package_name)

        print(f"Uninstalled: {package_name}")

    except subprocess.CalledProcessError:

        print(f"Failed to uninstall: {package_name}")

