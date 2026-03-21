# IoT-GPT Sample Programs

10 beginner-friendly Python programs that demonstrate core IoT-GPT concepts. Each program runs independently and is heavily commented for learning.

## Programs

| # | File | What It Does | Libraries Needed |
|---|------|-------------|-----------------|
| 01 | `01_weather_forecast.py` | Fetch weather forecast for any city. Includes IoT-GPT snow alert logic. | `requests` |
| 02 | `02_lan_device_scanner.py` | Discover all devices on your home network (phones, PCs, IoT devices). | Built-in only |
| 03 | `03_smart_device_scheduler.py` | Schedule water heater + room heater to avoid peak load and save money. | Built-in only |
| 04 | `04_mqtt_iot_simulator.py` | Simulate MQTT messaging between sensors and IoT-GPT brain. | `paho-mqtt` (optional) |
| 05 | `05_air_quality_monitor.py` | Real-time air quality index for any city. IoT-GPT decides to open windows or run air purifier. | `requests` |
| 06 | `06_sensor_data_logger.py` | Log temperature, humidity, CO2, and motion data to CSV. Analyze trends. | Built-in only |
| 07 | `07_calm_light_simulator.py` | Simulate the calm technology notification system (shoe-rack light colors). | Built-in only |
| 08 | `08_energy_usage_tracker.py` | Compare energy costs before and after IoT-GPT optimization. | Built-in only |
| 09 | `09_device_attribute_registry.py` | Explore the Device Attribute Registry — the knowledge base of IoT-GPT. | Built-in only |
| 10 | `10_sunrise_and_automation.py` | Schedule devices based on real sunrise/sunset data — adapts to seasons! | `requests` |

## Quick Start

```bash
# Install required libraries (only two external ones needed)
pip install requests paho-mqtt

# Run any program
python 01_weather_forecast.py
python 03_smart_device_scheduler.py
python 07_calm_light_simulator.py
```

> **All programs work offline** — they detect connection failures and show sample output so you can learn even without internet.

## What You'll Learn

- How to call free public APIs (weather, air quality, sunrise)
- How to scan a local network using Python
- How to log sensor data to CSV files
- How MQTT messaging works in IoT systems
- How energy scheduling reduces electricity bills
- What "calm technology" means and how to implement it
- How a Device Attribute Registry stores smart home knowledge

## Next Steps After Running These

1. **Get a Raspberry Pi 5** — run these programs on real hardware
2. **Add a real sensor** — DHT22 (temperature/humidity) costs ~$5
3. **Install Mosquitto** — a real MQTT broker for your home network
4. **Connect a smart bulb** — Philips Hue or IKEA TRÅDFRI via ZigBee
5. **Join the research team** — see the main README for how to participate!

## Hardware Shopping List (under $100 CAD)

| Item | Cost (approx.) | Where to Buy |
|------|---------------|-------------|
| Raspberry Pi 5 (4GB) | $60 | raspberrypi.com / local electronics |
| DHT22 sensor | $5 | Amazon |
| Smart LED bulb (ZigBee) | $15 | IKEA TRÅDFRI |
| ZigBee USB dongle | $20 | Amazon (SONOFF Zigbee 3.0 USB Dongle) |
| microSD card (32GB) | $8 | Any electronics store |

**Total: ~$108 CAD** for a complete IoT-GPT starter kit!
