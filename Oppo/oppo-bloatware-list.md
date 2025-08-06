# Oppo Bloatware Package List

This document contains a comprehensive list of bloatware packages found on Oppo devices running ColorOS. Each package is categorized by risk level and includes descriptions to help you make informed removal decisions.

## Risk Levels
- **SAFE**: Can be removed without affecting core functionality
- **CAUTION**: May affect some features, remove with care
- **DANGEROUS**: Critical system components, removal may cause instability

## Android System Bloatware

### Safe to Remove
- `com.android.bips` - Built-in Print Service
- `com.android.bookmarkprovider` - Browser bookmark storage
- `com.android.egg` - Android Easter Egg
- `com.android.printspooler` - Mobile printing service
- `com.android.wallpaper.livepicker` - Live wallpaper selector
- `com.android.wallpaperbackup` - Wallpaper backup service
- `com.android.wallpapercropper` - Wallpaper cropping tool
- `com.caf.fmradio` - FM Radio service

### Use Caution
- `com.android.chrome` - Google Chrome browser
- `com.android.mms.service` - SMS/MMS messaging service
- `com.android.providers.calendar` - Calendar data provider
- `com.android.providers.partnerbookmarks` - Chrome bookmarks
- `com.android.providers.userdictionary` - Keyboard dictionary

### Dangerous to Remove
- `com.android.cellbroadcastreceiver` - Emergency alerts system
- `com.android.cellbroadcastreceiver.overlay.common` - Emergency alerts overlay
- `com.android.vpndialogs` - VPN connection dialogs

## ColorOS System Apps

### Safe to Remove
- `com.coloros.aftersalesservice` - After-sales service app
- `com.coloros.childrenspace` - Kids Space mode
- `com.coloros.compass2` - Compass application
- `com.coloros.focusmode` - Focus Mode for productivity
- `com.coloros.gamespace` - Game Center
- `com.coloros.healthcheck` - Device health checker
- `com.coloros.healthservice` - Device health service
- `com.coloros.musiclink` - Music Party sharing
- `com.coloros.safesdkproxy` - Phone Cleaner (contains tracking)
- `com.coloros.screenrecorder` - Screen recording app
- `com.coloros.speechassist` - Voice assistant (Chinese)
- `com.coloros.translate.engine` - Translation service
- `com.coloros.video` - Video player
- `com.coloros.wallpapers` - Wallpaper collection
- `com.coloros.widget.smallweather` - Weather widget

### Use Caution
- `com.coloros.alarmclock` - Alarm and clock app
- `com.coloros.assistantscreen` - Smart Assistant
- `com.coloros.backuprestore` - Clone Phone backup
- `com.coloros.calculator` - Calculator app
- `com.coloros.cloud` - Oppo Cloud storage
- `com.coloros.filemanager` - File Manager
- `com.coloros.floatassistant` - Floating window assistant
- `com.coloros.gallery3d` - Gallery app
- `com.coloros.securepay` - Secure payment service
- `com.coloros.smartsidebar` - Smart Sidebar
- `com.coloros.soundrecorder` - Voice recorder
- `com.coloros.weather.service` - Weather service

## Google Apps Bloatware

### Safe to Remove
- `com.google.android.apps.googleassistant` - Google Assistant
- `com.google.android.apps.nbu.files` - Files by Google
- `com.google.android.apps.nbu.paisa.user` - Google Pay
- `com.google.android.apps.photos` - Google Photos
- `com.google.android.apps.wellbeing` - Digital Wellbeing
- `com.google.android.feedback` - Google Feedback
- `com.google.android.keep` - Google Keep notes
- `com.google.android.music` - Google Play Music
- `com.google.android.projection.gearhead` - Android Auto
- `com.google.android.soundpicker` - Sound picker
- `com.google.android.talk` - Google Talk
- `com.google.android.videos` - Google Play Movies
- `com.google.android.vr.home` - Google VR Services
- `com.google.android.youtube` - YouTube
- `com.google.ar.core` - Google ARCore
- `com.google.ar.lens` - Google Lens
- `com.google.vr.vrcore` - Google VR Core

### Use Caution
- `com.google.android.apps.maps` - Google Maps
- `com.google.android.apps.messaging` - Google Messages
- `com.google.android.calendar` - Google Calendar
- `com.google.android.documentsui` - Files app
- `com.google.android.gm` - Gmail
- `com.google.android.googlequicksearchbox` - Google Search
- `com.google.android.inputmethod.latin` - Gboard keyboard
- `com.google.android.contacts` - Google Contacts

### Dangerous to Remove
- `com.google.android.marvin.talkback` - Accessibility service
- `com.google.android.tts` - Text-to-speech engine

## Hardware-Specific Bloatware

### Qualcomm Components (Safe to Remove)
- `com.qualcomm.qti.optinoverlay` - Qualcomm opt-in overlay
- `com.qualcomm.qti.simcontacts` - SIM contact management

### Qualcomm Components (Dangerous)
- `com.qualcomm.qti.ims` - IMS service for calls
- `com.qualcomm.qti.telephonyservice` - Telephony service

### MediaTek Components (Use Caution)
- `com.mediatek.atci.service` - AT command interface
- `com.mediatek.connectivity` - Connectivity service
- `com.mediatek.dm` - Device management
- `com.mediatek.mtklogger` - System logger
- `com.mediatek.omacp` - OMA client provisioning
- `com.mediatek.simcontacts` - SIM contacts
- `com.mediatek.selftest` - Hardware self-test
- `com.mediatek.settings.ext` - Settings extensions
- `com.mediatek.voicecommand` - Voice command service

## Removal Notes

- Always create a backup before removing any packages
- Test removals on a non-primary device first
- Some apps may reinstall after system updates
- Factory reset will restore all removed applications
- Use the interactive removal mode for safer operation
