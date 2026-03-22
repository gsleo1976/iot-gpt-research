# 🗂️ Repository Navigator

Complete index of everything in this repo — documents, slides, guides, sample code, and experiments.
Files within each folder are numbered in order of creation.

---

## 📁 Root

| File | Description |
|------|-------------|
| [`README.md`](README.md) | Project overview, architecture, experiments, timeline, and how to get involved |
| [`navigator.md`](navigator.md) | This file — full index of the entire repository |

---

## 📁 docs/

### 📂 docs/word/ — Word Documents

| # | File | Description |
|---|------|-------------|
| 01 | [`docs/word/01-IoT-GPT-Research-Proposal.docx`](docs/word/01-IoT-GPT-Research-Proposal.docx) | Full research proposal — background, methodology, architecture, experiments, expected outcomes |
| 02 | [`docs/word/02-IoT-GPT-Beginner-Guide.docx`](docs/word/02-IoT-GPT-Beginner-Guide.docx) | Hardware & software setup guide — Raspberry Pi, MQTT, DHT22 wiring, InfluxDB, Grafana |
| 03 | [`docs/word/03-IoT-GPT-Student-Contribution-Guide.docx`](docs/word/03-IoT-GPT-Student-Contribution-Guide.docx) | Student onboarding guide — 12-week daily plan, hardware shopping list (INR / Amazon India), 5 experiments, step-by-step setup |

### 📂 docs/slides/ — Presentations

| # | File | Description |
|---|------|-------------|
| 01 | [`docs/slides/01-IoT-GPT-Research-Presentation.pptx`](docs/slides/01-IoT-GPT-Research-Presentation.pptx) | 17-slide deck — research overview (1–10), student participation (11–15), 15 use cases (16), student roadmap (17) |
| 02 | [`docs/slides/02-presentation-slides.md`](docs/slides/02-presentation-slides.md) | All 17 slides as Markdown — same content as .pptx, readable without PowerPoint |

### 📂 docs/guides/ — Markdown Guides

| # | File | Description |
|---|------|-------------|
| 04 | [`docs/guides/04-learning-path.md`](docs/guides/04-learning-path.md) | 15-topic learning path across 4 phases — beginner to advanced, with direct links to free resources |
| 01 | [`docs/guides/01-IoT-GPT-Research-Proposal.md`](docs/guides/01-IoT-GPT-Research-Proposal.md) | Full research proposal in Markdown — background, methodology, architecture, experiments, expected outcomes |
| 02 | [`docs/guides/02-IoT-GPT-Beginner-Guide.md`](docs/guides/02-IoT-GPT-Beginner-Guide.md) | Hardware & software setup guide — Raspberry Pi, MQTT, DHT22 wiring, InfluxDB, Grafana (INR prices, Amazon India links) |
| 03 | [`docs/guides/03-IoT-GPT-Student-Contribution-Guide.md`](docs/guides/03-IoT-GPT-Student-Contribution-Guide.md) | Student onboarding guide — 12-week daily plan, hardware shopping list (INR / Amazon India), 5 experiments, step-by-step setup |

---

## 📁 samples/ — Python Sample Programs

| File | What It Does |
|------|--------------|
| [`samples/README.md`](samples/README.md) | Overview of all 10 sample programs + hardware shopping list |
| [`samples/01_weather_forecast.py`](samples/01_weather_forecast.py) | Fetches weather forecast; triggers a snow alert using wttr.in API |
| [`samples/02_lan_device_scanner.py`](samples/02_lan_device_scanner.py) | Scans your local network; discovers devices by IP, hostname, and type |
| [`samples/03_smart_device_scheduler.py`](samples/03_smart_device_scheduler.py) | Schedules water heater + room heater to avoid peak hours and simultaneous loads |
| [`samples/04_mqtt_iot_simulator.py`](samples/04_mqtt_iot_simulator.py) | Simulates a full MQTT IoT setup — temperature sensors, smart heater, IoT-GPT brain |
| [`samples/05_air_quality_monitor.py`](samples/05_air_quality_monitor.py) | Checks outdoor AQI (Open-Meteo) and decides when to open windows or run a purifier |
| [`samples/06_sensor_data_logger.py`](samples/06_sensor_data_logger.py) | Logs simulated sensor data to CSV and performs trend analysis |
| [`samples/07_calm_light_simulator.py`](samples/07_calm_light_simulator.py) | Demonstrates the calm notification engine — ambient colour signals for 5 real-world scenarios |
| [`samples/08_energy_usage_tracker.py`](samples/08_energy_usage_tracker.py) | Profiles 10 home devices; calculates peak vs. off-peak costs; exports CSV |
| [`samples/09_device_attribute_registry.py`](samples/09_device_attribute_registry.py) | Loads the Device Attribute Registry (DAR); detects conflicts; runs IoT-GPT Q&A demo |
| [`samples/10_sunrise_and_automation.py`](samples/10_sunrise_and_automation.py) | Fetches sunrise/sunset times; builds a sun-aware daily automation schedule |

---

## 📁 experiments/ — Experiment Results & Templates

Student contributors submit filled-in experiment reports here as Markdown files.

| File | Description |
|------|-------------|
| [`experiments/experiment-template.md`](experiments/experiment-template.md) | **Start here** — copy, rename, fill in your results, then open a pull request |

**File naming convention:**
```
exp-<number>-<short-name>-<your-name>-<YYYY-MM>.md
```
Example: `exp-01-weather-signal-light-gurdev-2026-03.md`

**Experiment numbers:**

| # | Experiment | Guide Reference |
|---|-----------|----------------|
| 01 | Weather Signal Light | [Student Guide § 5.1](docs/guides/02-student-contribution-guide.md#experiment-1--weather-signal-light-starter--week-45) |
| 02 | Simultaneous Load Logger | [Student Guide § 5.2](docs/guides/02-student-contribution-guide.md#experiment-2--simultaneous-load-logger--week-56) |
| 03 | Multi-Sensor MQTT Network | [Student Guide § 5.3](docs/guides/02-student-contribution-guide.md#experiment-3--multi-sensor-mqtt-network--week-56) |
| 04 | Off-Peak Scheduler Validation | [Student Guide § 5.4](docs/guides/02-student-contribution-guide.md#experiment-4--off-peak-scheduler-validation--week-7) |
| 05 | Full IoT-GPT Mini Demo | [Student Guide § 5.5](docs/guides/02-student-contribution-guide.md#experiment-5--full-iot-gpt-mini-demo--week-8) |

---

## 🛒 Hardware Quick-Buy Reference (Amazon India)

| Device | Price | Amazon India Link |
|--------|-------|------------------|
| Raspberry Pi 5 (4 GB) | ₹7,999 | [amazon.in](https://www.amazon.in/s?k=raspberry+pi+5+4gb) |
| Raspberry Pi USB-C Power Supply (27W) | ₹1,299 | [amazon.in](https://www.amazon.in/s?k=raspberry+pi+5+power+supply+27w) |
| SanDisk MicroSD 32 GB (Class 10 / A1) | ₹399 | [amazon.in](https://www.amazon.in/s?k=sandisk+microsd+32gb+class+10) |
| DHT22 Temperature & Humidity Sensor | ₹249 | [amazon.in](https://www.amazon.in/s?k=DHT22+temperature+humidity+sensor) |
| Breadboard + Jumper Wires Kit | ₹299 | [amazon.in](https://www.amazon.in/s?k=breadboard+jumper+wires+kit+electronics) |
| SONOFF Zigbee 3.0 USB Dongle Plus | ₹1,899 | [amazon.in](https://www.amazon.in/s?k=sonoff+zigbee+3.0+usb+dongle+plus) |
| IKEA TRADFRI E27 White Spectrum Bulb | ₹999 | [ikea.com/in](https://www.ikea.com/in/en/cat/smart-lighting-36812/) · [amazon.in](https://www.amazon.in/s?k=IKEA+TRADFRI+E27+white+smart+bulb) |
| IKEA TRADFRI E27 Colour Bulb (RGB) | ₹1,799 | [ikea.com/in](https://www.ikea.com/in/en/cat/smart-lighting-36812/) · [amazon.in](https://www.amazon.in/s?k=IKEA+TRADFRI+E27+colour+smart+bulb) |
| Desk lamp with E27 socket | ₹699 | [amazon.in](https://www.amazon.in/s?k=desk+lamp+e27+bulb+holder) |
| TP-Link Tapo P110 Smart Plug (energy monitor) | ₹2,199 | [amazon.in](https://www.amazon.in/s?k=tp-link+tapo+p110+smart+plug) |
| Second Smart Plug (energy metering) | ₹999 | [amazon.in](https://www.amazon.in/s?k=smart+plug+energy+monitor+india) |
| **Starter kit total** | **~₹10,000** | Items 1–5 above |
| **Full kit total** | **~₹19,000** | All 11 items above |
