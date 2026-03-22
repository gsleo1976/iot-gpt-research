# IoT-GPT Research Project — Student Contribution Guide
### How to Learn, Build, and Contribute

> **Maintained by:** Gurdev Singh · gurdev.leo@gmail.com
> **Repository:** [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research)
> **Version:** March 2026 — Research Preview
> **Audience:** University students, hobbyists, beginner makers

---

## Table of Contents

1. [What Is This Project?](#1-what-is-this-project)
2. [Hardware Shopping List](#2-hardware-shopping-list)
3. [Daily Learning Plan — 12-Week Roadmap](#3-daily-learning-plan--12-week-roadmap)
4. [Your First Project — Weather-to-Light Signal](#4-your-first-project--weather-to-light-signal)
5. [Experiments to Carry Out](#5-experiments-to-carry-out)
6. [Project Implementation Plan](#6-project-implementation-plan)
7. [Step-by-Step Setup Guide](#7-step-by-step-setup-guide)
8. [Troubleshooting Reference](#8-troubleshooting-reference)
9. [Useful Links & Resources](#9-useful-links--resources)

---

## 1. What Is This Project?

IoT-GPT is a research project building an intelligent coordination layer for smart home devices. Instead of devices working in isolation, IoT-GPT gives them a shared brain — so a room heater knows the water heater is running, a smart bulb knows it is going to snow, and the whole home schedules itself around cheap electricity hours.

As a student contributor you will build real hardware, write real Python code, and run real experiments. By the end, you will have hands-on experience with IoT protocols, sensor programming, smart automation, and energy data analysis — skills directly relevant to careers in embedded systems, data engineering, and sustainable technology.

> **Core Idea:** Today's "smart" devices are actually dumb loners. IoT-GPT makes them talk to each other — saving energy, reducing stress, and creating a calmer home.

---

## 2. Hardware Shopping List

You do not need all devices on day one. The list is ordered by priority — start with the first four items (under £50 / $60) and add more as you progress.

### 2.1 Essential Starter Kit (~£50 / ~$60)

| # | Device | Purpose | Approx. Cost | Where to Buy |
|---|--------|---------|-------------|--------------|
| 1 | Raspberry Pi 5 (4 GB) | Main computer — runs all automation logic | £55 / $75 | [raspberrypi.com](https://raspberrypi.com) · [Amazon India](https://www.amazon.in/s?k=raspberry+pi+5) |
| 2 | Raspberry Pi USB-C Power Supply | Powers the Pi reliably at 5V 5A | £12 / $15 | [raspberrypi.com](https://raspberrypi.com) · [Amazon India](https://www.amazon.in/s?k=raspberry+pi+5+power+supply) |
| 3 | MicroSD Card 32 GB+ (Class 10) | Operating system & data storage | £8 / $10 | [Amazon India](https://www.amazon.in/s?k=microsd+card+32gb+class+10) |
| 4 | DHT22 Temperature/Humidity Sensor | Measures indoor temperature & humidity | £5 / $6 | [Amazon India](https://www.amazon.in/s?k=DHT22+temperature+humidity+sensor) |
| 5 | Breadboard + Jumper Wires Kit | Prototype circuits without soldering | £5 / $6 | [Amazon India](https://www.amazon.in/s?k=breadboard+jumper+wires+kit) |
| 6 | HDMI cable + monitor (temporary) | First-time Pi setup only | You may already have one | — |

### 2.2 Smart Lighting & ZigBee (~£40 / ~$50)

| # | Device | Purpose | Approx. Cost | Where to Buy |
|---|--------|---------|-------------|--------------|
| 7 | SONOFF Zigbee 3.0 USB Dongle Plus | ZigBee coordinator — connects smart bulbs to Pi | £15 / $18 | [Amazon India](https://www.amazon.in/s?k=sonoff+zigbee+usb+dongle) · [SONOFF store](https://sonoff.tech) |
| 8 | IKEA TRADFRI E27 White Spectrum Bulb | Calm ambient signals — warm to cool white | £8 / $10 | [IKEA](https://www.ikea.com/in/en/) · [Amazon India](https://www.amazon.in/s?k=IKEA+TRADFRI+smart+bulb) |
| 9 | IKEA TRADFRI E27 Colour Bulb | Full RGB colour signals (snow = blue, etc.) | £15 / $18 | [IKEA](https://www.ikea.com/in/en/) · [Amazon India](https://www.amazon.in/s?k=IKEA+TRADFRI+colour+bulb) |
| 10 | Lamp or desk lamp with E27 socket | Holds the smart bulb for testing | £8 / $10 | [Amazon India](https://www.amazon.in/s?k=desk+lamp+e27+socket) · IKEA |

### 2.3 Energy Monitoring (~£30 / ~$36)

| # | Device | Purpose | Approx. Cost | Where to Buy |
|---|--------|---------|-------------|--------------|
| 11 | TP-Link Kasa Smart Plug (with energy monitoring) | Measures real-time power draw of any device plugged in | £15 / $18 | [Amazon India](https://www.amazon.in/s?k=tp-link+kasa+smart+plug+energy+monitoring) |
| 12 | Second Smart Plug (any brand with energy metering) | Monitor a second device simultaneously | £12 / $15 | [Amazon India](https://www.amazon.in/s?k=smart+plug+energy+monitor) |

> **Total Budget:** Starter kit only: ~£50 / ~$60 · Full setup (all items): ~£148 / ~$188. You can start all experiments with just the starter kit + ZigBee items.

---

## 3. Daily Learning Plan — 12-Week Roadmap

This plan assumes 1–2 hours per day on weekdays and 2–3 hours on weekends. Each week ends with a hands-on mini-project so you always finish with something working.

---

### PHASE 1 (Weeks 1–3) — Foundations

#### Week 1 — Python & Raspberry Pi Basics

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | Python refresher — variables, loops, functions | Complete Python.org tutorial sections 1–4 · [python.org/about/gettingstarted](https://python.org/about/gettingstarted) |
| Tue | Working with files and JSON in Python | Read/write a JSON file; practice dict operations |
| Wed | Flash Raspberry Pi OS onto microSD | Download Raspberry Pi Imager; flash OS; first boot |
| Thu | SSH into Pi, install packages (pip, git) | Enable SSH in raspi-config; connect from laptop |
| Fri | Run your first Python script on the Pi | Write a hello.py; schedule it with cron |
| Sat | Requests library — calling a web API | Fetch weather from wttr.in using requests library |
| Sun | **Mini-project:** Weather forecast terminal app | Print 3-day forecast for your city with colour output |

#### Week 2 — Sensors & GPIO

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | GPIO basics — digital in/out | Blink an LED using RPi.GPIO library |
| Tue | DHT22 wiring — 3-wire connection to Pi | Wire DHT22 to pins 3.3V, GND, GPIO4; read values |
| Wed | Reading DHT22 with Python | `pip install adafruit-circuitpython-dht`; read every 10s |
| Thu | Logging sensor data to CSV | Write timestamp, temp, humidity to data.csv every 60s |
| Fri | Matplotlib — plot your sensor data | Load CSV, plot 24-hour temperature chart |
| Sat | Threshold alerts — print when too hot/cold | Add logic: if temp > 24°C print "Too warm" |
| Sun | **Mini-project:** Indoor climate monitor | Run for 24 hours; plot results; identify patterns |

#### Week 3 — MQTT Messaging Protocol

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | What is MQTT? Topics, subscribe, publish | Read: [mosquitto.org/man/mqtt-7.html](https://mosquitto.org/man/mqtt-7.html) |
| Tue | Install Mosquitto broker on Pi | `sudo apt install mosquitto mosquitto-clients` |
| Wed | Publish a message from command line | `mosquitto_pub -t home/temp -m "22.5"` |
| Thu | Subscribe with Python (paho-mqtt) | `pip install paho-mqtt`; write subscriber.py |
| Fri | Publish sensor data to MQTT topic | Combine DHT22 reader + paho publish — pipe live data |
| Sat | Multiple topics — simulating two devices | Publish temp + humidity to separate topics |
| Sun | **Mini-project:** Live sensor dashboard in terminal | Subscribe to all topics; print latest values on screen |

---

### PHASE 2 (Weeks 4–6) — IoT & Smart Devices

#### Week 4 — ZigBee & Smart Bulbs

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | What is ZigBee? How ZigBee mesh works | [zigbee.org/learn](https://zigbee.org/learn) + [zigbee2mqtt.io/guide/getting-started](https://www.zigbee2mqtt.io/guide/getting-started/) |
| Tue | Install Zigbee2MQTT on Pi | Follow zigbee2mqtt.io installation guide |
| Wed | Pair your first IKEA TRADFRI bulb | Enable pairing mode; factory reset bulb (6× on/off); pair |
| Thu | Control bulb brightness via MQTT | Publish to `zigbee2mqtt/bulb/set` — change brightness 0–254 |
| Fri | Control bulb colour temperature | Set `color_temp` (150 = cool, 500 = warm) |
| Sat | Read bulb state back via MQTT | Subscribe to `zigbee2mqtt/bulb` — read JSON state |
| Sun | **Mini-project:** Bulb as calm notification | If DHT22 temp > 24°C → bulb turns warm amber |

#### Week 5 — APIs & External Data Sources

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | REST APIs — GET requests and JSON parsing | Use `wttr.in/London?format=j1` — parse JSON response |
| Tue | Open-Meteo weather API (no API key needed) | [open-meteo.com](https://open-meteo.com) — fetch 7-day forecast |
| Wed | Sunrise/sunset API | [api.sunrise-sunset.org](https://sunrise-sunset.org/api) — get today's sunrise time |
| Thu | Open-Meteo AQI — air quality index | Fetch hourly AQI; interpret pm2_5 values |
| Fri | Combining two APIs in one script | Fetch weather + AQI; decide if window should open |
| Sat | Scheduling — run code at specific times | `pip install schedule` |
| Sun | **Mini-project:** Sun-aware daily automation | Lights dim at sunset; morning weather check at 7am |

#### Week 6 — Data Storage & Visualisation

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | SQLite basics — create, insert, query | `import sqlite3`; create sensor_data.db; store readings |
| Tue | Install InfluxDB on Pi | [influxdata.com/downloads](https://www.influxdata.com/downloads/) — OSS version |
| Wed | Write sensor data to InfluxDB | `pip install influxdb-client`; write temperature points |
| Thu | Install Grafana on Pi | `apt install grafana`; connect to InfluxDB data source |
| Fri | Build a Grafana dashboard | Create panels: temperature, humidity, 24h trend |
| Sat | Set up Grafana alerts | Alert if temperature stays > 25°C for 30 minutes |
| Sun | **Mini-project:** 48-hour sensor recording | Log all sensor data for 2 days; analyse in Grafana |

---

### PHASE 3 (Weeks 7–9) — IoT-GPT System Building

#### Week 7 — Device Coordination Logic

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | JSON data structures for device attributes | Design a dict: `{"name":"water_heater","watts":3500,"warmup_min":20}` |
| Tue | Building the Device Attribute Registry (DAR) | Create devices.json with 5 devices; write a loader class |
| Wed | Conflict detection — which devices clash? | Write `detect_conflicts()`: if sum of simultaneous watts > 4000 |
| Thu | Simple scheduler — earliest start time | Given constraints, find safe start slots for each device |
| Fri | Off-peak electricity windows | Add `peak_hours=[6,9,17,20]` to DAR; find cheapest slots |
| Sat | OR-Tools introduction (optional advanced) | `pip install ortools`; model scheduling as a constraint problem |
| Sun | **Mini-project:** Two-device scheduler | Schedule water heater + room heater with no overlap |

#### Week 8 — Putting It All Together

| Day | Topic | Task / Resource |
|-----|-------|----------------|
| Mon | Multi-sensor MQTT network | DHT22 on Pi + simulated second sensor; both publish |
| Tue | Coordinator script — subscribe to all topics | `iot_gpt_brain.py`: reads all sensors, makes decisions |
| Wed | Decision engine — if/then rules | If morning + cold → schedule water heat for 06:40 |
| Thu | Light as output — map decisions to bulb colour | Cold morning → warm white; snow tonight → blue glow |
| Fri | Energy budget tracking | Track daily kWh; if over budget → amber warning light |
| Sat | Testing and debugging | Simulate edge cases: sensor failure, API timeout, bulb offline |
| Sun | **Mini-project:** Full mini IoT-GPT demo | All sensors → brain → decisions → calm light signals working |

#### Weeks 9–12 — Contribute to the Research

By week 9 you have a working prototype. The remaining weeks are about contributing to the actual research:

- Run the provided experiments (Section 5) and log your results to a shared CSV format
- Open a GitHub issue or pull request with your findings, improvements, or new sample code
- Write up a short experiment report (1–2 pages) using the provided template
- Optionally: implement a new use case and add it to the Device Attribute Registry

---

## 4. Your First Project — Weather-to-Light Signal

This is the very first thing you will build. It takes about **3–4 hours** end-to-end and demonstrates the single most important idea in the project: *technology informing without demanding*. A smart bulb glows a calm colour based on tomorrow's weather — no phone, no notification, no interruption.

> **End Result:** A Python script on your Raspberry Pi that checks the weather forecast every hour. If snow or ice is forecast, the shoe-rack bulb glows blue. If it is a warm sunny day, it glows soft warm white. If rain is coming, it glows cool white. Running 24/7, silently.

### 4.1 Hardware Required

- Raspberry Pi 5 (set up with Raspberry Pi OS)
- SONOFF ZigBee USB Dongle (plugged into Pi)
- IKEA TRADFRI E27 Colour Bulb (paired via Zigbee2MQTT)
- Desk lamp or any E27 lamp socket
- Internet connection on the Pi

### 4.2 Software Setup

**Step 1 — Install Zigbee2MQTT** (if not already done):

```bash
# On your Raspberry Pi:
sudo apt update && sudo apt upgrade -y
sudo apt install nodejs npm -y
sudo npm install -g zigbee2mqtt

# Edit config file
nano /opt/zigbee2mqtt/data/configuration.yaml
# Set serial port to /dev/ttyUSB0 (check with: ls /dev/ttyUSB*)
# Set homeassistant: false, permit_join: true
```

**Step 2 — Pair your IKEA bulb:**

```bash
# Start Zigbee2MQTT
sudo systemctl start zigbee2mqtt

# Factory reset your IKEA bulb: switch on/off 6 times rapidly
# It should flash to confirm reset, then appear in Zigbee2MQTT log
# Check: sudo journalctl -u zigbee2mqtt -f --output=cat
```

**Step 3 — Install Python libraries:**

```bash
pip install requests paho-mqtt --break-system-packages
```

### 4.3 The Code — `weather_light.py`

```python
import requests
import paho.mqtt.publish as publish
import time

MQTT_HOST   = "localhost"
BULB_TOPIC  = "zigbee2mqtt/YOUR_BULB_NAME/set"
CITY        = "London"   # change to your city

def get_weather():
    """Fetch tomorrow's weather code from Open-Meteo."""
    url = (f"https://api.open-meteo.com/v1/forecast"
           f"?latitude=51.5&longitude=-0.1"
           f"&daily=weathercode&timezone=Europe/London")
    r = requests.get(url, timeout=10)
    codes = r.json()["daily"]["weathercode"]
    return codes[1]  # tomorrow (index 0 = today)

def weather_to_light(code):
    """Map weather code to a calm bulb colour."""
    # WMO weather codes: 71-77 = snow, 85-86 = snow showers
    if code in range(71, 78) or code in [85, 86]:
        return {"color": {"x": 0.14, "y": 0.07}, "brightness": 120}  # Blue
    # 61-67 = rain
    elif code in range(61, 68):
        return {"color_temp": 200, "brightness": 100}  # Cool white
    # 0-3 = clear/partly cloudy
    elif code in range(0, 4):
        return {"color_temp": 300, "brightness": 200}  # Warm white
    else:
        return {"color_temp": 370, "brightness": 150}  # Neutral

def send_to_bulb(payload):
    import json
    publish.single(BULB_TOPIC, json.dumps(payload), hostname=MQTT_HOST)
    print(f"Sent to bulb: {payload}")

if __name__ == "__main__":
    while True:
        try:
            code = get_weather()
            print(f"Tomorrow weather code: {code}")
            light_setting = weather_to_light(code)
            send_to_bulb(light_setting)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(3600)  # check every hour
```

### 4.4 Colour Reference

| Weather Condition | WMO Codes | Bulb Signal |
|-------------------|-----------|-------------|
| Snow / ice forecast | 71–77, 85–86 | 🔵 Blue glow |
| Rain | 61–67 | 🔷 Cool white |
| Clear / sunny | 0–3 | 🟡 Warm white |
| Other (cloud, fog) | All others | ⚪ Neutral white |

### 4.5 Run and Test

1. Save the script as `weather_light.py` on your Pi
2. Update `BULB_TOPIC` with your actual bulb name from Zigbee2MQTT
3. Update latitude/longitude for your city (use [latlong.net](https://www.latlong.net))
4. Run: `python weather_light.py`
5. Watch your bulb change colour — it updates every hour
6. Auto-start on boot: `sudo crontab -e` → add `@reboot python /home/pi/weather_light.py &`

> **Congratulations!** You have just built a working piece of calm technology. Your home now knows about tomorrow's weather — and communicates it without a single notification.

---

## 5. Experiments to Carry Out

Each experiment builds on the previous one. Complete them in order and record results in a CSV file — this data feeds directly into the research.

---

### Experiment 1 — Weather Signal Light (Starter) | Week 4–5

Run the weather light for **7 continuous days** and log the following:

| Date | Forecast Code | Light Colour Shown | Actual Weather Next Day | Correct? |
|------|--------------|-------------------|------------------------|---------|
| 2026-MM-DD | 71 (snow) | Blue | Light snow at 9am | Yes |

**Research question:** How often does the weather API forecast match actual conditions?

---

### Experiment 2 — Simultaneous Load Logger | Week 5–6

**Goal:** Quantify the energy problem IoT-GPT is solving. Log real-world power draw when two high-power devices run simultaneously vs. staggered.

**Equipment needed:**
- 2 smart plugs with energy monitoring (TP-Link Kasa EP25)
- Device A: Electric kettle or fan heater (~2,000–2,500W)
- Device B: Hair dryer or second heater (~1,000–2,000W)

**Method:**
1. Run both devices simultaneously for 10 minutes. Record peak wattage every 30 seconds.
2. Wait 30 minutes. Run Device A for 15 min, then Device B for 15 min (staggered).
3. Compare peak demand and calculate cost difference using your electricity tariff.

| Mode | Peak Watts | Duration (min) | Energy (kWh) | Estimated Cost |
|------|-----------|----------------|-------------|----------------|
| Simultaneous | — | 10 | — | — |
| Staggered | — | 10 | — | — |

---

### Experiment 3 — Multi-Sensor MQTT Network | Week 5–6

**Goal:** Build a 2-node sensor network and demonstrate that a central brain can receive all data and make coordinated decisions.

- **Node 1:** Your Raspberry Pi with DHT22 publishing to `home/node1/temperature`
- **Node 2:** Simulated second room using `samples/04_mqtt_iot_simulator.py`

**Success criteria:** Both nodes publishing; central subscriber receives all messages; latency under 500ms.

---

### Experiment 4 — Off-Peak Scheduler Validation | Week 7

**Goal:** Verify that the smart scheduler actually moves loads to cheaper electricity hours and calculate real savings.

1. Find your electricity tariff: standard rate (e.g. £0.24/kWh) and off-peak rate (e.g. £0.07/kWh)
2. Run `samples/03_smart_device_scheduler.py` for one week on your Pi
3. Compare: cost without IoT-GPT (naive) vs with IoT-GPT (optimised)
4. Extrapolate to annual savings and log your result

| Week | Naive Cost (£) | Optimised Cost (£) | Saving (£) | Saving (%) |
|------|--------------|-------------------|-----------|-----------|
| Week 1 | — | — | — | — |

---

### Experiment 5 — Full IoT-GPT Mini Demo | Week 8

**Goal:** Integrate all components into a working mini-version of IoT-GPT and record a 24-hour automated operation.

**System components required:**
- DHT22 sensor → publishing to MQTT
- Weather API → fetched every hour
- Smart bulb → receiving commands from brain
- Coordinator script (`iot_gpt_brain.py`) → making decisions
- InfluxDB + Grafana → logging and visualising all activity

**Record:** How many autonomous decisions did the system make in 24 hours? How many were correct?

---

## 6. Project Implementation Plan

### Milestones

| Milestone | Week | Deliverable | Done? |
|-----------|------|-------------|-------|
| M0 — Hardware setup | Week 1 | Pi running, SSH working, Python scripts executing | [ ] |
| M1 — First sensor reading | Week 2 | DHT22 logging to CSV, 24h data collected | [ ] |
| M2 — MQTT network live | Week 3 | Mosquitto + paho publishing sensor data | [ ] |
| M3 — Smart bulb paired | Week 4 | IKEA bulb controllable via Python over MQTT | [ ] |
| M4 — Weather light working | Week 5 | weather_light.py running 24/7, logs started | [ ] |
| M5 — Load experiment done | Week 6 | Simultaneous vs staggered power CSV filed | [ ] |
| M6 — InfluxDB + Grafana live | Week 6 | 48h dashboard showing sensor trends | [ ] |
| M7 — Scheduler validated | Week 7 | Off-peak savings calculated, result logged | [ ] |
| M8 — Mini IoT-GPT complete | Week 8 | 24h autonomous operation recorded | [ ] |
| M9 — Research contribution | Week 10 | GitHub pull request with data, code, or report | [ ] |
| M10 — Experiment report | Week 12 | 2-page write-up of findings submitted via GitHub | [ ] |

Tick off each milestone as you complete it. Share your progress in the **GitHub Discussions** tab.

### 6.1 How to Contribute on GitHub

1. Fork the repository: [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research) → Fork
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/iot-gpt-research`
3. Create a branch: `git checkout -b student/your-name-experiment-1`
4. Add your experiment data as CSV in: `students/your-name/`
5. Open a Pull Request with a short summary of what you found

> **Good First Contributions:** Experiment result CSVs · Bug fixes in sample code · New sample programs · Improvements to the beginner guide · Translation of docs · New device profiles for the DAR

---

## 7. Step-by-Step Setup Guide

Follow these steps in order on your first day with the hardware. Each step should take 10–20 minutes.

---

### Step 1 — Flash Raspberry Pi OS

1. Download Raspberry Pi Imager from [raspberrypi.com/software](https://www.raspberrypi.com/software/)
2. Insert microSD card into your laptop
3. Open Raspberry Pi Imager → Choose OS → **Raspberry Pi OS (64-bit)**
4. Click the gear icon (advanced options) → enable SSH, set hostname, set WiFi, set username/password
5. Write to card → wait 3–5 minutes → eject card
6. Insert card into Pi, connect HDMI + keyboard for first boot (or SSH directly if WiFi is set)

---

### Step 2 — First Boot and Update

```bash
# After login:
sudo apt update && sudo apt full-upgrade -y
sudo raspi-config    # expand filesystem, set locale/timezone, enable SSH

# Install essentials
sudo apt install -y python3-pip git vim mosquitto mosquitto-clients nodejs npm
pip3 install requests paho-mqtt adafruit-circuitpython-dht --break-system-packages
```

---

### Step 3 — Connect DHT22 Sensor

Wire the DHT22 to your Pi (3 connections):

| DHT22 Pin | Raspberry Pi Pin | Colour (typical) |
|-----------|-----------------|-----------------|
| VCC (+) | Pin 1 (3.3V) | Red |
| DATA | Pin 7 (GPIO 4) | Yellow |
| GND (-) | Pin 6 (GND) | Black |

> **Note:** Place a **10kΩ pull-up resistor** between VCC and DATA on the breadboard. Without it, readings may be unreliable.

```bash
# Test DHT22 reading
python3 -c "
import adafruit_dht, board, time
sensor = adafruit_dht.DHT22(board.D4)
time.sleep(2)
print(f'Temperature: {sensor.temperature:.1f}C')
print(f'Humidity: {sensor.humidity:.1f}%')
"
```

---

### Step 4 — Configure Mosquitto MQTT Broker

```bash
# Create config file
sudo nano /etc/mosquitto/conf.d/local.conf

# Add these lines:
listener 1883
allow_anonymous true

# Restart broker
sudo systemctl restart mosquitto
sudo systemctl enable mosquitto

# Test (open two terminals):
# Terminal 1: mosquitto_sub -t test/#
# Terminal 2: mosquitto_pub -t test/hello -m "world"
```

---

### Step 5 — Install and Configure Zigbee2MQTT

```bash
# Find your ZigBee dongle port
ls /dev/ttyUSB*     # should show /dev/ttyUSB0

# Install Zigbee2MQTT
sudo npm install -g zigbee2mqtt --unsafe-perm

# Create config directory and file
sudo mkdir -p /opt/zigbee2mqtt/data
sudo nano /opt/zigbee2mqtt/data/configuration.yaml
```

Paste this into `configuration.yaml`:

```yaml
homeassistant: false
permit_join: true
mqtt:
  base_topic: zigbee2mqtt
  server: mqtt://localhost
serial:
  port: /dev/ttyUSB0
frontend:
  port: 8080
```

```bash
# Start Zigbee2MQTT
sudo npx zigbee2mqtt

# You should see: "Started Zigbee2MQTT" in the log
```

---

### Step 6 — Pair Your IKEA Smart Bulb

1. Make sure Zigbee2MQTT is running (`permit_join: true` in config)
2. Put the bulb in the lamp socket and turn it on
3. **Factory reset:** rapidly switch power ON-OFF-ON-OFF-ON-OFF (6 times) — the bulb will blink to confirm
4. Watch the Zigbee2MQTT log — you should see "New device joined"
5. Note the device's friendly name (or set one in config)
6. Test control from command line:

```bash
# Turn bulb on
mosquitto_pub -t "zigbee2mqtt/YOUR_BULB/set" -m '{"state":"ON","brightness":200}'

# Set warm white
mosquitto_pub -t "zigbee2mqtt/YOUR_BULB/set" -m '{"color_temp":370}'

# Set blue (for snow alerts)
mosquitto_pub -t "zigbee2mqtt/YOUR_BULB/set" -m '{"color":{"x":0.14,"y":0.07}}'

# Turn off
mosquitto_pub -t "zigbee2mqtt/YOUR_BULB/set" -m '{"state":"OFF"}'
```

---

### Step 7 — Clone the Repository and Run Sample Code

```bash
# Clone the repo
git clone https://github.com/gsleo1976/iot-gpt-research
cd iot-gpt-research/samples

# Run the weather forecast program
python3 01_weather_forecast.py

# Run the calm light simulator
python3 07_calm_light_simulator.py

# Run the MQTT IoT simulator
python3 04_mqtt_iot_simulator.py
```

---

### Step 8 — Set Up Auto-Start on Boot

```bash
# Add to crontab so everything starts automatically after reboot
sudo crontab -e

# Add these lines:
@reboot sleep 10 && sudo systemctl start mosquitto
@reboot sleep 15 && cd /home/pi && python3 weather_light.py &
@reboot sleep 20 && sudo npx zigbee2mqtt &
```

> **You're ready!** If all 8 steps completed successfully, you have a working IoT-GPT prototype. Proceed to Section 4 to build the weather-light project, then work through the experiments in Section 5.

---

## 8. Troubleshooting Reference

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| DHT22 returns `None` or `RuntimeError` | Bad wiring or missing pull-up resistor | Check VCC=3.3V, add 10kΩ resistor between VCC and DATA |
| Can't SSH into Pi | SSH not enabled or wrong IP | Use raspi-config to enable SSH; find IP with `nmap` or router admin page |
| Mosquitto connection refused | Broker not running | `sudo systemctl start mosquitto`; check `sudo systemctl status mosquitto` |
| ZigBee dongle not found at `/dev/ttyUSB0` | Wrong port or missing drivers | `ls /dev/ttyUSB*`; try `/dev/ttyACM0`; check `dmesg \| grep usb` |
| Bulb not pairing | Not in factory reset mode | Switch on/off 6× rapidly; light blinks = reset successful; retry pairing |
| Weather API returning error | No internet or wrong coordinates | Check `ping 8.8.8.8`; verify lat/lon values in your script |
| InfluxDB won't start | Port 8086 already in use | `sudo lsof -i :8086`; kill conflicting process |
| Grafana dashboard shows no data | Wrong InfluxDB connection or bucket name | Verify bucket name; test query in InfluxDB Data Explorer first |
| `pip install` fails | Missing system packages | `sudo apt install python3-dev libgpiod2`; retry pip install |

---

## 9. Useful Links & Resources

| Resource | URL | What It Is |
|----------|-----|-----------|
| Research Repository | [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research) | All code, docs, and sample programs |
| Raspberry Pi Imager | [raspberrypi.com/software](https://www.raspberrypi.com/software/) | Flash OS to microSD card |
| Raspberry Pi GPIO Pinout | [pinout.xyz](https://pinout.xyz) | Interactive Pi pin diagram |
| Zigbee2MQTT Getting Started | [zigbee2mqtt.io/guide/getting-started](https://www.zigbee2mqtt.io/guide/getting-started/) | Pair and control ZigBee devices |
| Open-Meteo API | [open-meteo.com](https://open-meteo.com) | Free weather + AQI API (no key needed) |
| Paho MQTT Python Client | [pypi.org/project/paho-mqtt](https://pypi.org/project/paho-mqtt/) | MQTT library for Python |
| InfluxDB OSS Install | [docs.influxdata.com/influxdb/v2/install](https://docs.influxdata.com/influxdb/v2/install/) | Time-series database for sensor data |
| Grafana Installation | [grafana.com/docs/grafana/latest/setup-grafana](https://grafana.com/docs/grafana/latest/setup-grafana/) | Dashboard and alerting platform |
| MQTT Explorer (desktop app) | [mqtt-explorer.com](https://mqtt-explorer.com) | GUI tool to browse all MQTT topics |
| MicroPython (optional) | [micropython.org](https://micropython.org) | Python for microcontrollers (ESP32, Pico) |

---

*IoT-GPT Research Project · Gurdev Singh · gurdev.leo@gmail.com · [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research)*
