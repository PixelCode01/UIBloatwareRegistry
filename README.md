# UIBloatwareRegistry

A comprehensive Android bloatware removal tool that helps you identify and safely remove pre-installed applications that affect device performance and privacy without root.

## Features

- **Automatic Device Detection**: Detects your device brand and loads appropriate removal scripts
- **Interactive Mode**: Choose exactly which apps to remove with safety warnings
- **All Apps Listing**: View and select from all installed applications on your device
- **Risk Assessment**: Each package is categorized as safe, caution, or dangerous
- **App Name Resolution**: Shows human-readable app names alongside package names
- **Backup System**: Create backups before removal for easy restoration
- **Logging**: Detailed logs of all operations for troubleshooting
- **Professional Interface**: Clean, user-friendly command-line interface

## Supported Brands

Currently supported:
- **Samsung** - Galaxy series devices with One UI
- **Xiaomi** - Mi, Redmi, and POCO devices with MIUI
- **Oppo** - Oppo devices with ColorOS
- **Vivo** - Vivo and iQOO devices with FunTouch OS
- **Realme** - Realme devices with Realme UI
- **Tecno** - Tecno devices with HiOS
- **OnePlus** - OnePlus devices with OxygenOS

Coming soon:
- Huawei (EMUI/HarmonyOS)
- Honor (Magic UI)
- Motorola (My UX)
- Nothing (Nothing OS)

## Prerequisites

- **Python 3.6+** installed on your computer
- **ADB (Android Debug Bridge)** installed and added to PATH
- **USB cable** to connect your device
- **Android device** with USB debugging enabled

### Installing ADB

**Windows:**
1. Download Android SDK Platform Tools
2. Extract and add to PATH environment variable

**macOS:**
```bash
brew install android-platform-tools
```

**Linux:**
```bash
sudo apt install android-tools-adb  # Ubuntu/Debian
sudo pacman -S android-tools        # Arch Linux
```

### Enable USB Debugging

1. Go to Settings > About Phone
2. Tap "Build Number" 7 times to enable Developer Options
3. Go to Settings > Developer Options
4. Enable "USB Debugging"

## Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/AnantMishra01/UIBloatwareRegistry.git
cd UIBloatwareRegistry
```

2. **Connect your device and run:**
```bash
python main.py
```

3. **Or test without a device:**
```bash
python main.py --test
```

The tool will automatically detect your device brand and guide you through the removal process.

## Usage Modes

### Interactive Mode (Recommended)
- Review each package before removal
- See risk levels and descriptions
- Create backups automatically
- Perfect for beginners

### All Apps Mode (Advanced)
- Lists all installed applications on device
- Shows app names and package names
- Select any app for removal
- Includes risk assessment for known bloatware
- Full control over what gets removed

### Batch Mode (Expert)
- Remove all configured packages at once
- Faster for experienced users
- Use with extreme caution

### Test Mode
- Run without ADB or connected device
- Perfect for testing and development
- No actual changes are made
- Use `--test` or `-t` flag

## Safety Information

**Risk Levels:**
- **SAFE**: Can be removed without issues
- **CAUTION**: May affect some functionality
- **DANGEROUS**: Could cause system instability

**Important Notes:**
- Always create backups before removal
- Test on a non-primary device first
- Use test mode to preview changes without risk
- Some apps may reinstall after system updates
- Factory reset will restore all removed apps

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- Add support for new device brands
- Update package lists with new bloatware
- Improve safety classifications
- Report bugs and issues
- Enhance documentation

## Disclaimer

Removing system applications may affect device functionality. Use this tool at your own risk. Always create backups and understand what each package does before removal. The developers are not responsible for any damage to your device.

## License

This project is licensed under the [MIT License](LICENSE).