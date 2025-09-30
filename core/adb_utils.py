"""Utility helpers for interacting with the Android Debug Bridge (adb)."""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

DEFAULT_TIMEOUT = 15


@dataclass
class DeviceState:
    """Represents the state of a connected adb device."""

    serial: str
    state: str
    details: str = ""

    def summary(self) -> str:
        """Return a concise human-readable summary of the device."""
        extra = f" {self.details}" if self.details else ""
        return f"{self.serial} [{self.state}]{extra}"


class ADBError(Exception):
    """Base class for adb related errors."""


class ADBNotFoundError(ADBError):
    """Raised when the adb executable cannot be located."""


class ADBCommandError(ADBError):
    """Raised when an adb command fails or times out."""

    def __init__(
        self,
        message: str,
        *,
        returncode: Optional[int] = None,
        stdout: str = "",
        stderr: str = "",
    ) -> None:
        super().__init__(message)
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self) -> str:
        base = super().__str__()
        fragments = [base]
        if self.returncode is not None:
            fragments.append(f"(exit code: {self.returncode})")
        if self.stderr:
            fragments.append(f"stderr: {self.stderr.strip()}")
        return " ".join(fragments)


class DeviceSelectionError(ADBError):
    """Raised when no suitable device can be selected."""

    def __init__(self, message: str, *, devices: Optional[List[DeviceState]] = None) -> None:
        super().__init__(message)
        self.devices: List[DeviceState] = devices or []


def _iter_adb_candidates(preferred: Optional[str] = None) -> Iterable[Path]:
    """Yield potential adb executable paths in priority order."""

    seen: set[str] = set()

    def _emit(path: Optional[str]) -> Iterable[Path]:
        if not path:
            return []
        target = Path(path).expanduser()
        if target.is_dir():
            return [target / name for name in ("adb.exe", "adb")]
        return [target]

    def _yield(path: Optional[str]):
        for candidate in _emit(path):
            resolved = candidate.resolve()
            key = str(resolved).lower()
            if key in seen:
                continue
            seen.add(key)
            yield resolved

    if preferred:
        yield from _yield(preferred)

    for env_var in ("ADB_PATH", "ANDROID_ADB_PATH"):
        yield from _yield(os.environ.get(env_var))

    for name in ("adb.exe", "adb"):
        which = shutil.which(name)
        if which:
            yield from _yield(which)

    potential_dirs = []
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        potential_dirs.append(Path(meipass))
        potential_dirs.append(Path(meipass) / "platform-tools")

    executable_dir = Path(sys.executable).resolve().parent
    potential_dirs.append(executable_dir)
    potential_dirs.append(executable_dir / "platform-tools")

    project_root = Path(__file__).resolve().parent.parent
    potential_dirs.append(project_root)
    potential_dirs.append(project_root / "platform-tools")

    for directory in potential_dirs:
        yield from _yield(str(directory))


def _platform_tools_directory() -> Path:
    """Location where downloaded platform tools should reside."""

    return Path(__file__).resolve().parent.parent / "platform-tools"


def _adb_executable_name() -> str:
    return "adb.exe" if os.name == "nt" else "adb"


def _platform_tools_download_url() -> str:
    system = platform.system().lower()
    if system == "windows":
        return "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
    if system == "darwin":
        return "https://dl.google.com/android/repository/platform-tools-latest-darwin.zip"
    if system == "linux":
        return "https://dl.google.com/android/repository/platform-tools-latest-linux.zip"
    raise ADBNotFoundError(
        f"Unsupported operating system '{platform.system()}' for automatic adb installation."
    )


def _download_and_extract_platform_tools(destination: Path) -> None:
    url = _platform_tools_download_url()
    parent = destination.parent
    parent.mkdir(parents=True, exist_ok=True)

    print("Downloading Android platform tools (adb)...")
    with tempfile.TemporaryDirectory() as tmpdir:
        archive_path = Path(tmpdir) / "platform-tools.zip"
        with urllib.request.urlopen(url) as response, archive_path.open("wb") as archive_file:
            shutil.copyfileobj(response, archive_file)

        # Extract into parent directory so the bundled `platform-tools` folder is created.
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(parent)


def _ensure_platform_tools_installed() -> Optional[str]:
    destination = _platform_tools_directory()
    adb_path = destination / _adb_executable_name()

    if adb_path.is_file() and os.access(adb_path, os.X_OK):
        return str(adb_path)

    try:
        _download_and_extract_platform_tools(destination)
    except Exception as exc:  # noqa: BLE001 - propagate as adb error
        raise ADBNotFoundError(
            "Failed to download Android platform tools automatically. "
            "Please install the Android SDK platform tools manually and rerun the program."
        ) from exc

    if adb_path.is_file():
        try:
            adb_path.chmod(adb_path.stat().st_mode | 0o111)
        except OSError:
            # If chmod fails (e.g., on Windows), continue silently.
            pass
        if os.access(adb_path, os.X_OK):
            return str(adb_path)

    return None


def resolve_adb_path(preferred: Optional[str] = None) -> str:
    """Return a usable adb executable path or raise an informative error."""

    for candidate in _iter_adb_candidates(preferred):
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)

    installed = _ensure_platform_tools_installed()
    if installed:
        return installed

    raise ADBNotFoundError(
        "Unable to locate the adb executable. Automatic installation failed. "
        "Set the ADB_PATH environment variable or install the Android Platform "
        "Tools manually and add them to PATH."
    )


def run_command(
    adb_path: str,
    args: List[str],
    *,
    device_serial: Optional[str] = None,
    timeout: int = DEFAULT_TIMEOUT,
    check: bool = True,
) -> subprocess.CompletedProcess:
    """Execute an adb command and optionally raise on failure."""

    if not adb_path:
        raise ADBNotFoundError("ADB path is not configured")

    cmd = [adb_path]
    if device_serial:
        cmd.extend(["-s", device_serial])
    cmd.extend(args)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as exc:
        raise ADBNotFoundError(str(exc)) from exc
    except subprocess.TimeoutExpired as exc:
        raise ADBCommandError(
            "ADB command timed out",
            stdout=(exc.stdout or ""),
            stderr=(exc.stderr or ""),
        ) from exc

    if check and result.returncode != 0:
        raise ADBCommandError(
            "ADB command failed",
            returncode=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
        )

    return result


def start_server(adb_path: str, *, timeout: int = DEFAULT_TIMEOUT) -> None:
    """Ensure the adb server is running."""

    run_command(adb_path, ["start-server"], timeout=timeout, check=False)


def parse_devices_output(stdout: str) -> List[DeviceState]:
    """Parse the output of `adb devices -l` into structured entries."""

    devices: List[DeviceState] = []
    for raw_line in stdout.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("List of devices attached"):
            continue
        if line.startswith("* daemon "):
            continue
        parts = line.split()
        if not parts:
            continue
        serial = parts[0]
        if len(parts) == 1:
            state = "unknown"
            details = ""
        else:
            state = parts[1]
            details = " ".join(parts[2:]) if len(parts) > 2 else ""
        devices.append(DeviceState(serial=serial, state=state, details=details))
    return devices


def list_devices(adb_path: str, *, timeout: int = DEFAULT_TIMEOUT) -> List[DeviceState]:
    """Return all connected devices using `adb devices -l`."""

    start_server(adb_path, timeout=timeout)
    result = run_command(adb_path, ["devices", "-l"], timeout=timeout, check=False)
    if result.returncode not in (0, None):
        raise ADBCommandError(
            "Failed to query connected devices",
            returncode=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
        )
    return parse_devices_output(result.stdout)


def find_authorized_device(
    adb_path: str,
    *,
    preferred_serial: Optional[str] = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> DeviceState:
    """Return an authorized device, preferring a specific serial when given."""

    devices = list_devices(adb_path, timeout=timeout)
    authorized = [device for device in devices if device.state == "device"]

    if preferred_serial:
        for device in authorized:
            if device.serial == preferred_serial:
                return device

    if not authorized:
        raise DeviceSelectionError(
            "No authorized devices detected",
            devices=devices,
        )

    return authorized[0]


__all__ = [
    "ADBCommandError",
    "ADBError",
    "ADBNotFoundError",
    "DEFAULT_TIMEOUT",
    "DeviceSelectionError",
    "DeviceState",
    "find_authorized_device",
    "list_devices",
    "parse_devices_output",
    "resolve_adb_path",
    "run_command",
    "start_server",
]
