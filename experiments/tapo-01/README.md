# TAPO-01 — Raspberry Pi 4 / Active Vision Lab (read-only bootstrap)

**Status:** experimental onboarding candidate; not deployed or physically verified.  
**Reported hardware:** Raspberry Pi 4 Model B (4 GB) and TP-Link Tapo C220.  
**Baseline:** Raspberry Pi OS Lite **64-bit**, Debian **13/trixie**, local LAN only.  
**Purpose:** reproducible acquisition test before any autonomy, PTZ movement or Chronon integration.

This is a lab experiment, **not** the canonical OpenRGD runtime, a completed
Reality Ingress/Chronon implementation, or an approved actuator driver. No
credentials, camera frames, local IP addresses or recordings belong in Git.

## 1. Write the microSD on Windows or Fedora

Use official Raspberry Pi Imager:
https://www.raspberrypi.com/software/

- Device: Raspberry Pi 4
- OS: Raspberry Pi OS (other) -> Raspberry Pi OS Lite (64-bit), **not Legacy**
- Storage: empty microSD (32 GB minimum; 64 GB A2 preferable)
- Customisation: hostname **rgd-tapo-01**, user **rgd** (or your own username),
  timezone **Europe/Rome**, SSH enabled (public-key auth preferred),
  and the intended LAN/Wi-Fi.
- For a Pi 4 use an adequate **5 V / 3 A USB-C** power supply.
- Put the Pi and camera on the same LAN. Ethernet is preferred on the Pi
  during the first experiments; isolate both from public port forwarding.

From Windows PowerShell, connect:

~~~powershell
ssh rgd@rgd-tapo-01.local
~~~

If mDNS does not resolve, find the Pi in the router's DHCP client table and
connect via IP instead. Only the real operator can flash the microSD,
enter credentials and verify physical hardware.

## 2. Update and reboot the Pi

~~~bash
sudo apt update
sudo apt full-upgrade -y
sudo reboot
~~~

Reconnect via SSH. Verify:

~~~bash
hostnamectl
uname -m
free -h
df -h /
~~~

Expected: Debian 13, aarch64, around 4 GB total RAM.

## 3. Install the minimum acquisition dependencies

Clone this **review branch** until the PR is reviewed and merged. Do not
blindly execute scripts from a remote URL:

~~~bash
mkdir -p ~/openrgd/repos
cd ~/openrgd/repos
git clone --branch feat/tapo01-pi4-readonly-bootstrap \
  https://github.com/OpenRGD/rgd-labs.git
cd rgd-labs/experiments/tapo-01
sudo bash scripts/bootstrap.sh
/usr/bin/python3 scripts/preflight.py
~~~

Only Debian packages are installed: git, curl, ffmpeg, python3-av,
python3-venv and certificates. No Docker, continuous video, recording,
systemd service or motor control is enabled.

## 4. Configure the camera (only after operator approval)

Set up the Tapo camera in the TP-Link app. Under advanced camera settings,
create a **camera account** (not the cloud account) for RTSP/ONVIF.
Find the camera's private IPv4 address using Tapo/router network information;
prefer a DHCP reservation. The documented Tapo ports are RTSP **554**
and ONVIF **2020**, with low-bandwidth RTSP path **/stream2**.

Keep credentials **outside** the checkout, in a private local file:

~~~bash
mkdir -p ~/.config/openrgd
chmod 700 ~/.config/openrgd
cp camera.example.json ~/.config/openrgd/tapo-01.json
chmod 600 ~/.config/openrgd/tapo-01.json
nano ~/.config/openrgd/tapo-01.json
~~~

Replace the three example values with the private camera IP and the camera
account username/password. Use correct JSON escaping for quotation marks.
Never paste passwords, full RTSP URLs or private recordings into chats,
logs, bug reports or GitHub issues.

Verify both local TCP ports (a reachability test, **not** an ONVIF
capability/actuation test):

~~~bash
/usr/bin/python3 scripts/preflight.py \
  --config ~/.config/openrgd/tapo-01.json
~~~

Probe just one decoded video frame, in RAM and without recording:

~~~bash
/usr/bin/python3 scripts/rtsp_probe.py \
  --config ~/.config/openrgd/tapo-01.json
~~~

Expected progression is a JSON report with status **pass** and both ports
reachable, then **frame_received** for the RTSP decode. These are
**acceptance criteria**, not claims of successful physical tests.

## 5. Boundaries and next phase

- The camera remains on TP-Link firmware; this experiment neither flashes
  it nor changes its factory safety mechanisms.
- No pan/tilt commands are issued yet. The ONVIF PTZ profile, firmware
  version, limits, tracking conflicts and emergency stop behavior must be
  independently verified with small manually approved motions.
- Source timestamps in the RTSP smoke test are local Pi clock readings,
  **not** certified Chronograf timestamps.
- A received frame is a **raw observation candidate**, not a Chronon,
  a verified detection, a learned memory or a claim of robot selfhood.
- The canonical robot description and non-actuating boot must be governed
  by [OpenRGD](https://github.com/OpenRGD/openrgd);
  [Reality Ingress](https://github.com/OpenRGD/rgd-reality-ingress) owns
  observation provenance, Cognition proposes attention/actions, Somatic/
  Operation gates movement and the appropriate temporal component owns
  Chronon representation.
- Experiment should be conducted in a space where any people present
  have been informed about the camera. The baseline captures no stored
  video/audio. Retention and consent policy is required before recording.
- If later persisting observations, avoid heavy continuous writes to
  microSD; use a dedicated volume/SSD, explicit retention and integrity
  metadata.

## Review checklist

- [ ] OS, CPU architecture, memory and free space actually verified on Pi 4
- [ ] Tapo C220 model/hardware revision and firmware version confirmed
- [ ] SSH access and local-only network protections verified
- [ ] Preflight both ports 554/2020 passed
- [ ] One RTSP /stream2 frame decoded without storage
- [ ] ONVIF capabilities inspected **before** enabling motor commands
- [ ] Chronon integration remains explicitly unimplemented

**Privacy:** public files must not contain precise lab location, network
addresses, serials, account passwords, recordings or personal imagery.
