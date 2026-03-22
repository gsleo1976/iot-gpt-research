# 🗂️ Repository Navigator

Complete index of everything in this repo — documents, slides, guides, sample code, and experiments.

---

## 📁 Root

| File | Description |
|------|-------------|
| [`README.md`](README.md) | Project overview, architecture, experiments, timeline, and how to get involved |
| [`navigator.md`](navigator.md) | This file — full index of the entire repository |

---

## 📁 docs/

Documents are organised by content type and numbered in order of creation.

### 📂 docs/word/  — Word Documents

| # | File | Description |
|---|------|-------------|
| 01 | [`docs/word/01-IoT-GPT-Research-Proposal.docx`](docs/word/01-IoT-GPT-Research-Proposal.docx) | Full research proposal — background, methodology, architecture, experiments, expected outcomes |
| 02 | [`docs/word/02-IoT-GPT-Beginner-Guide.docx`](docs/word/02-IoT-GPT-Beginner-Guide.docx) | Hardware & software setup guide — Raspberry Pi, MQTT, DHT22 wiring, InfluxDB, Grafana |
| 06 | [`docs/word/06-IoT-GPT-Student-Contribution-Guide.docx`](docs/word/06-IoT-GPT-Student-Contribution-Guide.docx) | Student onboarding guide — 12-week daily plan, shopping list, 5 experiments, step-by-step setup |

### 📂 docs/slides/  — Presentations

| # | File | Description |
|---|------|-------------|
| 03 | [`docs/slides/03-IoT-GPT-Research-Presentation.pptx`](docs/slides/03-IoT-GPT-Research-Presentation.pptx) | 17-slide PowerPoint — research overview (1–10), student participation (11–15), 15 use cases (16), student roadmap (17) |
| 04 | [`docs/slides/04-presentation-slides.md`](docs/slides/04-presentation-slides.md) | All presentation slides as Markdown — same content as .pptx, web-readable without PowerPoint |

### 📂 docs/guides/  — Markdown Guides

| # | File | Description |
|---|------|-------------|
| 05 | [`docs/guides/05-learning-path.md`](docs/guides/05-learning-path.md) | 15-topic learning path across 4 phases — from beginner to advanced, with direct links to free resources |
| 07 | [`docs/guides/07-student-contribution-guide.md`](docs/guides/07-student-contribution-guide.md) | Student contribution guide in Markdown — 12-week plan, hardware shopping list (Amazon India), 5 experiments, full setup walkthrough |

---

## 📁 samples/  — Python Sample Programs

| File | What It Does |
|------|--------------|
| [`samples/README.md`](samples/README.md) | Overview of all 10 sample programs + hardware shopping list |
| [`samples/01_weather_forecast.py`](samples/01_weather_forecast.py) | Fetches weather forecast and triggers a snow alert using wttr.in API |
| [`samples/02_lan_device_scanner.py`](samples/02_lan_device_scanner.py) | Scans your local network, discovers devices by IP, hostname, and type |
| [`samples/03_smart_device_scheduler.py`](samples/03_smart_device_scheduler.py) | Schedules water heater + room heater to avoid peak hours and simultaneous loads |
| [`samples/04_mqtt_iot_simulator.py`](samples/04_mqtt_iot_simulator.py) | Simulates a full MQTT IoT setup — temperature sensors, smart heater, and IoT-GPT brain |
| [`samples/05_air_quality_monitor.py`](samples/05_air_quality_monitor.py) | Checks outdoor air quality (Open-Meteo AQI) and decides when to open windows or run a purifier |
| [`samples/06_sensor_data_logger.py`](samples/06_sensor_data_logger.py) | Logs simulated sensor data to CSV and performs trend analysis |
| [`samples/07_calm_light_simulator.py`](samples/07_calm_light_simulator.py) | Demonstrates the calm notification engine — ambient colour signals for 5 real-world events |
| [`samples/08_energy_usage_tracker.py`](samples/08_energy_usage_tracker.py) | Profiles 10 home devices, calculates peak vs. off-peak costs, exports CSV report |
| [`samples/09_device_attribute_registry.py`](samples/09_device_attribute_registry.py) | Loads the Device Attribute Registry (DAR), detects device conflicts, runs an IoT-GPT Q&A demo |
| [`samples/10_sunrise_and_automation.py`](samples/10_sunrise_and_automation.py) | Fetches sunrise/sunset times and builds a sun-aware daily automation schedule |

---

## 📁 experiments/  — Experiment Results & Templates

Student contributors submit their experiment results here as filled-in Markdown reports.

| File | Description |
|------|-------------|
| [`experiments/experiment-template.md`](experiments/experiment-template.md) | **Start here** — copy this template, rename it, and fill in your results before opening a pull request |

**Naming convention for your report:**
```
exp-<number>-<short-name>-<your-name>-<YYYY-MM>.md
```
Example: `exp-01-weather-signal-light-gurdev-2026-03.md`

**Experiment numbers map to the student guide:**

| # | Experiment | Reference |
|---|-----------|-----------|
| 01 | Weather Signal Light | [guide § 5.1](docs/guides/07-student-contribution-guide.md#experiment-1--weather-signal-light-starter--week-45) |
| 02 | Simultaneous Load Logger | [guide § 5.2](docs/guides/07-student-contribution-guide.md#experiment-2--simultaneous-load-logger--week-56) |
| 03 | Multi-Sensor MQTT Network | [guide § 5.3](docs/guides/07-student-contribution-guide.md#experiment-3--multi-sensor-mqtt-network--week-56) |
| 04 | Off-Peak Scheduler Validation | [guide § 5.4](docs/guides/07-student-contribution-guide.md#experiment-4--off-peak-scheduler-validation--week-7) |
| 05 | Full IoT-GPT Mini Demo | [guide § 5.5](docs/guides/07-student-contribution-guide.md#experiment-5--full-iot-gpt-mini-demo--week-8) |
