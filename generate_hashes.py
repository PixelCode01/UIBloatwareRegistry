#!/usr/bin/env python3
"""Generate SHA256 hashes for release files"""

import hashlib
import os
import sys

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def main():
    files_to_hash = [
        "dist/android-bloatware-remover.exe",
        "dist/android-bloatware-remover"
    ]
    
    print("# File Verification Hashes")
    print()
    print("Use these SHA256 hashes to verify file integrity:")
    print()
    
    for file_path in files_to_hash:
        if os.path.exists(file_path):
            hash_value = calculate_sha256(file_path)
            file_size = os.path.getsize(file_path)
            print(f"**{os.path.basename(file_path)}**")
            print(f"- SHA256: `{hash_value}`")
            print(f"- Size: {file_size:,} bytes")
            print()
        else:
            print(f"File not found: {file_path}")
    
    print("## How to verify:")
    print()
    print("**Windows (PowerShell):**")
    print("```powershell")
    print("Get-FileHash -Algorithm SHA256 android-bloatware-remover-windows.exe")
    print("```")
    print()
    print("**Linux/Mac:**")
    print("```bash")
    print("sha256sum android-bloatware-remover-linux")
    print("# or")
    print("shasum -a 256 android-bloatware-remover-macos")
    print("```")

if __name__ == "__main__":
    main()