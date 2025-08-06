# Android Bloatware Remover

Remove unwanted pre-installed apps from your Android phone without root access. Works with Samsung, Xiaomi, Oppo, Vivo, Realme, Tecno, and OnePlus devices.

## What it does

Your phone comes with tons of apps you never asked for. This tool helps you get rid of them safely using ADB (Android Debug Bridge). No root required.

## Supported phones

- Samsung (One UI)
- Xiaomi, Redmi, POCO (MIUI) 
- Oppo (ColorOS)
- Vivo, iQOO (FunTouch OS)
- Realme (Realme UI)
- Tecno (HiOS)
- OnePlus (OxygenOS)
- Huawei (EMUI/HarmonyOS)
- Honor (Magic UI)
- Motorola (My UX)
- Nothing (Nothing OS)

## Setup

1. **Install ADB**
   - Windows: Download Android SDK Platform Tools, add to PATH
   - Mac: `brew install android-platform-tools`
   - Linux: `sudo apt install android-tools-adb`

2. **Enable USB Debugging on your phone**
   - Settings → About Phone → Tap "Build Number" 7 times
   - Settings → Developer Options → Enable "USB Debugging"

3. **Get the tool**
   ```bash
   git clone https://github.com/AnantMishra01/UIBloatwareRegistry.git
   cd UIBloatwareRegistry
   ```

## How to use

Connect your phone and run:
```bash
python main.py
```

You'll get three options:

1. **Interactive mode** - Shows known bloatware, you pick what to remove
2. **All apps mode** - Lists every app on your phone, you choose what goes
3. **Batch mode** - Removes all known bloatware at once (be careful!)

## Safety features

- **Risk levels**: Apps marked as SAFE, CAUTION, or DANGEROUS
- **Backups**: Creates restore points before removing anything
- **Test mode**: Try it without a phone using `python main.py --test`
- **App names**: Shows "Facebook" instead of cryptic package names

## Example

```
Found 45 applications
==================================================
  1. [SAFE] Facebook
     Package: com.facebook.katana
     
  2. [CAUTION] Gmail  
     Package: com.google.android.gm
     
  3. [DANGEROUS] Phone
     Package: com.android.dialer

Enter your selection: 1,5-8,12
Selected 6 apps for removal
Create backup? (y/n): y
Proceed? (yes): yes
```

## Important stuff

- **Always backup first** - Things can go wrong
- **Test on an old phone** - Don't experiment on your daily driver
- **Some apps come back** - System updates might restore them
- **Factory reset fixes everything** - If you mess up, this will restore all apps

## Contributing

Found a bug? Want to add support for your phone brand? Check out [CONTRIBUTING.md](CONTRIBUTING.md).

## Warning

This tool modifies your phone's software. We're not responsible if something breaks. Use common sense and make backups.

## License

MIT License - do whatever you want with this code.