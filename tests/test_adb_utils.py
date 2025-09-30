import os
import stat
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from core import adb_utils


class ResolveAdbPathTests(unittest.TestCase):
    def test_prefers_environment_variable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            adb_stub = Path(tmp) / ("adb.exe" if os.name == "nt" else "adb")
            adb_stub.write_bytes(b"")

            os.chmod(adb_stub, adb_stub.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

            with mock.patch.dict(os.environ, {"ADB_PATH": str(adb_stub)}):
                with mock.patch("os.access", return_value=True):
                    resolved = adb_utils.resolve_adb_path()

        self.assertEqual(Path(resolved), adb_stub)


class ParseDevicesOutputTests(unittest.TestCase):
    def test_parses_authorized_and_unauthorized_devices(self) -> None:
        output = (
            "List of devices attached\n"
            "R52M802RV9B\tdevice product:d2sxeea model:SM_S911B\n"
            "emulator-5554\tunauthorized\n"
            "* daemon not running; starting now at tcp:5037\n"
            "* daemon started successfully\n"
        )

        devices = adb_utils.parse_devices_output(output)

        self.assertEqual(len(devices), 2)
        self.assertEqual(devices[0].serial, "R52M802RV9B")
        self.assertEqual(devices[0].state, "device")
        self.assertIn("product:d2sxeea", devices[0].details)
        self.assertEqual(devices[1].serial, "emulator-5554")
        self.assertEqual(devices[1].state, "unauthorized")


if __name__ == "__main__":
    unittest.main()
