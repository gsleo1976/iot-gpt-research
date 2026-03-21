# 🌿 IoT-GPT: Intelligent Multi-Device Coordination for Sustainable Living & Calm Technology

> *"Technology should inform without demanding. It should move to the periphery of our attention when we don't need it, and gently come to the centre only when we do."*
> — Mark Weiser & John Seely Brown, Xerox PARC

---

## 📋 Project Overview

**IoT-GPT** is a research project proposing an intelligent IoT coordination framework that acts like a knowledgeable expert for your home — understanding every connected device deeply, and coordinating them together for:

- ♻️ **Maximum energy efficiency** (target: 25–40% reduction in household energy use)
- 🧘 **Minimum stress** through Calm Technology principles (ambient signals, not notifications)
- 🔗 **True multi-device intelligence** — devices that know about each other and work as a team

The core insight is simple: today's "smart" devices are actually dumb loners. A water heater doesn't know about a room heater. A smart bulb doesn't know it's going to snow. IoT-GPT fixes this by creating a shared brain for all your devices.

---

## 💡 Key Concepts

### The IoT-GPT Expert Module
An AI reasoning layer (built on a local, privacy-first language model) that has deep knowledge of every device's:
- Energy consumption profile
- Physical characteristics (heat-up time, thermal mass, cycling limits)
- Relationships with other devices
- Sensitivity to weather, electricity prices, and user routines

### Multi-Device Coordination Engine
Solves the scheduling problem across all devices simultaneously. Example:

| Scenario | Without IoT-GPT | With IoT-GPT |
|----------|----------------|--------------|
| Morning room + water heating | Both heaters on at same time → 5 kW peak, high cost | Staggered schedule → 3.2 kW max, 29% cheaper |
| Snow forecast day | User checks phone app 🤦 | Shoe-rack bulb glows blue 💙 |
| Peak electricity hours | Devices run normally | System shifts loads to off-peak automatically |
| Guest arrives at 3 PM | User manually adjusts 5 devices | Home prepares itself silently |

### Calm Technology Layer
Ambient, non-intrusive signals that live at the *periphery* of your attention:

| Signal | Meaning |
|--------|---------|
| 💙 Blue shoe-rack bulb | Snow or ice expected in next 6 hours |
| 💚 Slow green pulse (living room) | Currently running on renewable electricity |
| 🟠 Warm amber (kitchen) | Energy use higher than yesterday |
| 🤍 Gentle white fade (bedroom) | Hot water ready — shower good to go |

---

## 🎯 Research Objectives

1. **Build the IoT-GPT Expert Module** — AI that understands device attributes and reasons about optimal operation
2. **Develop the Multi-Device Coordination Engine** — Constraint-based optimizer for multi-device scheduling
3. **Create the Calm Notification Layer** — Ambient light signals that replace intrusive push notifications
4. **Validate Energy Savings** — Controlled experiments targeting 25–40% energy reduction
5. **Measure Wellbeing Impact** — User studies measuring calm, cognitive load, and comfort

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│              User Intention Layer                        │
│   (voice / app / scheduled preferences)                 │
├─────────────────────────────────────────────────────────┤
│           IoT-GPT Expert Reasoning Module                │
│   (device knowledge + context + optimization logic)      │
├─────────────────────────────────────────────────────────┤
│         Multi-Device Coordination Engine                 │
│   (scheduling, load balancing, inter-device sync)        │
├─────────────────────────────────────────────────────────┤
│           Calm Notification Layer                        │
│   (ambient light signals, gentle alerts)                 │
├─────────────────────────────────────────────────────────┤
│              Physical Device Layer                       │
│   (smart bulbs, heaters, sensors, actuators)             │
└─────────────────────────────────────────────────────────┘
```

---

## 🧪 Experiments

### Experiment 1 — Energy Savings from Coordinated Scheduling
Comparing isolated device operation vs. IoT-GPT coordination over 6 weeks per season.

**Target**: 25–40% kWh reduction in winter, 15–20% in mild conditions.

### Experiment 2 — Calm Notifications vs. Push Notifications
A crossover user study (20 participants) comparing:
- Cognitive load (NASA-TLX scale)
- Information recall accuracy
- Perceived stress (PSS scale)

**Target**: 15%+ reduction in cognitive load score.

### Experiment 3 — IoT-GPT vs. Human Expert Management
15 participants manually manage device schedules for 1 week each vs. IoT-GPT automated management.

**Target**: IoT-GPT matches or beats human managers on energy efficiency; eliminates ~15 min/day management overhead.

### Experiment 4 — Multi-Device Load Optimization Under Constraints
5 constraint scenarios from unconstrained to device failure mid-day.

**Target**: Zero constraint violations; replan within 30 seconds on device failure.

### Experiment 5 — Snowfall Alert Field Study
60-day real household deployment (October–December). Measures alert accuracy and user sentiment.

**Target**: >80% true positive rate, <15% false positive rate, user sentiment >4.0/5.0.

### Experiment 6 — Scalability: 3 to 15 Devices
Testing Expert Reasoning Module performance as device count scales.

**Target**: Schedule generation <2 seconds for 15 devices on Raspberry Pi 5.

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Hardware | Raspberry Pi 5, ZigBee smart devices, MQTT energy monitors |
| IoT Protocol | MQTT (Mosquitto), ZigBee (Sonoff coordinator) |
| AI / Reasoning | Python + LangChain + Mistral-7B (local, offline) |
| Optimization | Google OR-Tools (constraint programming) |
| Data Logging | InfluxDB + Grafana |
| Device Registry | JSON-LD / SQLite |
| User Interface | React web dashboard + optional Telegram bot |
| Weather Data | OpenWeatherMap API |

---

## 📅 12-Month Timeline

```
Month 1   │ Hardware setup, Device Attribute Registry, data logging
Month 2   │ IoT-GPT core: Coordination Engine + Calm Notification Controller
Month 3   │ Baseline experiments (isolated device operation)
Month 4   │ IoT-GPT active experiments, scalability tests
Month 5   │ LLM integration (Mistral-7B), snowfall alert deployment begins
Month 6   │ User studies begin (calm notifications, manual vs. automated)
Month 7-8 │ User studies complete, pilot household data collection
Month 9-10│ Full data analysis, results writing, visualizations
Month 11-12│ Final paper, open-source release, GitHub documentation
```

---

## 📁 Repository Structure

```
iot-gpt-research/
├── README.md                    ← This file
├── docs/
│   ├── research-proposal.docx  ← Full research proposal (Word document)
│   ├── architecture.md         ← Detailed system architecture
│   └── experiment-protocols/   ← Step-by-step experiment guides
├── src/
│   ├── expert-module/          ← Expert Reasoning Module (Python)
│   ├── coordination-engine/    ← Multi-device scheduler (OR-Tools)
│   ├── calm-notifications/     ← ZigBee bulb color controller
│   └── device-registry/        ← JSON-LD device schemas
├── experiments/
│   ├── experiment-1-energy/    ← Energy savings experiment data + analysis
│   ├── experiment-2-calm/      ← User study: calm vs. push notifications
│   ├── experiment-3-manual/    ← Human vs. IoT-GPT management
│   ├── experiment-4-constraints/← Load optimization under constraints
│   ├── experiment-5-snowfall/  ← Snowfall alert field study
│   └── experiment-6-scale/     ← Scalability experiments
├── data/
│   ├── baseline/               ← Baseline energy consumption logs
│   └── iot-gpt/                ← IoT-GPT coordinated operation logs
└── dashboards/
    └── grafana/                ← Grafana dashboard JSON exports
```

---

## 👥 Team

| Role | Responsibilities |
|------|-----------------|
| Principal Researcher / Lead | Project direction, experiment design, final paper |
| IoT Hardware Engineer | Testbed setup, MQTT/ZigBee configuration, device drivers |
| AI / Optimization Developer | Expert Reasoning Module, Coordination Engine |
| UX Researcher | User study design, recruitment, analysis |
| Data Engineer | InfluxDB pipeline, statistical analysis, visualizations |
| Project Manager | Timeline, documentation, GitHub maintenance |

---

## 📊 Expected Outcomes

- **25–40% energy savings** for heating devices through coordinated scheduling
- **£180–£320/year** estimated savings for a typical UK/EU household
- **180–280 kg CO2e/year** per household (equivalent to 10–15 trees annually)
- **15–25% reduction** in cognitive load for smart home management
- **Open-source** Device Attribute Registry schema + IoT-GPT codebase
- **Research paper** submitted to ACM BuildSys or IEEE Internet of Things Journal

---

## 📄 License

This research project and all materials in this repository are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You are free to share and adapt these materials for any purpose, provided appropriate credit is given.

---

## 🗂️ Repository Navigator

Looking for a specific file? See **[navigator.md](navigator.md)** for a complete index of all documents, slides, guides, and sample programs in this repo.

---

## 📬 Contact

**Gurdev Singh** | IoT Research for Sustainability and Calm Technology
📧 gurdev.leo@gmail.com

---

*"A home that breathes with its occupants — responsive, efficient, and quietly intelligent."*
