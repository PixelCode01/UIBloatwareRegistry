## Description

<!-- Provide a clear and concise description of your changes -->



## Type of Change

<!-- Check all that apply -->

- [ ] 🆕 New package(s) added
- [ ] 🔄 Updated existing package(s)
- [ ] 🗑️ Removed deprecated package(s)
- [ ] 🔧 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🎨 Code style/formatting changes

## Changes Made

<!-- List the specific changes you made -->

### Packages Added/Modified

<!-- If you added or modified packages, list them here -->

| Brand | Package Name | Category | Risk Level | Action |
|-------|--------------|----------|------------|--------|
| Samsung | com.example.package | bixby | safe | Added |
|  |  |  |  |  |

### Other Changes

<!-- List any other changes made -->

- 
- 
- 

## Testing

<!-- Describe how you tested your changes -->

### Testing Environment

- **Device Model(s):** 
- **Android Version(s):** 
- **Testing Method:** <!-- ADB, tool, test mode, etc. -->

### Test Results

<!-- Check all that apply -->

- [ ] ✅ Tested on actual device
- [ ] ✅ Used test mode to verify
- [ ] ✅ Package removal successful
- [ ] ✅ No system instability observed
- [ ] ✅ Affected features documented
- [ ] ✅ Recovery/restoration tested
- [ ] ⚠️ Found issues (documented below)
- [ ] ❌ Not tested yet (explain why)

### Issues Encountered

<!-- If any issues were found during testing, describe them here -->



## Risk Assessment

<!-- For package additions/modifications -->

### Packages with SAFE risk level

- Package: 
  - Reasoning: 
  - Testing: 

### Packages with CAUTION risk level

- Package: 
  - Reasoning: 
  - Affected features: 
  - Testing: 

### Packages with DANGEROUS risk level

- Package: 
  - Reasoning: 
  - Why included: 
  - Warnings: 
  - Testing: 

## Checklist

### General Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own changes
- [ ] I have commented my code where necessary
- [ ] My changes generate no new warnings or errors
- [ ] I have read the [CONTRIBUTING.md](../CONTRIBUTING.md) guide

### For Package Changes

- [ ] Package names are accurate and complete (com.example.package format)
- [ ] Descriptions are clear and user-friendly
- [ ] Risk levels follow the guidelines in CONTRIBUTING.md
- [ ] Categories are appropriate and logical
- [ ] All required metadata is provided (name, description, risk)
- [ ] JSON syntax is valid (no syntax errors)
- [ ] No duplicate packages added

### Testing Checklist

- [ ] Tested package removal on actual device OR used test mode
- [ ] Verified basic device functions still work
- [ ] Documented any affected features or issues
- [ ] Tested package restoration/recovery
- [ ] Multiple devices tested (if possible)

### Documentation Checklist

- [ ] Updated relevant documentation
- [ ] Added comments for complex changes
- [ ] Included examples where helpful
- [ ] Updated README if needed

## Screenshots/Evidence (Optional)

<!-- If applicable, add screenshots or logs to demonstrate your testing -->



## Related Issues

<!-- Link related issues using #issue_number -->

Closes #
Related to #

## Additional Context

<!-- Add any other context about the pull request here -->



## For Maintainers

<!-- Maintainers: Check these before merging -->

- [ ] Code review completed
- [ ] Risk levels verified
- [ ] Testing evidence provided and adequate
- [ ] Documentation updated
- [ ] No conflicts with existing data
- [ ] JSON structure validated
- [ ] Ready to merge

---

**Note for contributors:** Please fill out all relevant sections. Incomplete PRs may be delayed or closed. If you're using the contribution tool (`python contribute.py`), it automatically formats everything correctly!
