@echo off
REM Local build script for Windows

echo Android Bloatware Remover - Local Build Script
echo ================================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is required but not installed
    exit /b 1
)

REM Install PyInstaller if not present
echo Installing PyInstaller...
pip install pyinstaller

REM Create spec file
echo Creating PyInstaller spec file...
(
echo # -*- mode: python ; coding: utf-8 -*-
echo.
echo block_cipher = None
echo.
echo # Collect all brand directories and their contents
echo brand_dirs = ['Samsung', 'Xiaomi', 'Oppo', 'Vivo', 'Realme', 'Tecno', 'OnePlus', 'Huawei', 'Honor', 'Motorola', 'Nothing']
echo datas = []
echo.
echo # Add brand directories
echo for brand in brand_dirs:
echo     datas.append(^(f'{brand}/*.md', f'{brand}/'^^)
echo     datas.append(^(f'{brand}/*.py', f'{brand}/'^^)
echo.
echo # Add core module
echo datas.append(^('core/*.py', 'core/'^^)
echo.
echo # Add other files
echo datas.append(^('README.md', '.'^^)
echo datas.append(^('LICENSE', '.'^^)
echo.
echo a = Analysis(
echo     ['main.py'],
echo     pathex=[],
echo     binaries=[],
echo     datas=datas,
echo     hiddenimports=[
echo         'Samsung.samsung_remover',
echo         'Xiaomi.xiaomi_remover', 
echo         'Oppo.oppo_remover',
echo         'Vivo.vivo_remover',
echo         'Realme.realme_remover',
echo         'Tecno.tecno_remover',
echo         'OnePlus.oneplus_remover',
echo         'Huawei.huawei_remover',
echo         'Honor.honor_remover',
echo         'Motorola.motorola_remover',
echo         'Nothing.nothing_remover',
echo         'core.bloatware_remover'
echo     ],
echo     hookspath=[],
echo     hooksconfig={},
echo     runtime_hooks=[],
echo     excludes=[],
echo     win_no_prefer_redirects=False,
echo     win_private_assemblies=False,
echo     cipher=block_cipher,
echo     noarchive=False,
echo ^^)
echo.
echo pyz = PYZ(^a.pure, a.zipped_data, cipher=block_cipher^^)
echo.
echo exe = EXE(
echo     pyz,
echo     a.scripts,
echo     a.binaries,
echo     a.zipfiles,
echo     a.datas,
echo     [],
echo     name='android-bloatware-remover',
echo     debug=False,
echo     bootloader_ignore_signals=False,
echo     strip=False,
echo     upx=True,
echo     upx_exclude=[],
echo     runtime_tmpdir=None,
echo     console=True,
echo     disable_windowed_traceback=False,
echo     argv_emulation=False,
echo     target_arch=None,
echo     codesign_identity=None,
echo     entitlements_file=None,
echo ^^)
) > android-bloatware-remover.spec

REM Build executable
echo Building executable...
pyinstaller android-bloatware-remover.spec --clean

if %errorlevel% equ 0 (
    echo ✓ Build completed successfully!
    echo Executable location: dist\android-bloatware-remover.exe
    
    REM Test the executable
    echo Testing executable...
    timeout /t 10 /nobreak > nul
    dist\android-bloatware-remover.exe --test
) else (
    echo ✗ Build failed!
    exit /b 1
)