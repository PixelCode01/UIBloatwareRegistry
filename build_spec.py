#!/usr/bin/env python3
"""Build script for creating standalone executables."""

import subprocess

def run_command(cmd, cwd=None):
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, 
                              capture_output=True, text=True)
        print(f"Command succeeded: {cmd}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {cmd}")
        print(f"Error: {e.stderr}")
        return False

def create_spec_file():
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None

brand_dirs = [
    'Samsung',
    'Xiaomi',
    'Oppo',
    'Vivo',
    'Realme',
    'Tecno',
    'OnePlus',
    'Huawei',
    'Honor',
    'Motorola',
    'Nothing',
    'Asus',
    'Google',
    'Infinix',
    'Lenovo',
]
datas = []

for brand in brand_dirs:
    if os.path.exists(brand):
        md_files = os.path.join(brand, '*.md')
        py_files = os.path.join(brand, '*.py')
        datas.append((md_files, brand + '/'))
        datas.append((py_files, brand + '/'))

if os.path.exists('core'):
    datas.append(('core/*.py', 'core/'))

if os.path.exists('README.md'):
    datas.append(('README.md', '.'))
if os.path.exists('LICENSE'):
    datas.append(('LICENSE', '.'))

a = Analysis(
    ['main.py'],
    pathex=[os.getcwd()],
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
        'Asus.asus_remover',
        'Google.google_remover',
        'Infinix.infinix_remover',
        'Lenovo.lenovo_remover',
        'core.bloatware_remover',
        'device_detector',
        'version'
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
    upx=False,
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
    
    print("Created PyInstaller spec file.")

def build_executable():
    print("Building standalone executable...")
    
    if not run_command("pip install pyinstaller"):
        return False
    
    create_spec_file()
    
    if not run_command("pyinstaller android-bloatware-remover.spec --clean"):
        return False
    
    print("Executable built successfully.")
    return True

def main():
    print("Creating PyInstaller spec file...")
    create_spec_file()
    print("Spec file created successfully!")

if __name__ == "__main__":
    main()