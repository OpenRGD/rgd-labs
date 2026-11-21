#!/usr/bin/env python3
"""No-network tests for TAPO-01 private camera configuration."""
import json
import os
import tempfile
import unittest
from pathlib import Path
from sys import path

path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from preflight import load_config  # noqa: E402


class ConfigTests(unittest.TestCase):
    def test_private_config_is_readable(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "camera.json"
            file.write_text(json.dumps({
                "host": "192.168.1.50",
                "username": "local_camera_account",
                "password": "example-only",
            }), encoding="utf-8")
            os.chmod(file, 0o600)
            self.assertEqual(load_config(file)["host"], "192.168.1.50")

    def test_group_read_permissions_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "camera.json"
            file.write_text(json.dumps({
                "host": "192.168.1.50",
                "username": "local_camera_account",
                "password": "example-only",
            }), encoding="utf-8")
            os.chmod(file, 0o640)
            with self.assertRaises(ValueError):
                load_config(file)

    def test_public_ip_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "camera.json"
            file.write_text(json.dumps({
                "host": "8.8.8.8",
                "username": "local_camera_account",
                "password": "example-only",
            }), encoding="utf-8")
            os.chmod(file, 0o600)
            with self.assertRaises(ValueError):
                load_config(file)


if __name__ == "__main__":
    unittest.main()
