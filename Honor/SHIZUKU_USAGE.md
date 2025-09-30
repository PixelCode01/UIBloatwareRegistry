# Honor Bloatware Remover - Shizuku Version

This shell script version is specifically designed for Honor device users who want to remove bloatware using **Shizuku** without needing a PC.

## What is Shizuku?

Shizuku is an Android app that allows you to run ADB commands directly on your device without connecting to a computer. It's perfect for removing bloatware when you don't have access to a PC.

## Prerequisites

1. **Honor device** running Magic UI (any version)
2. **Shizuku app** installed and activated
3. **Terminal app** that supports Shizuku (like Termux or Shizuku's built-in terminal)

## Installation Steps

### Step 1: Install and Setup Shizuku

1. Download **Shizuku** from:
   - [GitHub Releases](https://github.com/RikkaApps/Shizuku/releases)
   - [Google Play Store](https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api)

2. **Enable Developer Options** on your Honor device:
   - Go to Settings -> About Phone
   - Tap "Build Number" 7 times
   - Go back to Settings -> System & Updates -> Developer Options
   - Enable "USB Debugging"

3. **Activate Shizuku**:
   - Connect your device to a PC once (just for Shizuku setup)
   - Enable USB Debugging and authorize the computer
   - Open Shizuku app and follow the setup instructions
   - Once activated, you can disconnect from PC

### Step 2: Download the Script

1. Download the `honor_remover.sh` script to your device
2. Save it to `/sdcard/` or any accessible location

### Step 3: Run the Script

1. Open your terminal app (with Shizuku support)
2. Grant Shizuku permissions to the terminal app
3. Navigate to where you saved the script:
   ```bash
   cd /sdcard/
   ```
4. Make sure the script is executable:
   ```bash
   chmod +x honor_remover.sh
   ```
5. Run the script:
   ```bash
   ./honor_remover.sh
   ```

## Usage Options

The script provides several modes:

### 1. Interactive Removal (Recommended)
- Shows only installed bloatware packages
- Categorizes by risk level (SAFE, CAUTION, DANGEROUS)
- Lets you select specific packages to remove

### 2. Batch Removal
- Removes all SAFE packages automatically
- Creates backup before removal
- Fastest method for maximum bloatware removal

### 3. List All Packages
- Shows every installed package on your device
- Useful for identifying unknown bloatware

### 4. Create Backup Only
- Creates a backup of installed packages
- Recommended before any removal

## Safety Features

- **Automatic Backup**: Creates package list backup before removal
- **Risk Levels**:
   - SAFE: No impact on core functionality
   - CAUTION: May affect some features
   - DANGEROUS: Critical system components
- **Confirmation Prompts**: Prevents accidental removal
- **Detailed Logging**: Shows exactly what was removed

## Package Categories

### SAFE Packages (Recommended for Removal)
- Honor AppGallery
- Honor Browser
- Honor Music/Video
- Game Center
- Various Honor utilities
- Pre-installed social media apps

### CAUTION Packages (Remove with Care)
- Honor Launcher (install alternative first)
- Default Phone/Messages apps
- Gallery app
- Assistant services

### DANGEROUS Packages (DO NOT REMOVE)
- Honor Mobile Services
- System Server
- Core Honor ID services

## Troubleshooting

### Script Won't Run
- Ensure Shizuku is active and has proper permissions
- Check that your terminal app has Shizuku access
- Verify the script file permissions (`chmod +x honor_remover.sh`)

### Packages Won't Remove
- Some system packages may only be disabled, not fully removed
- This is normal behavior for certain core apps
- Check if Shizuku is still active

### Device Issues After Removal
- Restart your device first
- If problems persist, you can reinstall packages from Honor AppGallery
- In extreme cases, factory reset will restore everything

## Recommended Terminal Apps

1. **Termux** (with Shizuku add-on)
2. **Material Terminal** (Shizuku compatible)
3. **Terminal Emulator** (various Shizuku-compatible versions)

## Important Notes

- Always back up your device before removing packages
- Some apps may return after Magic UI updates
- Test on a secondary device first if possible
- Factory reset will restore all removed applications
- This script is specifically for Honor devices with Magic UI

## What Gets Removed

This script targets common Honor bloatware including:
- Pre-installed social media apps (Facebook, Instagram, etc.)
- Honor's duplicate apps (when you have alternatives)
- Unnecessary system utilities
- Regional bloatware apps
- Marketing and data collection services

## Support

If you encounter issues:
1. Check that your Honor device is supported
2. Ensure Shizuku is properly activated
3. Verify you have the necessary permissions
4. Try running individual commands manually first

## Alternative Method (Without Shizuku)

If you have access to a PC with ADB:
1. Use the Python version from the main repository
2. Follow the standard ADB setup instructions
3. Run the interactive Python script

---

**Remember**: Removing system apps can affect device functionality. Always understand what you're removing and create backups first.