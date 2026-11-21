#!/usr/bin/env bash
# TAPO-01 / Pi 4 read-only acquisition foundation.
# Installs OS packages only; does not start services or move the camera.
set -euo pipefail

if [[ $(id -u) -ne 0 ]]; then
  echo "Run with sudo: sudo bash scripts/bootstrap.sh" >&2
  exit 2
fi

if [[ $(uname -m) != "aarch64" ]]; then
  echo "Expected aarch64 Raspberry Pi OS Lite 64-bit" >&2
  exit 2
fi

# shellcheck disable=SC1091
source /etc/os-release
if [[ "$VERSION_CODENAME" != "trixie" ]]; then
  echo "Expected Raspberry Pi OS Debian 13 (trixie); found $VERSION_CODENAME" >&2
  exit 2
fi

if [[ -r /proc/device-tree/model ]]; then
  model=$(tr -d '\000' </proc/device-tree/model)
  if [[ "$model" != *"Raspberry Pi 4 Model B"* ]]; then
    echo "Warning: this experiment is sized for Raspberry Pi 4 Model B; detected: $model" >&2
  fi
fi

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y \
  ca-certificates curl ffmpeg git python3 python3-av python3-venv

/usr/bin/python3 -c 'import av; print("PyAV OK:", av.__version__)'
echo "TAPO-01 bootstrap complete. No camera stream or motor commands were started."
