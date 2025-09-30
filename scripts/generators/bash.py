from __future__ import annotations

from typing import Iterable, Optional


def generate(packages: Iterable[str], *, device_serial: Optional[str] = None) -> str:
    pkg_list = [pkg.strip() for pkg in packages if pkg.strip()]
    if not pkg_list:
        return "# No packages selected"

    prefix = f"adb -s {device_serial} " if device_serial else "adb "
    lines: list[str] = []
    lines.append("#!/usr/bin/env bash")
    lines.append("set -euo pipefail")
    lines.append("packages=(")
    lines.extend(f'    "{pkg}"' for pkg in pkg_list)
    lines.append(")")
    lines.append("errors=()")
    lines.append("for pkg in \"${packages[@]}\"; do")
    lines.append(f"    if ! {prefix}shell pm uninstall --user 0 \"$pkg\" >/dev/null 2>&1; then")
    lines.append(f"        if ! {prefix}shell pm disable-user --user 0 \"$pkg\" >/dev/null 2>&1; then")
    lines.append("            errors+=(\"$pkg\")")
    lines.append("        fi")
    lines.append("    fi")
    lines.append("done")
    lines.append("if [ ${#errors[@]} -gt 0 ]; then")
    lines.append("    printf 'Failed to process\\n'")
    lines.append("    for pkg in \"${errors[@]}\"; do")
    lines.append("        printf ' - %s\\n' \"$pkg\"")
    lines.append("    done")
    lines.append("else")
    lines.append("    echo 'All packages processed successfully.'")
    lines.append("fi")
    return "\n".join(lines)
