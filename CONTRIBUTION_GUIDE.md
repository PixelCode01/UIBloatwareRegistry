# Package Contribution Guide

## Overview

The new contribution system simplifies adding bloatware packages to the registry. Instead of editing multiple files (Python, Shell scripts, Markdown), you can now use a single tool or edit one JSON file.

## What's New?

### ✅ Before (Old System)
To add a new package, you needed to:
1. Edit the brand's Python file (`Samsung/samsung_remover.py`)
2. Edit the brand's Shell script (`Samsung/samsung_remover.sh`)
3. Edit the brand's Markdown file (`Samsung/samsung-bloatware-list.md`)
4. Ensure consistency across all three files
5. Know Python, Shell, and Markdown syntax

### 🎉 After (New System)
Now you can:
1. Run `python contribute.py` (interactive tool)
2. OR edit `packages_registry.json` directly
3. That's it! One source of truth for all packages

## Quick Start

### Method 1: Interactive Tool (Recommended)

```bash
# Run the contribution tool
python contribute.py
```

The tool will guide you through:
- Selecting brand and category
- Entering package information
- Validating risk levels
- Saving to the registry

### Method 2: Command Line

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

### Method 3: Manual JSON Editing

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

## File Structure

### New System
```
UIBloatwareRegistry/
├── packages_registry.json      # ⭐ Single source of truth
├── contribute.py               # ⭐ Contribution tool
├── core/
│   └── package_registry.py     # ⭐ Registry manager
├── .github/
│   ├── ISSUE_TEMPLATE/         # ⭐ Issue templates
│   │   ├── new_package_entry.yml
│   │   ├── update_risk_level.yml
│   │   └── removal_problem_report.yml
│   └── pull_request_template.md # ⭐ PR template
└── CONTRIBUTING.md             # ⭐ Enhanced guidelines
```

### Old System (Deprecated)
```
UIBloatwareRegistry/
├── Samsung/
│   ├── samsung_remover.py      # ⚠️ Will use registry
│   ├── samsung_remover.sh      # ⚠️ May be deprecated
│   └── samsung-bloatware-list.md # ⚠️ Generated from registry
```

## Risk Level Guidelines

### 🟢 SAFE
- No system functionality affected
- Can be removed without concerns
- Examples: Bixby, Samsung Cloud, carrier apps

### 🟡 CAUTION
- May affect some functionality
- Remove only if you don't use it
- Examples: Default SMS app, Browser

### 🔴 DANGEROUS
- May cause system instability
- NOT recommended for average users
- Examples: Google Play Services, System launcher

### ⚪ UNKNOWN
- Not yet tested or categorized
- Research before removing
- Treat as DANGEROUS until proven otherwise

## Testing Workflow

1. **Identify Package**
   ```bash
   adb shell pm list packages | grep keyword
   ```

2. **Test in Test Mode**
   ```bash
   python main.py --test
   ```

3. **Remove for Current User**
   ```bash
   adb shell pm uninstall --user 0 com.example.package
   ```

4. **Verify Device Functionality**
   - Basic features working?
   - Any crashes or errors?
   - Can you restore it?

5. **Add to Registry**
   ```bash
   python contribute.py
   ```

6. **Submit PR**
   - Use the PR template
   - Document testing results
   - Include device info

## Contribution Tool Features

### Interactive Mode
```bash
python contribute.py
```

Features:
- ✅ Add new packages
- ✅ Update existing packages
- ✅ Remove packages
- ✅ Search packages
- ✅ View brands and categories
- ✅ Risk level guidelines
- ✅ Input validation
- ✅ Duplicate detection

### CLI Mode
```bash
# Quick add
python contribute.py add --brand samsung --category bixby \
  --package com.test.app --description "Test" --risk safe

# Search across brands
python contribute.py search --query "google"

# Remove package
python contribute.py remove --brand samsung --package com.test.app
```

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

## Migration Notes

### For Contributors
- Old workflow still works (for now)
- New workflow is preferred
- Both will be maintained during transition
- Use `contribute.py` for all new contributions

### For Maintainers
- Registry is the source of truth
- Python files will load from registry
- MD files can be auto-generated
- Shell scripts may be deprecated

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

## Resources

- [CONTRIBUTING.md](../CONTRIBUTING.md) - Full contribution guide
- [README.md](../README.md) - Project overview
- [Issue Templates](.github/ISSUE_TEMPLATE/) - Report issues
- [PR Template](.github/pull_request_template.md) - Submit changes

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

- 📖 Read [CONTRIBUTING.md](../CONTRIBUTING.md)
- 💬 Start a [Discussion](https://github.com/PixelCode01/UIBloatwareRegistry/discussions)
- 🐛 Report an [Issue](https://github.com/PixelCode01/UIBloatwareRegistry/issues)

---

**Happy Contributing! 🎉**
