# Experiment Report — [Experiment Title]

> **Copy this file and rename it** before filling it in.
> Example filename: `exp-01-weather-signal-light-gurdev-2026-03.md`

---

## Metadata

| Field | Value |
|-------|-------|
| **Experiment #** | e.g. 01 |
| **Experiment Name** | e.g. Weather Signal Light |
| **Contributor Name** | Your name |
| **GitHub Username** | @your-handle |
| **Date Started** | YYYY-MM-DD |
| **Date Completed** | YYYY-MM-DD |
| **Raspberry Pi Model** | e.g. Raspberry Pi 5 (4 GB) |
| **Location / City** | e.g. Bengaluru, India |

---

## 1. Objective

> What are you trying to find out or prove with this experiment?

_Write 2–4 sentences describing the goal._

---

## 2. Hypothesis

> What do you expect to happen, and why?

_Write 1–3 sentences._

---

## 3. Hardware Used

| Device | Model / Version | Qty |
|--------|----------------|-----|
| Single-board computer | Raspberry Pi 5 (4 GB) | 1 |
| Sensor | DHT22 | 1 |
| Smart bulb | IKEA TRADFRI E27 Colour | 1 |
| ZigBee coordinator | SONOFF USB Dongle Plus | 1 |
| Smart plug | TP-Link Kasa (with energy meter) | 1 |
| _Add more rows as needed_ | | |

---

## 4. Software & Libraries

| Component | Version |
|-----------|---------|
| Raspberry Pi OS | e.g. Bookworm 64-bit |
| Python | e.g. 3.11 |
| paho-mqtt | e.g. 1.6.1 |
| Zigbee2MQTT | e.g. 1.36.0 |
| Mosquitto | e.g. 2.0.18 |
| Sample program used | e.g. `samples/01_weather_forecast.py` |
| _Add more rows as needed_ | |

---

## 5. Setup & Method

> Step-by-step description of how you ran the experiment.

1. _Step one..._
2. _Step two..._
3. _..._

**Any deviations from the guide?**
_Note any changes you made to the standard setup — different hardware, different parameters, etc._

---

## 6. Raw Results

> Paste your CSV data, copy a table, or link to a file in this folder.

### Option A — Paste data table

| Timestamp | Measurement 1 | Measurement 2 | Notes |
|-----------|--------------|--------------|-------|
| 2026-MM-DD HH:MM | — | — | |

### Option B — Link to CSV file

Data saved in: `[filename.csv](filename.csv)` _(place the CSV in this same experiments/ folder)_

---

## 7. Analysis

> What patterns, trends, or anomalies did you observe?

_Write your analysis here. Include numbers where possible._

**Key metrics:**

| Metric | Value |
|--------|-------|
| Duration of experiment | e.g. 7 days |
| Total data points collected | e.g. 168 (hourly readings) |
| Success rate / accuracy | e.g. 82% forecasts matched actual weather |
| Energy saved (if applicable) | e.g. 28% reduction vs. naive scheduling |
| Peak demand reduction (if applicable) | e.g. from 4,800W to 3,200W |

---

## 8. Observations & Surprises

> What did you notice that you didn't expect?

- _Observation 1_
- _Observation 2_
- _..._

---

## 9. Conclusion

> Did the results match your hypothesis? What does this mean for the IoT-GPT project?

_Write 3–5 sentences summarising what you found and what it implies._

---

## 10. Issues Encountered

> Any problems during setup or runtime? How did you solve them?

| Issue | How Resolved |
|-------|-------------|
| _e.g. DHT22 returning None_ | _Added 10kΩ pull-up resistor between VCC and DATA_ |
| | |

---

## 11. Suggested Improvements

> What would you change if you ran this experiment again?

- _Suggestion 1_
- _Suggestion 2_

---

## 12. Reproducibility Checklist

Before submitting your pull request, confirm the following:

- [ ] Raw data CSV is included (or pasted above)
- [ ] All software versions are noted in Section 4
- [ ] Any custom code is committed to `students/your-name/` in the repo
- [ ] Hardware deviations are noted in Section 5
- [ ] Results section has actual numbers, not just "it worked"

---

## 13. References

> Any articles, docs, or prior work you relied on.

- [IoT-GPT Research Repository](https://github.com/gsleo1976/iot-gpt-research)
- [Open-Meteo API Docs](https://open-meteo.com/en/docs)
- _Add more as needed_

---

*Submitted to: [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research) · IoT Research for Sustainability and Calm Technology*
