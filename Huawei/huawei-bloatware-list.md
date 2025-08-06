# Huawei Bloatware Package List

This document contains a comprehensive list of bloatware packages found on Huawei devices running EMUI/HarmonyOS. Each package is categorized by risk level to help you make informed removal decisions.

## Risk Levels
- **SAFE**: Can be removed without affecting core functionality
- **CAUTION**: May affect some features, remove with care
- **DANGEROUS**: Critical system components, removal may cause instability

## Huawei System Apps

### Safe to Remove
- `com.huawei.appmarket` - Huawei AppGallery
- `com.huawei.browser` - Huawei Browser
- `com.huawei.calculator` - Huawei Calculator
- `com.huawei.camera` - Huawei Camera (if using alternative)
- `com.huawei.compass` - Compass app
- `com.huawei.desktop.explorer` - File Manager
- `com.huawei.gameassistant` - Game Assistant
- `com.huawei.gamebox` - Game Center
- `com.huawei.health` - Huawei Health
- `com.huawei.himovie` - Huawei Video
- `com.huawei.hmusic` - Huawei Music
- `com.huawei.hwid` - Huawei ID
- `com.huawei.magazine` - Magazine Unlock
- `com.huawei.mirror` - Mirror app
- `com.huawei.notepad` - Notepad
- `com.huawei.parentcontrol` - Parental Control
- `com.huawei.phoneservice` - Phone Service
- `com.huawei.scanner` - AI Scanner
- `com.huawei.screenrecorder` - Screen Recorder
- `com.huawei.search` - Huawei Search
- `com.huawei.tips` - Tips app
- `com.huawei.translator` - Translator
- `com.huawei.vassistant` - Voice Assistant
- `com.huawei.wallet` - Huawei Wallet
- `com.huawei.weather` - Weather app
- `com.huawei.works` - Docs app

### Use Caution
- `com.huawei.android.launcher` - Huawei Launcher
- `com.huawei.contacts` - Contacts app
- `com.huawei.deskclock` - Clock app
- `com.huawei.gallery` - Gallery app
- `com.huawei.mms` - Messages app
- `com.huawei.phoneservice` - Phone app
- `com.huawei.systemmanager` - Phone Manager

### Dangerous to Remove
- `com.huawei.android.hwaps` - Huawei Mobile Services
- `com.huawei.hwid.core` - Huawei ID Core
- `com.huawei.systemserver` - System Server

## EMUI/HarmonyOS Components

### Safe to Remove
- `com.huawei.android.chr` - User Experience Program
- `com.huawei.android.hsf` - Huawei Service Framework
- `com.huawei.android.karaoke` - Karaoke feature
- `com.huawei.android.thememanager` - Theme Manager
- `com.huawei.bd` - Big Data service
- `com.huawei.hiaction` - HiAction automation
- `com.huawei.hicard` - HiCard service
- `com.huawei.hifolder` - HiFolder
- `com.huawei.hitouch` - HiTouch
- `com.huawei.livewallpaper.paradise` - Live wallpapers
- `com.huawei.motionservice` - Motion service
- `com.huawei.nearby` - Huawei Share
- `com.huawei.stylus` - Stylus support

### Use Caution
- `com.huawei.android.launcher` - EMUI Launcher
- `com.huawei.android.internal.app` - Internal apps
- `com.huawei.fastapp` - Quick App Center
- `com.huawei.intelligent` - HiAssistant
- `com.huawei.powergenie` - Power Genie

### Dangerous to Remove
- `com.huawei.android.pushagent` - Push service
- `com.huawei.hwid` - Huawei ID (required for many features)
- `com.huawei.systemmanager` - System Manager

## Google Services (if present)

### Safe to Remove
- `com.google.android.apps.docs` - Google Drive
- `com.google.android.apps.photos` - Google Photos
- `com.google.android.music` - Google Play Music
- `com.google.android.videos` - Google Play Movies
- `com.google.android.youtube` - YouTube

### Use Caution
- `com.google.android.gm` - Gmail
- `com.google.android.googlequicksearchbox` - Google Search

### Dangerous to Remove
- `com.google.android.gms` - Google Play Services (if present)

## Third-Party Bloatware

### Safe to Remove
- `com.facebook.katana` - Facebook
- `com.facebook.orca` - Facebook Messenger
- `com.instagram.android` - Instagram
- `com.netflix.mediaclient` - Netflix
- `com.spotify.music` - Spotify
- `com.twitter.android` - Twitter
- `com.whatsapp` - WhatsApp (if pre-installed)

## Carrier Bloatware

### Safe to Remove
- Various carrier-specific apps depending on region
- Carrier billing apps
- Carrier customer service apps
- Carrier TV/streaming apps

## Removal Notes

- Always create a backup before removing any packages
- Test removals on a non-primary device first
- Some apps may reinstall after EMUI/HarmonyOS updates
- Factory reset will restore all removed applications
- Use the interactive removal mode for safer operation
- Huawei devices without Google services may have different package lists
- HarmonyOS devices may have additional Huawei-specific packages