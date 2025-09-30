@echo off
setlocal

echo Android Bloatware Remover - Local Build Script
echo ================================================

python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is required but not installed
    exit /b 1
)

echo Installing PyInstaller...
pip install pyinstaller >nul
if errorlevel 1 (
    echo Failed to install PyInstaller.
    exit /b 1
)

echo Generating PyInstaller spec file...
python build_spec.py
if errorlevel 1 (
    echo Failed to generate PyInstaller spec file.
    exit /b 1
)

if not exist android-bloatware-remover.spec (
    echo Spec file not found after generation.
    exit /b 1
)

echo Building executable...
pyinstaller android-bloatware-remover.spec --clean
if errorlevel 1 (
    echo Build failed.
    exit /b 1
)

if exist dist\android-bloatware-remover.exe (
    echo Build completed successfully.
    echo Executable location: dist\android-bloatware-remover.exe
    echo Testing executable...
    echo 5^| dist\android-bloatware-remover.exe --test >nul
    if errorlevel 1 (
        echo CLI smoke test failed.
        exit /b 1
    )
    echo CLI smoke test passed.
) else (
    echo Build completed but executable was not found in the expected location.
)

exit /b 0