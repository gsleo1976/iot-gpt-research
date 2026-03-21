# IoT-GPT Research — Presentation Slides

**Intelligent IoT Coordination for Sustainable Living**
A Research Project on Smart Home Automation & Calm Technology

> Gurdev Singh · gsleo1976 · March 2026
> [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research)

---

## Slide 1 — Title

# IoT-GPT

**Intelligent IoT Coordination for Sustainable Living**
*A Research Project on Smart Home Automation & Calm Technology*

Gurdev Singh · gsleo1976 · March 2026
github.com/gsleo1976/iot-gpt-research

---

## Slide 2 — The Problem We're Solving

### Energy Waste
- Room heater + water heater running simultaneously draw 3,500W — can trip the circuit breaker
- Peak electricity hours (6–9 AM, 5–8 PM) are 2× more expensive
- Average home wastes 20–30% energy on poor device scheduling

### Notification Overload
- Smartphones buzz 80+ times per day on average
- Every alert pulls you out of focus and increases stress
- Most smart home alerts are low-priority and interruptible
- We need **ambient, calm** ways to stay informed

> **IoT-GPT solves both problems** — intelligent coordination + calm technology.

---

## Slide 3 — What is IoT-GPT?

> *A smart AI brain that understands every device in your home*

### 🧠 Device Expert
Knows every device's power draw, warmup time, and conflicts. Never runs the room heater and water heater at the same time.

### 📅 Smart Scheduler
Plans your morning routine — water heats by 6:58 AM, room warms by 6:40 AM — all before you wake up at 7:00 AM.

### 💡 Calm Notifier
A shoe-rack smart bulb glows soft **blue** if snow is forecast. No buzzing. No popup. Just a gentle ambient glow.

### ⚡ Energy Optimizer
Shifts high-power devices to off-peak hours automatically. **Target: 15–25% energy reduction.**

---

## Slide 4 — System Architecture

| Layer | Components |
|-------|-----------|
| **Physical Layer** | DHT22 sensors · ZigBee smart bulbs · Smart heaters · Power meters |
| **Protocol Layer** | ZigBee (via Zigbee2MQTT) + MQTT Broker (Mosquitto) on Raspberry Pi 5 |
| **Intelligence Layer** | Device Attribute Registry (DAR) · Coordination Engine (OR-Tools) · Mistral-7B LLM |
| **Application Layer** | Calm Notification Controller · Energy Optimizer · Scheduling Engine |
| **Data Layer** | InfluxDB (time-series storage) · Grafana (dashboards) · Node-RED (flows) |

> All components run **locally on Raspberry Pi 5** · No cloud dependency · Privacy by design

---

## Slide 5 — Device Attribute Registry (DAR)

> *The knowledge base — IoT-GPT knows everything about every device*

### Example: Water Heater Entry in DAR

```json
{
  "device": "water_heater_01",
  "power_watts": 2000,
  "warmup_minutes": 30,
  "conflicts_with": ["room_heater"],
  "preferred_hours": [1, 2, 3, 4, 5],
  "avoid_peak_hours": true
}
```

### DAR Attribute Categories

| Category | What It Stores |
|----------|---------------|
| **Physical** | Power draw, voltage, warmup time, temperature range |
| **Behavioral** | Interruptible? Max daily cycles? Run duration? |
| **Relational** | Conflicts with which devices? Preferred sequence? |
| **Temporal** | Best hours to run, peak hours to avoid |
| **Calm-Tech** | Notification color, brightness level, trigger conditions |

---

## Slide 6 — Multi-Device Coordination Engine

### Smart Morning Schedule — Wake at 7:00 AM

**WITHOUT IoT-GPT** (all devices ON at 7 AM — 3,500W surge!)

| Time | Device | Load |
|------|--------|------|
| 7:00 AM | Water Heater | 2,000W |
| 7:00 AM | Room Heater | 1,500W |
| **Total** | **Simultaneous** | **3,500W ⚠️** |

**WITH IoT-GPT** (staggered, off-peak, 30% savings!)

| Time | Device | Action |
|------|--------|--------|
| 6:20 AM | Room Heater | ON — warms bedroom |
| 6:40 AM | Room Heater | OFF — room at target temp |
| 6:28 AM | Water Heater | ON — heats water |
| 6:58 AM | Water Heater | OFF — hot water ready |
| 6:55 AM | Smart Lights | ON at 10% — gentle wake signal |

**Key results:**
- ✅ No simultaneous high-power devices
- ✅ Peak hours (6–9 AM) shifted away where possible
- ✅ **15–25% energy cost reduction** (research target)

---

## Slide 7 — Calm Technology

> *"The most potentially interesting, challenging, and profound change implied by the ubiquitous computing era is a focus on calm."*
> — Weiser & Brown, Designing Calm Technology (1995)

### Ambient Light Signal System

| Event | Bulb Signal | Message |
|-------|------------|---------|
| ❄️ Snow forecast | 🔵 BLUE — soft glow | Wear snow boots! |
| 🌫️ Poor air quality | 🟣 PURPLE — pulse | Keep windows closed |
| 🔴 High CO₂ in room | 🔴 RED — bright | Open window now! |
| ⚡ Peak hour soon | 🟡 AMBER — slow pulse | Delay high-power devices |
| ✅ All clear | ⚫ OFF (dark) | No action needed |

> The light works at the **periphery of attention** — you notice it without being interrupted.

**Experiment 2** will measure: Push notification stress vs. ambient light — using the NASA Task Load Index (NASA-TLX) cognitive load scale.

---

## Slide 8 — Experimental Setup

### Hardware Components
- Raspberry Pi 5 (8GB) — IoT-GPT brain
- SONOFF ZigBee 3.0 USB Dongle
- 2× DHT22 temperature / humidity sensors
- Philips Hue or IKEA TRÅDFRI smart bulb (shoe rack)
- Smart power meters on all heaters
- CAT5e Ethernet to home router

### Software Stack (all open-source, all free)
- **Mosquitto** — MQTT message broker
- **Zigbee2MQTT** — ZigBee device bridge
- **InfluxDB 2.x** — time-series database
- **Grafana** — real-time dashboards
- **Python 3.11** — all IoT-GPT logic
- **Mistral-7B** (local LLM) — natural language reasoning
- **Google OR-Tools** — constraint-based scheduling

> **Estimated cost: ~$150 CAD hardware · $0 software**
> All code: github.com/gsleo1976/iot-gpt-research

---

## Slide 9 — 6 Research Experiments

| # | Experiment | What We Measure |
|---|-----------|----------------|
| **1** | **Energy Savings** | kWh consumed with/without IoT-GPT. Target: 15–25% reduction. |
| **2** | **Calm vs Push Alerts** | NASA-TLX cognitive load test. Ambient light vs. phone notification. |
| **3** | **IoT-GPT vs Manual Control** | User study: AI scheduling vs. manual. Error rate & comfort score. |
| **4** | **Load Optimization** | Constraint satisfaction: schedule 5+ devices under 15A circuit limit. |
| **5** | **Snow Alert Field Study** | Real-world shoe-rack bulb test over 30 days. Recall accuracy & user satisfaction. |
| **6** | **Scalability** | Scale from 3 to 15 devices. Measure response time & scheduling accuracy. |

---

## Slide 10 — Expected Results & Impact

### Key Targets

| Metric | Target |
|--------|--------|
| Energy savings per household | **15–25%** |
| Reduction in cognitive load (calm tech) | **~40%** lower NASA-TLX score |
| Scheduling accuracy (3–15 devices) | **90%+** correct schedules |
| Hardware cost to reproduce | **~$150 CAD** |

### Broader Impact
- **Open-source release** — any researcher can replicate the setup for ~$150 CAD
- Calm technology framework applicable to hospitals, schools, and offices
- Contributes to **UN SDG 7** (Affordable Clean Energy) and **SDG 11** (Sustainable Cities)
- Blueprint for edge-AI smart homes without cloud dependency or privacy risks

---

## Slide 11 — Why Students Should Join

> *Slides 11–15: How You Can Participate in This Research*

### Why Join This Research?

**📄 Real Publication Credit**
Co-author opportunity on the final research paper submitted to an academic journal or conference.

**🛠️ Hands-On Skills**
Work with Raspberry Pi, Python, MQTT, InfluxDB, ZigBee — skills in high demand in IoT and embedded systems careers.

**🎓 Course Credit**
Applicable as an independent study, directed research, or capstone project at most universities.

**🌱 Meaningful Work**
Your contribution directly reduces home energy waste and improves quality of daily life through calmer technology.

---

## Slide 12 — Available Student Roles

| Role | What You Do | Skills Needed | Hours/Week |
|------|------------|---------------|-----------|
| **Hardware Builder** | Set up Raspberry Pi, wire sensors, configure ZigBee | Basic electronics comfort | 15 hrs (month 1–2) |
| **Python Developer** | Write IoT-GPT scheduling, MQTT, and sensor logic | Python basics | 10 hrs (ongoing) |
| **Data Analyst** | Process InfluxDB data, build Grafana dashboards, run stats | CSV/Excel, some Python | 8 hrs (month 3–8) |
| **User Study Researcher** | Design surveys, run NASA-TLX tests with participants | Communication skills | 12 hrs (month 6–8) |
| **Technical Writer** | Document experiments, maintain GitHub wiki, write the paper | Clear writing, Markdown | 6 hrs (ongoing) |
| **AI/LLM Integrator** | Fine-tune Mistral-7B on IoT device data | Python + some ML knowledge | 10 hrs (month 4–9) |

---

## Slide 13 — Skills You Will Gain

### Hardware & Embedded
- Raspberry Pi GPIO and Linux command line
- ZigBee and MQTT communication protocols
- Sensor wiring — no soldering required!
- Edge computing concepts and architecture

### Software Development
- Python for IoT (`paho-mqtt`, `requests`, `csv`, `influxdb-client`)
- Git version control and GitHub collaboration
- REST API calls (weather, air quality, sunrise-sunset)
- Time-series database queries (InfluxDB / Flux language)

### Data & Research
- Grafana dashboard creation and visualization
- Experimental design with proper control groups
- Statistical analysis of A/B test results
- Writing academic reports and technical documentation

> **No experience needed to start** — we provide tutorials and a complete beginner's guide (included in this repo at `docs/IoT-GPT-Beginner-Guide.docx`)

---

## Slide 14 — How to Get Started

### Your Step-by-Step Path

**Step 1 — This week: Read the repo**
Visit [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research).
Read `README.md` and the `docs/` folder. Run the 10 sample Python programs in `samples/`.

**Step 2 — Week 2: Set up your Raspberry Pi**
Follow the Beginner's Guide (`docs/IoT-GPT-Beginner-Guide.docx`) step by step.
Takes about 1–2 days. Ask questions in the GitHub Discussions tab.

**Step 3 — Week 3: Pick a role and say hello**
Email [gurdev.leo@gmail.com](mailto:gurdev.leo@gmail.com) with your background and which role interests you.
No formal application needed — just introduce yourself.

**Step 4 — Month 1: Join the weekly session**
Virtual meeting every **Saturday 10 AM – 12 PM**.
New members are paired with an experienced researcher for onboarding.

---

## Slide 15 — Join the Research!

> **Help us build smarter, calmer, and more sustainable homes.**

### Contact & Links

| | |
|-|-|
| 📧 **Email** | gurdev.leo@gmail.com |
| 🐙 **GitHub** | [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research) |
| 📅 **Weekly Meeting** | Every Saturday 10 AM – 12 PM (virtual, link on GitHub) |

---

> **No experience needed · Open to all students · Remote participation welcome · Free hardware guidance**

---

*IoT-GPT Research Project · March 2026 · Open Source · MIT License*
