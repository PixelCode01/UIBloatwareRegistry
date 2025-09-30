from __future__ import annotations

from typing import Iterable, Optional


def generate(packages: Iterable[str], *, device_serial: Optional[str] = None) -> str:
    pkg_list = [pkg.strip() for pkg in packages if pkg.strip()]
    if not pkg_list:
        return "# No packages selected"

    prefix = f"adb -s {device_serial} shell" if device_serial else "adb shell"
    lines = ["# Run these commands in a terminal"]
    for pkg in pkg_list:
        lines.append(f"{prefix} pm uninstall --user 0 {pkg}")
    return "\n".join(lines)
