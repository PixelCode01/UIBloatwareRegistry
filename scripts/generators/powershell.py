from __future__ import annotations

from typing import Iterable, Optional


def generate(packages: Iterable[str], *, device_serial: Optional[str] = None) -> str:
    pkg_list = [pkg.strip() for pkg in packages if pkg.strip()]
    if not pkg_list:
        return "Write-Output 'No packages selected'"

    serial = f" -s {device_serial}" if device_serial else ""
    lines: list[str] = []
    lines.append("$packages = @(")
    lines.extend(f'    "{pkg}"' for pkg in pkg_list)
    lines.append(")")
    lines.append("$errors = @()")
    lines.append("foreach ($pkg in $packages) {")
    lines.append(f"    $result = adb{serial} shell pm uninstall --user 0 $pkg")
    lines.append("    if ($LASTEXITCODE -ne 0 -or -not $result.Contains('Success')) {")
    lines.append(f"        $fallback = adb{serial} shell pm disable-user --user 0 $pkg")
    lines.append("        if ($LASTEXITCODE -ne 0) {")
    lines.append("            $errors += $pkg")
    lines.append("        }")
    lines.append("    }")
    lines.append("}")
    lines.append("if ($errors.Count -gt 0) {")
    lines.append("    Write-Output 'Failed to process:'")
    lines.append("    $errors | ForEach-Object { Write-Output (\" - $_\") }")
    lines.append("} else {")
    lines.append("    Write-Output 'All packages processed successfully.'")
    lines.append("}")
    return "\n".join(lines)
