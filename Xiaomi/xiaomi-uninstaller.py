import subprocess

# List of Xiaomi bloatware package names to uninstall

bloatware_packages = [

    "com.android.bips",

    "com.android.bookmarkprovider",

    "com.android.browser",

    "com.android.calendar",

    "com.android.cellbroadcastreceiver",

    "com.android.cellbroadcastreceiver.overlay.common",

    "com.android.chrome",

    "com.android.deskclock",

    "com.android.dreams.basic",

    "com.android.dreams.phototable",

    "com.android.egg",

    "com.android.emergency",

    "com.android.hotwordenrollment.okgoogle",

    "com.android.mms",

    "com.android.mms.service",

    "com.android.printspooler",

    "com.android.statementservice",

    "com.android.stk",

    "com.android.thememanager",

    "com.android.thememanager.module",

    "com.android.wallpaper.livepicker",

    "com.android.wallpaperbackup",

    "com.android.wallpapercropper",

    "com.google.android.apps.docs",

    "com.google.android.apps.maps",

    "com.google.android.apps.photos",

    "com.google.android.apps.meetings",

    "com.google.android.apps.wellbeing",

    "com.google.android.feedback",

    "com.google.android.gm",

    "com.google.android.gms",

    "com.google.android.gms.location.history",

    "com.google.android.googlequicksearchbox",

    "com.google.android.inputmethod.latin",

    "com.google.android.marvin.talkback",

    "com.google.android.music",

    "com.google.android.printservice.recommendation",

    "com.google.android.syncadapters.calendar",

    "com.google.android.tts",

    "com.google.android.videos",

    "com.google.android.youtube",

    "com.google.ar.lens",

    "com.mfashiongallery.emag",

    "com.mi.android.globalFileexplorer",

    "com.mi.android.globallauncher",

    "com.mi.android.globalpersonalassistant",

    "com.mi.globalTrendNews",

    "com.mi.health"

]

# Uninstall the bloatware packages

for package in bloatware_packages:

    subprocess.run(["adb", "shell", "pm", "uninstall", package])

print("Xiaomi bloatware uninstallation complete.")

