# Android Bloatware Remover

Remove unwanted pre-installed apps from your Android phone without root access. Works with Samsung, Xiaomi, Oppo, Vivo, Realme, Tecno, OnePlus, Huawei, Honor, Motorola, and Nothing devices.

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

## Quick Download

**Download standalone executable** - No Python installation required!

1. Go to [Releases](https://github.com/PixelCode01/UIBloatwareRegistry/releases)
2. Download for your system:
   - **Windows**: `android-bloatware-remover-windows.exe`
   - **Linux**: `android-bloatware-remover-linux`
   - **Mac**: `android-bloatware-remover-macos`
3. Run the executable directly!

**Note**: Windows Defender may show a false positive. See [SECURITY.md](SECURITY.md) for details.

## No PC? Use Shizuku!

**Remove bloatware directly on your phone** using Shizuku - No PC required!

1. Install [Shizuku](https://github.com/RikkaApps/Shizuku/releases) on your device
2. Download the shell script for your brand:
   - **Samsung**: `Samsung/samsung_remover.sh`
   - **Xiaomi**: `Xiaomi/xiaomi_remover.sh`
   - **OnePlus**: `OnePlus/oneplus_remover.sh`
   - **Realme**: `Realme/realme_remover.sh`
   - **Oppo**: `Oppo/oppo_remover.sh`
   - **Vivo**: `Vivo/vivo_remover.sh`
   - **Huawei**: `Huawei/huawei_remover.sh`
   - **Honor**: `Honor/honor_remover.sh`
   - **Motorola**: `Motorola/motorola_remover.sh`
   - **Nothing**: `Nothing/nothing_remover.sh`
   - **Tecno**: `Tecno/tecno_remover.sh`
3. Run the script using a Shizuku-compatible terminal
4. Follow the interactive prompts to remove bloatware

See [Honor/SHIZUKU_USAGE.md](Honor/SHIZUKU_USAGE.md) for detailed setup instructions (applies to all brands).

## Manual Setup (Advanced)

1. **Install ADB**
   - Windows: Download Android SDK Platform Tools, add to PATH
   - Mac: `brew install android-platform-tools`
   - Linux: `sudo apt install android-tools-adb`
   - Optional: Set the `ADB_PATH` environment variable to the full path of your `adb` binary if it isn't on PATH.

2. **Enable USB Debugging on your phone**
   - Settings -> About Phone -> Tap "Build Number" 7 times
   - Settings -> Developer Options -> Enable "USB Debugging"

3. **Get the tool**
   ```bash
   git clone https://github.com/PixelCode01/UIBloatwareRegistry.git
   cd UIBloatwareRegistry
   ```

## How to use

### Using Standalone Executable
Just run the downloaded executable:
```bash
# Windows
android-bloatware-remover-windows.exe

# Linux/Mac
./android-bloatware-remover-linux
./android-bloatware-remover-macos
```

> **Tip:** If the executable cannot find `adb`, place the `platform-tools` folder next to the binary or set the `ADB_PATH` environment variable to the full path of `adb`.

### Using Python Source
Connect your phone and run:
```bash
python main.py
```

You'll get four options:

1. **Interactive mode** - Shows known bloatware, you pick what to remove
2. **All apps mode** - Lists every app on your phone, you choose what goes
3. **Manual mode** - Type a package name (`com.android.chrome`) or search by app name (`chrome`)
4. **Batch mode** - Removes all known bloatware at once (be careful!)

### Connecting over Wi-Fi

- Start the tool with Wi-Fi prompts: `python main.py --wifi`
- Provide everything non-interactively with `--wifi-endpoint`, `--wifi-pair`, and `--wifi-code`
- Enable wireless debugging on a cabled device using `python main.py --enable-tcpip`

See [WIFI_ADB_GUIDE.md](WIFI_ADB_GUIDE.md) for a complete walk-through, pairing reminders, and troubleshooting tips.

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

## Export package data

Generate a consolidated JSON file with all bloatware package information from every supported brand:

```bash
python scripts/generate_data_bundle.py
```

This creates `build/data.json` containing:
- All package names, descriptions, and risk levels
- Brand/platform associations
- Category classifications (adware, telemetry, OEM tools)
- Metadata (generation timestamp, package counts)

Use this data for:
- Custom tooling and automation
- Package analysis and research
- Integration with other debloating workflows
- Creating custom removal scripts

## Important stuff

- **Always backup first** - Things can go wrong
- **Test on an old phone** - Don't experiment on your daily driver
- **Some apps come back** - System updates might restore them
- **Factory reset fixes everything** - If you mess up, this will restore all apps

## Contributing

Found a bug? Want to add support for your phone brand? Check out [CONTRIBUTING.md](CONTRIBUTING.md).

## Important Notes

### Windows Defender False Positive
Windows Defender may flag the executable as a virus. This is a **false positive** common with PyInstaller executables. The tool is completely safe - all source code is open and auditable. See [SECURITY.md](SECURITY.md) for details and solutions.

### Safety Warning
This tool modifies your phone's software. We're not responsible if something breaks. Use common sense and make backups.

## License

MIT License - do whatever you want with this code.