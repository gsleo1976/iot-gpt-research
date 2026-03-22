# IoT-GPT Research Project — Beginner's Guide to Experimental Setup

**How to Build a Smart Home IoT Research Lab from Scratch**

*For students and researchers with little to no IoT experience*

Version 1.0 | March 2026

---

## 1. Introduction

This guide walks you through everything you need to set up the IoT-GPT experimental environment — even if you have never worked with IoT devices, Raspberry Pi, or smart home technology before. By the end of this guide, you will have a working smart home testbed that can run all six experiments described in the IoT-GPT research project.

The guide is organized into clear, numbered steps. Each step includes what you need (hardware, software, or knowledge), step-by-step instructions, how to verify it worked, and what to do if something goes wrong.

> **💡 Tip:** No prior experience with IoT or hardware is required. Each step builds on the previous one. Take your time — the setup typically takes 1–2 days on a first attempt.

### 1.1 What Is IoT-GPT?

IoT-GPT is an intelligent home automation system that:

- Learns the attributes of every connected device (power draw, warm-up time, conflicts with other devices, etc.)
- Coordinates multiple devices together — for example, scheduling the water heater and room heater so they never run at the same time, avoiding circuit overload
- Uses calm technology — ambient light signals instead of phone notifications — to inform you without interrupting your focus
- Runs entirely on a Raspberry Pi at the edge of your home network, with no cloud service required

### 1.2 What You Will Build

Your experimental setup will consist of:

- 1 Raspberry Pi 5 running the full IoT-GPT software stack
- 2–3 ZigBee-connected smart devices (heaters, smart bulb, or sensors)
- A temperature and humidity sensor (DHT22) wired to the Pi GPIO pins
- An MQTT network for all device communication
- A data logging pipeline using InfluxDB and Grafana dashboards

---

## 2. What You Need (Shopping List)

### 2.1 Hardware

| Item | Model / Spec | Cost (INR) | Where to Buy |
|------|-------------|-----------|--------------|
| Raspberry Pi 5 | 4GB or 8GB RAM | ~₹7,999 | [amazon.in](https://www.amazon.in/s?k=raspberry+pi+5+4gb) |
| MicroSD Card | SanDisk 32GB Class 10 / A1 | ~₹399 | [amazon.in](https://www.amazon.in/s?k=sandisk+microsd+32gb+class+10) |
| Power Supply | Official Pi 5 PSU (27W USB-C) | ~₹1,299 | [amazon.in](https://www.amazon.in/s?k=raspberry+pi+5+power+supply+27w) |
| ZigBee USB Dongle | SONOFF Zigbee 3.0 USB Dongle Plus | ~₹1,899 | [amazon.in](https://www.amazon.in/s?k=sonoff+zigbee+3.0+usb+dongle+plus) |
| Smart LED Bulb | IKEA TRÅDFRI E27 White Spectrum | ~₹999 | [amazon.in](https://www.amazon.in/s?k=IKEA+TRADFRI+E27+white+smart+bulb) |
| Smart LED Bulb (RGB) | IKEA TRÅDFRI E27 Colour | ~₹1,799 | [amazon.in](https://www.amazon.in/s?k=IKEA+TRADFRI+E27+colour+smart+bulb) |
| DHT22 Sensor | Temperature + Humidity | ~₹249 | [amazon.in](https://www.amazon.in/s?k=DHT22+temperature+humidity+sensor) |
| Breadboard + Jumper Wires | Kit with female-to-male wires | ~₹299 | [amazon.in](https://www.amazon.in/s?k=breadboard+jumper+wires+kit+electronics) |
| Smart Plug | TP-Link Tapo P110 (energy monitoring) | ~₹2,199 | [amazon.in](https://www.amazon.in/s?k=tp-link+tapo+p110+smart+plug) |
| Desk Lamp | With E27 socket | ~₹699 | [amazon.in](https://www.amazon.in/s?k=desk+lamp+e27+bulb+holder) |
| **Starter Kit Total** | Items 1–4 + sensor + wires | **~₹10,000** | |
| **Full Kit Total** | All items above | **~₹19,000** | |

> **⚠ Note:** The Raspberry Pi 5 may be out of stock at times. The Raspberry Pi 4 (4GB) works fine as an alternative for all experiments.

### 2.2 Software (All Free)

| Software | Purpose | How to Install |
|----------|---------|----------------|
| Raspberry Pi OS 64-bit | Operating system | Raspberry Pi Imager tool |
| Python 3.11+ | Running IoT-GPT code | Pre-installed on Pi OS |
| Mosquitto | MQTT broker for device messaging | `sudo apt install mosquitto` |
| Zigbee2MQTT | Connect ZigBee devices to MQTT | `npm install -g zigbee2mqtt` |
| InfluxDB 2.x | Store time-series sensor data | Official InfluxDB package |
| Grafana | Visualize sensor data in dashboards | Official Grafana package |
| Node-RED (optional) | Visual IoT programming | `sudo npm install -g node-red` |
| VS Code + Remote SSH | Code from your laptop | code.visualstudio.com |

---

## 3. Setting Up the Raspberry Pi

### 3.1 Install the Operating System

Download and install Raspberry Pi Imager on your laptop:

```
https://www.raspberrypi.com/software/
```

Open Raspberry Pi Imager and follow these steps:

1. Click **CHOOSE DEVICE** and select **Raspberry Pi 5**
2. Click **CHOOSE OS** and select **Raspberry Pi OS (64-bit)**
3. Click **CHOOSE STORAGE** and select your microSD card
4. Click the gear icon ⚙ to pre-configure hostname, username, password, and Wi-Fi
5. Click **WRITE** and wait for it to finish (~5 minutes)

> **💡 Tip:** Pre-configuring Wi-Fi and SSH means you can use the Pi without a monitor. Just power it on and connect via SSH from your laptop.

### 3.2 First Boot and SSH Connection

Insert the microSD into the Pi, connect power, and wait 2 minutes. Then SSH in from your laptop:

```bash
ssh pi@raspberrypi.local
```

Update system packages (takes 10–20 minutes):

```bash
sudo apt update && sudo apt upgrade -y
```

> **⚠ Note:** Do not turn off the Pi while updating. Let the upgrade complete fully.

---

## 4. Installing the MQTT Broker (Mosquitto)

MQTT is the messaging protocol that IoT devices use to communicate. Think of it like a group chat: devices publish messages to "topics" and other devices subscribe to receive them.

### 4.1 Install Mosquitto

```bash
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### 4.2 Test the Broker

Open two terminal windows on the Pi. In **window 1**, subscribe to a test topic:

```bash
mosquitto_sub -t 'iot/test' -v
```

In **window 2**, publish a message:

```bash
mosquitto_pub -t 'iot/test' -m 'Hello from IoT-GPT!'
```

The message should appear in window 1. If it does, MQTT is working!

### 4.3 Configure for Your Network

Allow connections from devices on your local network:

```bash
sudo nano /etc/mosquitto/mosquitto.conf
```

Add at the end of the file:

```
listener 1883
allow_anonymous true
```

Save and restart:

```bash
sudo systemctl restart mosquitto
```

---

## 5. Connecting Your First Sensor (DHT22)

The DHT22 sensor measures temperature and humidity. It connects directly to the Raspberry Pi GPIO pins using just three wires. No soldering required!

### 5.1 Wiring

| DHT22 Pin | Raspberry Pi Pin | Wire Color |
|-----------|-----------------|-----------|
| VCC (+) | Pin 1 (3.3V Power) | Red |
| DATA | Pin 7 (GPIO 4) | Yellow |
| GND (−) | Pin 6 (Ground) | Black |

> **💡 Tip:** The DHT22 has 4 pins but you only use 3. Leave the third pin (labeled NC = No Connect) empty.

### 5.2 Install the Library

```bash
pip3 install adafruit-circuitpython-dht --break-system-packages
sudo apt install libgpiod2
```

### 5.3 Read Sensor Data

Create and run a test script:

```python
import adafruit_dht, board, time

sensor = adafruit_dht.DHT22(board.D4)

for i in range(5):
    print(f'Temp: {sensor.temperature}C  Humidity: {sensor.humidity}%')
    time.sleep(2)
```

> **⚠ Note:** DHT22 sometimes fails on the first read. This is normal. The script retries automatically. If it consistently fails, re-check the wiring.

---

## 6. Data Logging with InfluxDB and Grafana

InfluxDB stores your sensor data over time like a diary for numbers. Grafana turns that data into real-time charts and dashboards.

### 6.1 Install InfluxDB

```bash
sudo apt update && sudo apt install influxdb2
sudo systemctl enable influxdb && sudo systemctl start influxdb
```

Open the setup UI at: **http://raspberrypi.local:8086**

Create an organization, a bucket named `iot_gpt`, and save the API token shown on screen.

### 6.2 Install Grafana

```bash
sudo apt install -y grafana
sudo systemctl enable grafana-server && sudo systemctl start grafana-server
```

Open Grafana at: **http://raspberrypi.local:3000** (default login: admin / admin)

> **💡 Tip:** In Grafana, add InfluxDB as a data source and create a dashboard with temperature and humidity panels for a live view of your sensor.

---

## 7. Running Your First Experiment

### 7.1 Energy Baseline (Experiment 1 Preview)

Before testing IoT-GPT, measure baseline energy usage for one week with a manual schedule:

1. Connect the TP-Link Tapo P110 smart plug to your heater outlet
2. Install the Python library: `pip3 install python-kasa --break-system-packages`
3. Run the baseline energy logger from the samples folder:

```bash
python3 samples/08_energy_usage_tracker.py
```

### 7.2 What Good Data Looks Like

After a week of logging, your Grafana dashboard should show:

- Temperature readings arriving every 60 seconds with no gaps
- Daily energy usage per device clearly visible in kWh
- Peak usage during morning (6–9 AM) and evening (5–8 PM) hours

### 7.3 Auto-Start on Boot

Set your IoT-GPT scripts to start automatically when the Pi boots:

```bash
sudo nano /etc/systemd/system/iotgpt.service
```

Paste this content:

```ini
[Unit]
Description=IoT-GPT Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/iot-gpt/main.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable iotgpt && sudo systemctl start iotgpt
```

---

## 8. Troubleshooting Common Problems

| Problem | Likely Cause | Solution |
|---------|-------------|---------|
| Can't SSH into Pi | Pi not on network or wrong hostname | Use the Pi's IP address directly. Check your router's device list. |
| DHT22 shows errors | Loose wiring or reading too fast | Check wiring. Add `time.sleep(2)` between reads. |
| MQTT messages not received | Broker not started or firewall | Run: `sudo systemctl status mosquitto` |
| InfluxDB will not start | Port conflict or low memory | Check: `journalctl -u influxdb`. Try rebooting. |
| Grafana shows no data | Wrong data source settings | Re-enter InfluxDB URL and token in Grafana. |
| ZigBee not pairing | Wrong USB port or firmware | Unplug and replug dongle. Check Zigbee2MQTT logs. |
| Python import errors | Library not installed | Run: `pip3 install <library_name> --break-system-packages` |

---

## 9. Next Steps and Resources

### 9.1 After Basic Setup

1. Run all 10 sample Python programs in the `samples/` folder to learn each concept
2. Connect your ZigBee smart bulb and test calm light notifications (`samples/07_calm_light_simulator.py`)
3. Try the full smart device scheduling simulation (`samples/03_smart_device_scheduler.py`)
4. Start the 7-day energy baseline measurement for Experiment 1
5. Join the weekly research team meetings (schedule on GitHub)

### 9.2 Useful Resources

| Resource | URL / Location | What It Is |
|----------|---------------|-----------|
| Project GitHub | [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research) | All code, docs, and data |
| Raspberry Pi Docs | raspberrypi.com/documentation | Official Pi guides |
| MQTT Essentials | hivemq.com/mqtt-essentials | Free MQTT learning series |
| InfluxDB Docs | docs.influxdata.com | Database setup and queries |
| Zigbee2MQTT | zigbee2mqtt.io | Connect any ZigBee device |
| Adafruit DHT Guide | learn.adafruit.com/dht | Sensor wiring and code |

### 9.3 Getting Help

- Post questions in the team shared chat (link in GitHub repo)
- Weekly lab sessions: every Saturday 10am–12pm (virtual)
- Email the project lead: gurdev.leo@gmail.com
- GitHub Issues: open an issue at the repository for technical bugs

---

**You're ready to start! The best way to learn IoT is to build something.**

*Run the sample programs, break things, fix them, and have fun!*

— IoT-GPT Research Team

---

*Submitted to: [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research) · IoT Research for Sustainability and Calm Technology*
