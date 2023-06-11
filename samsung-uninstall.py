import subprocess

# List of Samsung bloatware package names

bloatware_packages = [

    "samsung.android.bixby.wakeup",

    "samsung.android.app.spage",

    "samsung.android.app.routines",

    "samsung.android.bixby.service",

    "samsung.android.visionintelligence",

    "samsung.android.bixby.agent",

    "samsung.android.bixby.agent.dummy",

    "samsung.android.bixbyvision.framework",

    "dsi.ant.sample.acquirechannels",

    "dsi.ant.service.socket",

    "dsi.ant.server",

    "dsi.ant.plugins.antplus",

    "samsung.android.messaging",

    "sec.android.easyonehand",

    "samsung.android.drivelink.stub",

    "sec.android.widgetapp.samsungapps",

    "sec.android.app.sbrowser",

    "samsung.android.mateagent",

    "sec.android.easyMover.Agent",

    "samsung.android.app.watchmanagerstub",

    "sec.android.daemonapp",

    "samsung.android.app.social",

    "samsung.ecomm.global",

    "sec.android.app.voicenote",

    "samsung.android.oneconnect",

    "samsung.android.voc",

    "sec.android.app.popupcalculator",

    "sec.android.splitsound",

    "mobeam.barcodeService",

    "samsung.android.app.dressroom",

    "samsung.android.scloud",

    "samsung.android.sdk.handwriting",

    "samsung.android.sdk.professionalaudio.utility.jammonitor",

    "samsung.android.universalswitch",

    "samsung.android.visioncloudagent",

    "samsung.android.widgetapp.yahooedge.finance",

    "samsung.android.widgetapp.yahooedge.sport",

    "samsung.app.highlightplayer",

    "samsung.safetyinformation",

    "samsung.storyservice",

    "samsung.android.service.aircommand",

    "samsung.android.app.aodservice",

    "sec.android.app.dexonpc",

    "samsung.android.ardrawing",

    "samsung.android.svoiceime",

    "samsung.android.beaconmanager",

    "samsung.android.email.provider",

    "wsomacp",

    "samsung.android.samsungpassautofill",

    "samsung.android.authfw",

    "samsung.android.samsungpass",

    "samsung.android.spay",

    "samsung.android.spayfw",

    "android.bips",

    "google.android.printservice.recommendation",

    "android.printspooler",

    "samsung.android.app.ledbackcover",

    "sec.android.cover.ledcover",

    "sec.android.desktopmode.uiservice",

    "samsung.desktopsystemui",

    "sec.android.app.desktoplauncher",

    "vcast.mediamanager",

    "samsung.vmmhux",

    "vzw.hss.myverizon",

    "asurion.android.verizon.vms",

    "motricity.verizon.ssodownloadable",

    "vzw.hs.android.modlite",

    "samsung.vvm",

    "vznavigator.[You_Model_Here]",

    "att.dh",

    "att.dtv.shaderemote",

    "att.tv",

    "samsung.attvvm",

    "att.myWireless",

    "asurion.android.protech.att",

    "att.android.attsmartwifi",

    "google.android.apps.docs",

    "google.android.apps.maps",

    "google.android.apps.photos",

    "google.android.apps.tachyon",

    "google.android.apps.wellbeing",

    "google.android.feedback",

    "google.android.gm",

    "google.android.googlequicksearchbox",

    "google.android.inputmethod.latin",

    "google.android.marvin.talkback",

    "google.android.music",

    "google.android.printservice.recommendation",

    "google.android.syncadapters.calendar",

    "google.android.tts",

    "google.android.videos",

    "google.ar.lens",

    "cnn.mobile.android.phone.edgepanel",

    "samsung.android.service.peoplestripe",

    "samsung.android.app.sbrowseredge",

    "samsung.android.app.appsedge",

    "gocro.smartnews.android",

    "synchronoss.dcs.att.r2g",

    "wavemarket.waplauncher",

    "pandora.android",

    "sec.penup",

    "samsung.android.service.livedrawing",

    "linkedin.android",

    "hunge.app",

    "greatbigstory.greatbigstory",

    "android.documentsui",

    "drivemode",

    "samsung.android.app.contacts",

    "samsung.android.calendar",

    "cnn.mobile.android.phone",

    "bleacherreport.android.teamstream",

    "aetherpal.device",

    "google.android.dialer",

    "wb.goog.got.conquest",

    "wb.goog.dcuniverse",

    "innogames.foeandroid",

    "playstudios.popslots",

    "gsn.android.tripeaks",

    "foxnextgames.m3",

    "audible.application",

    "microsoft.skydrive"

]

# Uninstall bloatware packages using ADB

def uninstall_bloatware():

    for package in bloatware_packages:

        command = f"adb shell pm uninstall --user 0 {package}"

        subprocess.run(command, shell=True)

# Run the uninstallation process

uninstall_bloatware()

