#!/usr/bin/env python3
"""Non-actuating Pi / Tapo reachability preflight. No camera credentials logged."""
import argparse
import ipaddress
import json
import os
import platform
import shutil
import socket
import stat
import sys
from pathlib import Path


def load_config(path):
    config_path = Path(path).expanduser()
    mode = config_path.stat().st_mode
    if not stat.S_ISREG(mode) or mode & 0o077:
        raise ValueError("camera_config_must_be_a_private_regular_file_chmod_600")
    data = json.loads(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("camera_config_must_be_json_object")
    required = ("host", "username", "password")
    if any(not isinstance(data.get(k), str) or not data[k] for k in required):
        raise ValueError("camera_config_missing_host_username_or_password")
    try:
        ipaddress.IPv4Address(data["host"])
    except ipaddress.AddressValueError as exc:
        raise ValueError("camera_host_must_be_local_ipv4_address") from exc
    if not ipaddress.IPv4Address(data["host"]).is_private:
        raise ValueError("camera_host_must_be_private_ipv4_address")
    return data


def memory_total_mib():
    with open("/proc/meminfo", encoding="utf-8") as file:
        for line in file:
            if line.startswith("MemTotal:"):
                return round(int(line.split()[1]) / 1024)
    return 0


def tcp_open(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2):
            return True
    except (OSError, TimeoutError):
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", help="Private camera JSON, e.g. ~/.config/openrgd/tapo-01.json")
    args = parser.parse_args()

    machine = platform.machine()
    os_release = {}
    for line in Path("/etc/os-release").read_text(encoding="utf-8").splitlines():
        key, _, value = line.partition("=")
        os_release[key] = value.strip('"')
    mem_mib = memory_total_mib()
    disk_free_gib = round(shutil.disk_usage("/").free / (1024**3), 1)
    hardware_ok = machine == "aarch64" and mem_mib >= 3000 and disk_free_gib >= 3
    release_ok = os_release.get("VERSION_CODENAME") == "trixie"
    software_ok = shutil.which("ffmpeg") is not None

    try:
        import av  # pylint: disable=import-outside-toplevel,unused-import
        pyav_ok = True
    except ImportError:
        pyav_ok = False

    report = {
        "experiment": "TAPO-01",
        "mode": "read_only_non_actuating",
        "hardware": {
            "architecture": machine,
            "mem_total_mib": mem_mib,
            "free_root_gib": disk_free_gib,
            "hardware_ok": hardware_ok,
        },
        "os": {
            "codename": os_release.get("VERSION_CODENAME", "unknown"),
            "supported_baseline": release_ok,
        },
        "software": {"ffmpeg": software_ok, "python3_av": pyav_ok},
        "camera": {"configured": bool(args.config)},
        "chronon": "not_integrated",
    }

    camera_ok = True
    if args.config:
        try:
            cfg = load_config(args.config)
            checks = {str(port): tcp_open(cfg["host"], port) for port in (554, 2020)}
            camera_ok = all(checks.values())
            report["camera"]["tcp_reachable"] = checks
            report["camera"]["note"] = "TCP connectivity only; no stream or ONVIF PTZ capability validation"
        except (ValueError, OSError, json.JSONDecodeError) as exc:
            camera_ok = False
            report["camera"]["config_error"] = (
                str(exc) if isinstance(exc, ValueError) else "camera_config_not_readable"
            )

    good = hardware_ok and release_ok and software_ok and pyav_ok and camera_ok
    report["status"] = "pass" if good else "needs_attention"
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
