# Contributing to UIBloatwareRegistry

Thank you for considering contributing to UIBloatwareRegistry! We appreciate your interest in making this repository better. This guide will help you contribute safely and effectively.

## Table of Contents

- [Quick Start](#quick-start)
- [How to Identify Bloatware Packages](#how-to-identify-bloatware-packages)
- [How to Test Package Removal](#how-to-test-package-removal)
- [Risk Level Guidelines](#risk-level-guidelines)
- [Adding New Packages](#adding-new-packages)
- [Submitting Contributions](#submitting-contributions)
- [Code Guidelines](#code-guidelines)
- [Issue Reporting](#issue-reporting)
- [License](#license)

## Quick Start

We've made contributing easier! Use our contribution tool:

```bash
python contribute.py
```

This interactive tool will guide you through adding new packages to the registry.

### What's New?

#### Before (Old System)
To add a new package, you needed to:
1. Edit the brand's Python file (`Samsung/samsung_remover.py`)
2. Edit the brand's Shell script (`Samsung/samsung_remover.sh`)
3. Edit the brand's Markdown file (`Samsung/samsung-bloatware-list.md`)
4. Ensure consistency across all three files
5. Know Python, Shell, and Markdown syntax

#### After (New System)
Now you can:
1. Run `python contribute.py` (interactive tool)
2. OR edit `packages_registry.json` directly
3. That's it! One source of truth for all packages

### Contributing Methods

#### Method 1: Interactive Tool (Recommended)

```bash
# Run the contribution tool
python contribute.py
```

The tool will guide you through:
- Selecting brand and category
- Entering package information
- Validating risk levels
- Saving to the registry

#### Method 2: Command Line

```bash
# Add a package directly
python contribute.py add \
  --brand samsung \
  --category bixby \
  --package com.samsung.android.bixby.test \
  --description "Bixby Test Service" \
  --risk safe

# Search for packages
python contribute.py search --query "bixby"

# Remove a package
python contribute.py remove --brand samsung --package com.example.package
```

#### Method 3: Manual JSON Editing

Edit `packages_registry.json` directly:

```json
{
  "brands": {
    "samsung": {
      "name": "Samsung",
      "categories": {
        "bixby": {
          "name": "Bixby Services",
          "description": "Samsung's virtual assistant",
          "packages": [
            {
              "name": "com.samsung.android.bixby.agent",
              "description": "Bixby Voice Assistant",
              "risk": "safe"
            }
          ]
        }
      }
    }
  }
}
```

## How to Identify Bloatware Packages

### Step 1: List All Packages on Your Device

Connect your device via ADB and run:

```bash
adb shell pm list packages
```

### Step 2: Get Package Details

To understand what a package does:

```bash
# Get app name
adb shell pm dump <package.name> | grep -i "label"

# Check if it's a system app
adb shell pm list packages -s | grep <package.name>

# See the package path
adb shell pm path <package.name>
```

### Step 3: Research the Package

- Search the package name online
- Check XDA forums and Reddit r/Android
- Look for the app in the Play Store
- Review similar bloatware lists

### Safety Checklist

**DO identify packages that are:**
- Manufacturer-specific apps you don't use
- Carrier-installed apps
- Duplicate apps (when alternatives are available)
- Promotional or shopping apps
- OEM assistants you don't use

**DO NOT identify packages that are:**
- Core system services
- Android framework components
- Google Play Services (unless you know what you're doing)
- Security or authentication services you use

## How to Test Package Removal

### Testing Safely

1. **Use Test Mode First**:
   ```bash
   python main.py --test
   ```

2. **Remove for Current User Only**:
   ```bash
   adb shell pm uninstall --user 0 <package.name>
   ```
   This doesn't completely remove the package - it can be restored!

3. **Test Device Functionality**:
   - Make/receive calls
   - Send/receive SMS
   - Use camera
   - Connect to WiFi
   - Use fingerprint/face unlock
   - Test any features related to the removed package

4. **Restore if Needed**:
   ```bash
   adb shell cmd package install-existing <package.name>
   ```

### Test Duration

- Test for at least **24-48 hours** after removal
- Restart your device during testing
- Try various scenarios related to the removed package

## Risk Level Guidelines

Choose the appropriate risk level for each package:

### Safe
**Definition**: Can be removed without affecting system functionality

**Criteria**:
- Optional apps (games, shopping, news)
- Duplicate functionality (manufacturer apps when Google alternatives exist)
- Services you don't use (Bixby if you don't use it)
- Carrier bloatware

**Examples**:
- `com.samsung.android.game.gamehome` - Game Launcher
- `com.amazon.mShop.android.shopping` - Amazon Shopping
- `com.netflix.mediaclient` - Netflix (pre-installed)

### Caution
**Definition**: May affect some functionality, but system remains stable

**Criteria**:
- Default apps with system integration (browser, messaging)
- Apps that other apps might depend on
- Features that some users rely on

**Examples**:
- `com.sec.android.app.sbrowser` - Samsung Internet
- `com.samsung.android.messaging` - Samsung Messages
- `com.google.android.apps.maps` - Google Maps

### Dangerous
**Definition**: May cause system instability, boot loops, or critical feature loss

**Criteria**:
- Core system services
- Authentication services
- Payment systems
- Device admin apps
- System frameworks

**Examples**:
- `com.samsung.android.spay` - Samsung Pay
- `com.google.android.gms` - Google Play Services
- `com.android.systemui` - System UI

### Unknown
**Definition**: Not yet tested or categorized

**Usage**: Temporary classification until proper testing is done

## Adding New Packages

### Using the Contribution Tool (Recommended)

```bash
python contribute.py
```

Follow the interactive prompts to add packages safely.

### Manual Method

1. Edit `packages_registry.json`
2. Add your package under the appropriate brand and category:

```json
{
  "name": "com.example.bloatware",
  "description": "Example Bloatware App",
  "risk": "safe"
}
```

3. Test your changes locally
4. Submit a pull request

### Required Information

When adding a package, provide:

1. **Package Name**: Full package identifier (e.g., `com.samsung.android.app.example`)
2. **Description**: Clear, concise description (e.g., "Samsung Example App")
3. **Risk Level**: Based on guidelines above (`safe`, `caution`, `dangerous`)
4. **Category**: Appropriate category for the package
5. **Testing Evidence**: Brief description of how you tested it

### Risk Tier Rationale Template

When proposing a risk level, explain your reasoning:

```
**Package**: com.example.app
**Proposed Risk**: safe/caution/dangerous
**Rationale**:
- Tested removal on [Device Model, Android Version]
- Observed behavior: [What happened after removal]
- Affects: [List affected features, or "No issues found"]
- Restore test: [Yes/No - was restore successful?]
- Testing duration: [How long you tested]
- Additional context: [Any other relevant information]
```

## Submitting Contributions

1. **Fork the repository** on GitHub

2. **Create a new branch** with a descriptive name:
   ```bash
   git checkout -b add-samsung-game-launcher
   ```

3. **Make your changes** following the guidelines above

4. **Test thoroughly** using test mode and actual removal

5. **Commit with a clear message**:
   ```bash
   git commit -m "add: Samsung Game Launcher to safe removal list
   
   - Package: com.samsung.android.game.gamehome
   - Risk: safe
   - Tested on Galaxy S21, Android 13
   - No issues observed after 48h testing"
   ```

6. **Push your branch**:
   ```bash
   git push origin add-samsung-game-launcher
   ```

7. **Submit a pull request** using our PR template

## Code Guidelines

- Follow consistent code formatting and style
- Use meaningful variable and function names
- Include appropriate comments for clarity
- Write clear and concise commit messages
- Test your changes before submitting

## Issue Reporting

### For Bugs or Problems

Use the **"Removal Problem Report"** issue template and include:
- Device model and Android version
- Package that caused the issue
- Symptoms observed
- Steps to reproduce
- Whether you were able to restore functionality

### For New Package Entries

Use the **"New Package Entry"** issue template

### For Risk Level Updates

Use the **"Update Risk Level"** issue template if you have evidence that a package's risk level should change

## API for Developers

If you're integrating with the registry programmatically:

```python
from core.package_registry import PackageRegistry

# Initialize registry
registry = PackageRegistry()

# Get all brands
brands = registry.get_brands()

# Get packages for a brand
packages = registry.get_packages_for_brand('samsung')

# Get specific package info
info = registry.get_package_info('samsung', 'com.samsung.android.bixby.agent')

# Add a package
registry.add_package('samsung', 'bixby', {
    'name': 'com.test.app',
    'description': 'Test App',
    'risk': 'safe'
})

# Save changes
registry.save_registry()
```

## Troubleshooting

### "Package already exists"
```bash
python contribute.py search --query "package-name"
# Check if it's already in the registry
```

### "Invalid JSON"
```bash
# Validate your JSON
python -m json.tool packages_registry.json
```

### "Permission denied"
```bash
# Make contribute.py executable
chmod +x contribute.py
```

## Best Practices

1. **Always test before adding**
   - Use real device or test mode
   - Verify functionality
   - Test recovery

2. **Use descriptive information**
   - Clear package descriptions
   - Accurate risk levels
   - Proper categorization

3. **Document your testing**
   - Device model and Android version
   - Features tested
   - Issues encountered

4. **Follow PR template**
   - Complete all sections
   - Provide evidence
   - Link related issues

## FAQ

**Q: Do I need to know Python?**
A: No! Use the interactive tool or edit JSON directly.

**Q: Can I still edit the .py files?**
A: Yes, but it's not recommended. Use the registry instead.

**Q: Will old .md files be updated?**
A: They may be auto-generated from the registry in the future.

**Q: How do I add a new brand?**
A: Use `python contribute.py` and select "Add a new brand"

**Q: What if I make a mistake?**
A: Git version control keeps everything safe. Just submit a correction PR!

## Support

- Read this contribution guide thoroughly
- Start a [Discussion](https://github.com/PixelCode01/UIBloatwareRegistry/discussions)
- Report an [Issue](https://github.com/PixelCode01/UIBloatwareRegistry/issues)

## License

By contributing to the UIBloatwareRegistry repository, you agree that your contributions will be licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

We appreciate your contributions and look forward to building a valuable resource for managing Android bloatware together!

**Happy Contributing!**

