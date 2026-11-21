#!/usr/bin/env python3
"""Read exactly one decoded Tapo RTSP video frame into memory; store nothing."""
import argparse
import json
import sys
from datetime import datetime, timezone
from urllib.parse import quote

from preflight import load_config


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, help="Private camera JSON file (mode 600)")
    args = parser.parse_args()
    try:
        cfg = load_config(args.config)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        error = str(exc) if isinstance(exc, ValueError) else "config_unreadable"
        print(json.dumps({"status": "configuration_failed", "error": error}))
        return 2

    # Keep credentials inside the Python process, NOT in ffmpeg command line,
    # command history, stdout, runtime logs, or repository.
    username = quote(cfg["username"], safe="")
    password = quote(cfg["password"], safe="")
    url = f'rtsp://{username}:{password}@{cfg["host"]}:554/stream2'

    try:
        import av
        with av.open(url, options={"rtsp_transport": "tcp"}, timeout=(8.0, 8.0)) as container:
            frame = next(container.decode(video=0), None)
            if frame is None:
                raise RuntimeError("no_frame")
            event = {
                "experiment": "TAPO-01",
                "status": "frame_received",
                "observation": {
                    "source_kind": "physical_camera",
                    "sensor_model": "tapo-c220_operator_reported",
                    "stream": "stream2",
                    "width": frame.width,
                    "height": frame.height,
                    "observed_at_utc": datetime.now(timezone.utc).isoformat(),
                    "raw_frame_persisted": False,
                },
                "chronon": "not_integrated",
                "actuation": "none",
            }
            print(json.dumps(event, indent=2, ensure_ascii=False))
            return 0
    except Exception as exc:  # library errors may contain credentialed URLs: redact all
        print(json.dumps({
            "experiment": "TAPO-01",
            "status": "stream_failed",
            "error_type": type(exc).__name__,
            "note": "Check camera account, network reachability and RTSP; details intentionally redacted",
        }))
        return 1


if __name__ == "__main__":
    sys.exit(main())
