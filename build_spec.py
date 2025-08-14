#!/usr/bin/env python3
"""
Build script for creating standalone executables
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {cmd}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {cmd}")
        print(f"Error: {e.stderr}")
        return False

def create_spec_file():
    """Create PyInstaller spec file"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

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
'''
    
    with open('android-bloatware-remover.spec', 'w') as f:
        f.write(spec_content)
    
    print("✓ Created PyInstaller spec file")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building standalone executable...")
    
    # Install PyInstaller if not present
    if not run_command("pip install pyinstaller"):
        return False
    
    # Create spec file
    create_spec_file()
    
    # Build executable
    if not run_command("pyinstaller android-bloatware-remover.spec --clean"):
        return False
    
    print("✓ Executable built successfully")
    return True

def main():
    """Main build function"""
    print("Android Bloatware Remover - Build Script")
    print("=" * 50)
    
    if build_executable():
        print("\n✓ Build completed successfully!")
        print("Executable location: dist/android-bloatware-remover")
    else:
        print("\n✗ Build failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()