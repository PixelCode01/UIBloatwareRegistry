import subprocess

# List of package names to be uninstalled

packages_to_uninstall = [

    'com.coloros.aftersalesservice',

    'com.coloros.alarmclock',

    'com.coloros.assistantscreen',

    'com.coloros.backuprestore',

    'com.coloros.backuprestore.remoteservice',

    'com.coloros.calculator',

    'com.coloros.childrenspace',

    'com.coloros.cloud',

    'com.coloros.compass2',

    'com.coloros.filemanager',

    'com.coloros.floatassistant',

    'com.coloros.focusmode',

    'com.coloros.gallery3d',

    'com.coloros.gamespace',

    'com.coloros.healthcheck',

    'com.coloros.healthservice',

    'com.coloros.musiclink',

    'com.coloros.safesdkproxy',

    'com.coloros.screenrecorder',

    'com.coloros.securepay',

    'com.coloros.smartsidebar',

    'com.coloros.speechassist',

    'com.coloros.soundrecorder',

    'com.coloros.translate.engine',

    'com.coloros.video',

    'com.coloros.wallpapers',

    'com.coloros.weather.service',

    'com.coloros.widget.smallweather',

    'com.google.android.apps.googleassistant',

    'com.google.android.apps.maps',

    'com.google.android.apps.messaging',

    'com.google.android.apps.nbu.files',

    'com.google.android.apps.nbu.paisa.user',

    'com.google.android.apps.photos',

    'com.google.android.apps.wellbeing',

    'com.google.android.calendar',

    'com.google.android.documentsui',

    'com.google.android.feedback',

    'com.google.android.gm',

    'com.google.android.googlequicksearchbox',

    'com.google.android.inputmethod.latin',

    'com.google.android.keep',

    'com.google.android.marvin.talkback',

    'com.google.android.projection.gearhead',

    'com.google.android.soundpicker',

    'com.google.android.talk',

    'com.google.android.tts',

    'com.google.android.videos',

    'com.google.android.vr.home',

    'com.google.android.youtube',

    'com.google.ar.core',

    'com.google.ar.lens',

    'com.google.vr.vrcore',

    'com.google.android.contacts',

    'com.google.android.apps.messaging',

    'com.qualcomm.qti.ims',

    'com.qualcomm.qti.optinoverlay',

    'com.qualcomm.qti.simcontacts',

    'com.mediatek.atci.service',

    'com.mediatek.connectivity',

    'com.mediatek.dm',

    'com.mediatek.mtklogger',

    'com.mediatek.mtklogger.reciver',

    'com.mediatek.omacp',

    'com.mediatek.simcontacts',

    'com.mediatek.schpwronoff',

    'com.mediatek.selftest',

    'com.mediatek.settings.ext',

    'com.mediatek.schpwronoff',

    'com.mediatek.schpwronoff',

    'com.mediatek.voicecommand'

]

# Uninstall packages

for package in packages_to_uninstall:

    subprocess.run(['adb', 'shell', 'pm', 'uninstall', package], check=True)
