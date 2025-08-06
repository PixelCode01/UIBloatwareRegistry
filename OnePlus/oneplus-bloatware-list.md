# OnePlus Bloatware Package List

This document contains a comprehensive list of bloatware packages found on OnePlus devices running OxygenOS. Each package is categorized by risk level to help you make informed removal decisions.

## Risk Levels
- **SAFE**: Can be removed without affecting core functionality
- **CAUTION**: May affect some features, remove with care
- **DANGEROUS**: Critical system components, removal may cause instability

## OnePlus System Apps

### Safe to Remove
- `com.oneplus.account` - OnePlus Account service
- `com.oneplus.backuprestore` - OnePlus Clone Phone
- `com.oneplus.brickmode` - Brick mode service
- `com.oneplus.calculator` - OnePlus Calculator
- `com.oneplus.camera` - OnePlus Camera (if using alternative)
- `com.oneplus.card` - OnePlus Card service
- `com.oneplus.cloud` - OnePlus Cloud storage
- `com.oneplus.compass` - Compass application
- `com.oneplus.deskclock` - Clock and alarm app
- `com.oneplus.filemanager` - OnePlus File Manager
- `com.oneplus.gallery` - OnePlus Gallery
- `com.oneplus.gamespace` - Game Space
- `com.oneplus.iconpack.circle` - Circle icon pack
- `com.oneplus.iconpack.square` - Square icon pack
- `com.oneplus.market` - OnePlus Store
- `com.oneplus.note` - OnePlus Notes
- `com.oneplus.opsocialnetwork` - OnePlus Community
- `com.oneplus.screenshot` - Screenshot service
- `com.oneplus.skin` - OnePlus themes
- `com.oneplus.soundrecorder` - Sound recorder
- `com.oneplus.weather` - OnePlus Weather
- `com.oneplus.widget` - OnePlus widgets
- `com.oneplus.worklife` - Work Life Balance

### Use Caution
- `com.oneplus.contacts` - OnePlus Contacts
- `com.oneplus.dialer` - OnePlus Phone app
- `com.oneplus.launcher` - OnePlus Launcher
- `com.oneplus.mms` - OnePlus Messages
- `com.oneplus.music` - OnePlus Music player
- `com.oneplus.setupwizard` - Setup wizard
- `com.oneplus.systemui` - System UI components

### Dangerous to Remove
- `com.oneplus.framework` - OnePlus framework
- `com.oneplus.opbugreportlite` - Bug reporting service
- `com.oneplus.security` - Security framework

## OxygenOS System Components

### Safe to Remove
- `net.oneplus.commonlogtool` - Common log tool
- `net.oneplus.odm` - ODM service
- `net.oneplus.oemtcma` - OEM TCMA service
- `net.oneplus.push` - OnePlus push service
- `net.oneplus.weather` - Weather service

### Use Caution
- `net.oneplus.launcher` - OxygenOS Launcher
- `net.oneplus.opsystemhelper` - System helper

### Dangerous to Remove
- `net.oneplus.opdiagnose` - System diagnostics

## Google Apps Bloatware

### Safe to Remove
- `com.google.android.apps.docs` - Google Drive
- `com.google.android.apps.photos` - Google Photos
- `com.google.android.apps.youtube.music` - YouTube Music
- `com.google.android.music` - Google Play Music
- `com.google.android.videos` - Google Play Movies
- `com.google.android.youtube` - YouTube
- `com.google.android.keep` - Google Keep
- `com.google.android.apps.tachyon` - Google Duo
- `com.google.ar.lens` - Google Lens
- `com.google.android.feedback` - Google Feedback

### Use Caution
- `com.google.android.apps.maps` - Google Maps
- `com.google.android.gm` - Gmail
- `com.google.android.googlequicksearchbox` - Google Search
- `com.google.android.inputmethod.latin` - Gboard
- `com.google.android.calendar` - Google Calendar

### Dangerous to Remove
- `com.google.android.gms` - Google Play Services
- `com.google.android.gsf` - Google Services Framework
- `com.google.android.tts` - Text-to-speech

## Netflix and Third-Party Apps

### Safe to Remove
- `com.netflix.mediaclient` - Netflix (if pre-installed)
- `com.netflix.partner.activation` - Netflix activation
- `com.facebook.katana` - Facebook
- `com.facebook.orca` - Facebook Messenger
- `com.facebook.services` - Facebook Services
- `com.facebook.system` - Facebook System
- `com.instagram.android` - Instagram
- `com.spotify.music` - Spotify

## Qualcomm Components

### Safe to Remove
- `com.qualcomm.qti.workloadclassifier` - Workload classifier
- `com.qualcomm.qti.poweroffalarm` - Power off alarm
- `com.qualcomm.qti.devicestatisticsservice` - Device statistics

### Use Caution
- `com.qualcomm.qti.callenhancement` - Call enhancement
- `com.qualcomm.qti.callfeaturessetting` - Call features
- `com.qualcomm.qti.dynamicddsservice` - Dynamic DDS service
- `com.qualcomm.qti.simsettings` - SIM settings

### Dangerous to Remove
- `com.qualcomm.qti.ims` - IMS service for VoLTE
- `com.qualcomm.qti.telephonyservice` - Telephony service

## Android System Bloatware

### Safe to Remove
- `com.android.bips` - Built-in Print Service
- `com.android.bookmarkprovider` - Bookmark provider
- `com.android.printspooler` - Print spooler
- `com.android.wallpaperbackup` - Wallpaper backup
- `com.android.wallpapercropper` - Wallpaper cropper

### Use Caution
- `com.android.chrome` - Chrome browser
- `com.android.mms.service` - MMS service

### Dangerous to Remove
- `com.android.cellbroadcastreceiver` - Emergency alerts
- `com.android.emergency` - Emergency information

## Removal Notes

- Always create a backup before removing any packages
- Test removals on a non-primary device first
- Some apps may reinstall after OxygenOS updates
- Factory reset will restore all removed applications
- Use the interactive removal mode for safer operation
- OnePlus devices may have carrier-specific bloatware
- OxygenOS updates may restore some removed apps