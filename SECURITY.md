# Security Information

## Windows Defender False Positives

### Why does Windows Defender flag this as a virus?

This is a **false positive** that commonly occurs with PyInstaller executables. Here's why:

1. **PyInstaller behavior**: PyInstaller bundles Python and all dependencies into a single executable, which can trigger heuristic detection
2. **Unsigned executable**: The executable isn't code-signed with a certificate, making Windows more suspicious
3. **ADB interaction**: The tool interacts with ADB (Android Debug Bridge), which antivirus software may flag as suspicious
4. **New executable**: Windows Defender is more likely to flag new, uncommon executables

### Is it actually safe?

**Yes, it's completely safe.** Here's how you can verify:

1. **Source code is open**: All source code is available in this repository for inspection
2. **Build process is transparent**: GitHub Actions builds are public and auditable
3. **No network activity**: The tool only communicates with your connected Android device via ADB
4. **No system modifications**: Only removes apps you explicitly select

### How to use safely

#### Option 1: Add Windows Defender Exception
1. Open Windows Security
2. Go to "Virus & threat protection"
3. Click "Manage settings" under "Virus & threat protection settings"
4. Click "Add or remove exclusions"
5. Add the downloaded executable file

#### Option 2: Use Python Source (Recommended for paranoid users)
Instead of the executable, run from source:
```bash
git clone https://github.com/PixelCode01/UIBloatwareRegistry.git
cd UIBloatwareRegistry
python main.py
```

#### Option 3: Build Your Own Executable
```bash
git clone https://github.com/PixelCode01/UIBloatwareRegistry.git
cd UIBloatwareRegistry
pip install pyinstaller
python build_spec.py
pyinstaller android-bloatware-remover.spec
```

### Verification Steps

1. **Check file hash**: Compare with hashes provided in releases
2. **Scan with multiple engines**: Use VirusTotal.com to scan with 60+ antivirus engines
3. **Review source code**: Inspect the code before running
4. **Test in VM**: Run in a virtual machine first if concerned

## Reporting Security Issues

If you find a legitimate security issue, please:

1. **Do NOT** open a public issue
2. Email security concerns to the repository owner
3. Provide detailed information about the vulnerability
4. Allow time for the issue to be addressed before public disclosure

## Code Signing

We are working on implementing code signing to reduce false positives. This requires:
- Purchasing a code signing certificate
- Setting up automated signing in the build process
- Establishing trust with certificate authorities

## Best Practices for Users

1. **Always download from official releases**: Only download from GitHub releases page
2. **Verify checksums**: Compare file hashes when provided
3. **Use test mode first**: Run with `--test` flag to verify functionality
4. **Keep backups**: Always backup your device before removing apps
5. **Review what you're removing**: Understand each package before removal

## Technical Details

### What the tool does:
- Connects to Android devices via ADB
- Lists installed packages
- Removes selected packages using `adb shell pm uninstall`
- Creates backup files locally
- Logs operations for troubleshooting

### What the tool does NOT do:
- Access the internet (except for ADB communication)
- Modify system files on your computer
- Install anything on your computer
- Send data to external servers
- Access personal files or data

### ADB Commands Used:
```bash
adb devices                           # List connected devices
adb shell getprop ro.product.brand    # Get device brand
adb shell pm list packages            # List installed packages
adb shell pm uninstall --user 0 <pkg> # Remove package
```

All commands are standard ADB operations used by Android developers worldwide.