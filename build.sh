#!/bin/bash
# Local build script for testing

echo "Android Bloatware Remover - Local Build Script"
echo "================================================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed"
    exit 1
fi

# Install PyInstaller if not present
echo "Installing PyInstaller..."
pip3 install pyinstaller

# Create spec file
echo "Creating PyInstaller spec file..."
cat > android-bloatware-remover.spec << 'EOF'
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collect all brand directories and their contents
brand_dirs = ['Samsung', 'Xiaomi', 'Oppo', 'Vivo', 'Realme', 'Tecno', 'OnePlus', 'Huawei', 'Honor', 'Motorola', 'Nothing']
datas = []

# Add brand directories
for brand in brand_dirs:
    datas.append((f'{brand}/*.md', f'{brand}/'))
    datas.append((f'{brand}/*.py', f'{brand}/'))

# Add core module
datas.append(('core/*.py', 'core/'))

# Add other files
datas.append(('README.md', '.'))
datas.append(('LICENSE', '.'))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'Samsung.samsung_remover',
        'Xiaomi.xiaomi_remover', 
        'Oppo.oppo_remover',
        'Vivo.vivo_remover',
        'Realme.realme_remover',
        'Tecno.tecno_remover',
        'OnePlus.oneplus_remover',
        'Huawei.huawei_remover',
        'Honor.honor_remover',
        'Motorola.motorola_remover',
        'Nothing.nothing_remover',
        'core.bloatware_remover'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='android-bloatware-remover',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
EOF

# Build executable
echo "Building executable..."
pyinstaller android-bloatware-remover.spec --clean

if [ $? -eq 0 ]; then
    echo "✓ Build completed successfully!"
    echo "Executable location: dist/android-bloatware-remover"
    
    # Test the executable
    echo "Testing executable..."
    chmod +x dist/android-bloatware-remover
    timeout 10s dist/android-bloatware-remover --test || echo "Test completed"
else
    echo "✗ Build failed!"
    exit 1
fi