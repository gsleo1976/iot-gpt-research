# IoT-GPT — Intelligent Multi-Device Coordination for Sustainable Living & Calm Technology

**Research Project Proposal**
Gurdev Singh | March 2026 | Version 1.0
gurdev.leo@gmail.com

---

## Abstract

This research project proposes the design, development, and experimental evaluation of IoT-GPT — an intelligent coordination framework for Internet of Things (IoT) devices in residential and small-scale commercial environments. IoT-GPT acts like a knowledgeable expert that deeply understands every connected device in a home or building — its energy consumption patterns, behavioural characteristics, physical limitations, and inter-device relationships — and uses that knowledge to automatically coordinate devices for maximum energy efficiency and minimum user stress.

The central idea is that most IoT deployments today treat each device in isolation. A smart water heater does not know about a smart room heater. A smart bulb does not know about the weather forecast. IoT-GPT bridges these silos by building a Device Attribute Registry, a Multi-Device Coordination Engine, and a Calm Notification Layer that together make a home feel effortlessly intelligent.

This proposal details the objectives, system architecture, use cases, experimental design, expected outcomes, and team execution plan for a 12-month research project targeting 25–40% household energy savings and a measurable reduction in technology-related cognitive load.

**Keywords:** *Internet of Things, Smart Home, Energy Efficiency, Calm Technology, Multi-Device Coordination, Ambient Computing, Sustainable Technology, Artificial Intelligence, Load Scheduling*

---

## 1. Introduction

### 1.1 The Problem with Today's IoT

The promise of the Internet of Things was simple: connect everyday objects to the internet and make life easier. But what actually happened is a collection of isolated 'smart' devices, each with its own app, its own schedule, its own logic — and none of them talking to each other in a meaningful way.

- **Energy waste:** A water heater and a room heater both running at full power simultaneously during peak electricity hours, when coordinating them could slash the bill by 30–40%.
- **Cognitive overload:** Homeowners managing 6–10 separate apps, each sending its own notifications, alerts, and suggestions. Technology that was supposed to simplify life is adding stress.
- **Lost opportunity:** Devices sitting idle or running at full blast when a lighter, smarter approach — informed by weather forecasts, usage history, and other devices — would serve the user better.

### 1.2 The Vision: IoT-GPT

This project proposes IoT-GPT, an intelligent IoT coordination layer inspired by how large language models work as generalist experts. Just as a GPT model has learned the behaviour of language across millions of documents and can reason about new problems, IoT-GPT learns the behaviour of every connected device and reasons about how to best operate the home as a unified, intelligent system.

IoT-GPT does not replace existing device firmware. Instead, it sits as a coordination layer above all devices, observing their behaviour, building knowledge about them, and issuing smarter schedules, load-balancing instructions, and ambient signals.

### 1.3 Calm Technology

A key philosophical pillar of this project is Calm Technology, a concept first articulated by researchers Mark Weiser and John Seely Brown at Xerox PARC in the 1990s. The principle is: technology should inform without demanding. It should move to the periphery of our attention when we don't need it, and gently come to the centre only when we do.

A blue-glowing IoT bulb near your shoe rack, quietly signalling that snow is expected today, is a perfect example of calm technology. You notice it as you're putting on your shoes. No phone notification. No alarm. No app to open. The information reaches you at exactly the right moment, in exactly the right place, with minimum effort.

---

## 2. Research Objectives

### 2.1 Primary Objectives

- **Objective 1 — Build the IoT-GPT Expert Module:** Design and implement an AI-powered software module that can ingest device specifications, historical usage data, and environmental context (weather, time of day, season) to build a rich, structured knowledge base about each connected device in a home.
- **Objective 2 — Develop the Multi-Device Coordination Engine:** Build a scheduling and load-balancing engine that coordinates two or more devices to achieve combined goals — such as heating both room and water efficiently while staying under a target energy budget — by finding the optimal schedule across all devices simultaneously.
- **Objective 3 — Create the Calm Notification Layer:** Design a set of ambient, non-intrusive notification interfaces (coloured light signals, gentle vibration, subtle sound patterns) and the logic that decides when and how to surface information to users without disrupting their flow.
- **Objective 4 — Validate Energy Savings Through Experiments:** Demonstrate through controlled experiments that IoT-GPT's coordinated device management leads to measurable, statistically significant reductions in energy consumption (target: 25–40% reduction) compared to isolated device operation.
- **Objective 5 — Measure Impact on User Wellbeing:** Conduct user studies to measure whether calm, ambient IoT interactions reduce technology-related stress and cognitive load compared to conventional app-based notification systems.

### 2.2 Secondary Objectives

- Develop an open-source Device Attribute Registry format (JSON-LD schema) that any IoT manufacturer can adopt.
- Investigate the use of small, on-device language models for local, privacy-preserving IoT intelligence.
- Explore integration with public APIs (weather services, electricity grid load APIs) for real-world context.
- Produce a reusable research testbed that other teams can use for IoT sustainability experiments.

---

## 3. The IoT-GPT System Architecture

### 3.1 Overview

IoT-GPT is structured as four interacting layers, stacked from the user's intentions at the top to the physical devices at the bottom. Each layer has a clear role and communicates with the layers directly above and below it.

| Layer | Role |
|-------|------|
| **User Intention Layer** | Voice commands, app preferences, and scheduled routines set by the user. |
| **IoT-GPT Expert Reasoning Module** | The AI brain: device knowledge base + environmental context + optimization logic. |
| **Multi-Device Coordination Engine** | Translates reasoning into concrete schedules; handles load balancing and inter-device sync. |
| **Calm Notification Layer** | Decides what to communicate and how: ambient light signals, gentle sound cues. |
| **Physical Device Layer** | Smart bulbs, heaters, water heaters, sensors, and actuators in the home. |

### 3.2 Device Attribute Registry (DAR)

The Device Attribute Registry is the heart of IoT-GPT. It is a structured knowledge base, stored as JSON-LD, that describes every device in the home across five dimensions:

- **Physical Attributes:** Energy consumption (rated, standby, peak watts), thermal characteristics (heat-up time, cool-down curve, thermal mass), and operational constraints (min on-time, safe cycling interval).
- **Behavioural Attributes:** Historical usage patterns, learned user preferences (preferred water temperature, room temperature targets), and seasonal behaviour changes.
- **Relational Attributes:** Which devices compete for the same circuit, which benefit from coordinated operation, and which serve the same user goal.
- **Environmental Sensitivity:** Weather-dependent behaviour, time-of-use electricity pricing sensitivity, and grid load awareness.
- **Notification Preferences:** What information is worth surfacing, in what form, and under what conditions — with a strong preference for ambient signals over screen notifications.

### 3.3 Expert Reasoning Module (ERM)

The Expert Reasoning Module is an AI component — combining rule-based logic with a fine-tuned small language model (Mistral-7B, running locally on a Raspberry Pi 5) — that answers questions such as:

- What is the best schedule for the water heater and room heater today, given the weather forecast, electricity prices, and the user's morning routine?
- The outdoor temperature is dropping to -2°C tonight. What devices should be pre-configured now to ensure comfort by 7 AM?
- The user has a guest arriving at 3 PM. Which devices should be adjusted proactively?

The ERM has access to the full Device Attribute Registry, 30-day rolling usage history, external APIs (weather, electricity prices, optional calendar), and the user's override history.

### 3.4 Multi-Device Coordination Engine

The Coordination Engine solves a constrained optimisation problem: find the device schedule that minimises energy cost (or carbon footprint) subject to user comfort constraints.

> **Example — Winter Morning Comfort**
>
> - Room Heater (2 kW) needs 20 minutes to reach comfort temperature.
> - Water Heater (3 kW) needs 40 minutes to reach shower temperature.
> - Circuit limit: 4 kW simultaneous draw.
> - **Naive approach:** Both on at 6:30 AM → 5 kW draw, circuit stress, higher cost.
> - **IoT-GPT approach:** Water heater 5:50 AM (off-peak), room heater 6:10 AM (staggered). Both ready by 6:30 AM. Energy saved: 28%.

### 3.5 Calm Notification Layer

The Calm Notification Layer uses ambient devices — primarily smart bulbs — to communicate relevant information without interrupting the user's mental flow. No compulsory interaction is ever required; the user can always ignore a calm signal with no penalty.

| Signal | Location | Meaning |
|--------|----------|---------|
| **Blue glow** | Shoe rack bulb | Snow or ice forecast in next 6 hours |
| **Slow green pulse** | Living room | Home currently on renewable electricity |
| **Warm amber** | Kitchen | Energy use higher than yesterday at this time |
| **Gentle white fade** | Bedroom | Hot water ready — shower good to go |

---

## 4. Use Cases and Scenarios

**Use Case 1: The Winter Morning Routine**

It is January. The outdoor temperature dropped to -4°C overnight. Without IoT-GPT, the user wakes to a cold room and waits 35 minutes for hot water — total discomfort: 45 minutes, energy used: ~3.8 kWh. With IoT-GPT, the water heater starts at 5:50 AM (off-peak tariff) and the room heater at 6:10 AM (staggered). By 7:00 AM the room is 20°C and water is at 55°C. Energy used: 2.7 kWh — saving 29%.

**Use Case 2: The Snowfall Alert**

At 8 AM on a Tuesday, the weather API reports 75% probability of snowfall between 5–8 PM. IoT-GPT shifts the shoe rack bulb to a calm blue tone. When the user leaves at 8:30 AM, they glance at the bulb while putting on shoes, register "snow tonight," and pick up snow boots — without ever checking a weather app.

**Use Case 3: Peak Load Avoidance**

The electricity grid is under high load on a hot summer evening (5–8 PM demand response signal). IoT-GPT automatically shifts the water heater to 9 PM, pre-cools the home before the peak period, dims non-essential lights by 30%, and shows a warm amber glow in the living room.

**Use Case 4: Guest Arrival Preparation**

The user's calendar shows a guest arriving at 3 PM. At 2 PM, IoT-GPT begins a silent preparation sequence: guest room heater activates to reach 21°C by 3 PM, water heater schedules a second heat cycle for 4:30 PM, and entrance pathway lights shift to welcoming warm white. No notification is sent — the home prepares itself.

**Use Case 5: Device Anomaly Detection**

The water heater is taking 60% longer than usual to reach temperature over 3 consecutive days. The ERM flags this based on Device Attribute Registry knowledge (unusual heating time can indicate limescale). A single amber notification appears on the kitchen counter bulb: "Your water heater appears to be taking longer to heat than usual. Consider scheduling a descaling maintenance check."

---

## 5. Experimental Setup

### 5.1 Physical Testbed

The experiment will be conducted across two environments. Environment A is a controlled 40m² lab apartment fully instrumented with smart devices. Environment B consists of two volunteer households running IoT-GPT for 60 days, compared against a 60-day baseline period.

**Environment A — Controlled Lab Apartment**

- 1× Smart Water Heater (3 kW, MQTT-enabled, with energy monitoring)
- 1× Smart Electric Room Heater (2 kW, ZigBee-enabled)
- 1× Smart Air Conditioner (inverter type, 1.5 kW, Wi-Fi enabled)
- 4× Smart RGB Bulbs (ZigBee — shoe rack, kitchen, bedroom, living room)
- 8× Smart Plug Power Monitors (one per major device)
- 1× Raspberry Pi 5 running the IoT-GPT software stack
- 1× Weather API subscription (OpenWeatherMap)
- Temperature, humidity, and occupancy sensor arrays throughout

### 5.2 Software Stack

| Component | Technology |
|-----------|-----------|
| IoT-GPT Core | Python 3.11 on Raspberry Pi 5 |
| Device Communication | MQTT broker (Mosquitto), ZigBee coordinator (Sonoff USB) |
| Expert Reasoning Module | LangChain + Mistral-7B quantized (local, no cloud) |
| Coordination Engine | Google OR-Tools (constraint programming) |
| Calm Notification Controller | Custom Python + ZigBee bulb colour API |
| Data Logging | InfluxDB + Grafana |
| Device Registry | JSON-LD / SQLite |
| User Interface | React web dashboard + optional Telegram bot |

### 5.3 Instrumentation and Measurement

Every experiment logs the following metrics at 1-minute resolution: energy consumption per device (kWh), device on/off schedule (timestamps), room temperature and humidity, hot water temperature at tap, user comfort self-rating (3-question daily survey, 1–5 scale), system override count, and notification count with user response time.

---

## 6. Experiments to Be Carried Out

### Experiment 1: Energy Savings from Coordinated Scheduling

**What we are testing:** Does IoT-GPT's coordinated multi-device scheduling consume less energy than running each device on its own default schedule?

**How to run it:**
- Weeks 1–2 (Baseline): Run water heater and room heater on factory default schedules with no coordination.
- Weeks 3–4 (IoT-GPT): Enable coordination. Keep all other variables constant.
- Repeat across 3 seasons — 6 weeks per season, alternating baseline and IoT-GPT weeks.

**Metrics:** Total kWh per week, peak demand draw (kW), electricity cost, carbon emission equivalent (gCO2e).

**Expected finding:** 25–40% energy reduction in winter; 15–20% in mild conditions.

---

### Experiment 2: Calm Notification vs. Push Notification User Study

**What we are testing:** Do ambient calm signals (coloured light) result in lower cognitive load and better information retention than standard push notifications?

**How to run it:**
- Recruit 20 participants, split into two groups (10 each) for a crossover design.
- Group A: push notifications for 4 weeks, then calm signals for 4 weeks. Group B: calm signals first, then push notifications.
- After each period: NASA Task Load Index (NASA-TLX), information recall test, Perceived Stress Scale (PSS).

**Metrics:** NASA-TLX score, signal recall accuracy (%), PSS score, self-reported calm rating, number of times user checked the IoT app.

**Expected finding:** 15%+ reduction in NASA-TLX score; higher recall accuracy for calm signals in peripheral contexts.

---

### Experiment 3: IoT-GPT vs. Manual Device Management

**What we are testing:** How does IoT-GPT perform compared to a well-informed human managing devices manually?

**How to run it:**
- Recruit 15 participants to act as "expert home manager" for one week each in the controlled apartment.
- Provide full dashboards: weather forecast, electricity prices, energy consumption, comfort readings.
- Compare their daily device schedules to IoT-GPT's automated schedules.

**Metrics:** Energy used (kWh), comfort score, daily management time (minutes), user frustration rating (1–5).

**Expected finding:** IoT-GPT matches or outperforms humans on energy efficiency; reduces daily management time from ~15 min to near zero.

---

### Experiment 4: Multi-Device Load Optimisation Under Constraints

**What we are testing:** How well does the Coordination Engine handle hard constraints while preserving user comfort?

**Scenarios tested:** (A) No constraints — baseline; (B) Maximum simultaneous draw limited to 3.5 kW; (C) No heating devices 5–8 PM; (D) Guest arrives unexpectedly at 2 PM; (E) Water heater goes offline at 9 AM — system must replan.

**Metrics:** Constraint violation rate (%), temperature deviation from target (°C), hot water availability, replan time (seconds).

**Expected finding:** Zero violations in Scenarios A–C; successful replan within 30 seconds in D and E, <1°C deviation.

---

### Experiment 5: Ambient Snowfall Alert Real-World Accuracy Study

**What we are testing:** Does the calm snowfall alert (blue bulb) result in better footwear decisions, and does it feel natural or intrusive?

**How to run it:**
- Deploy in two pilot households for 60 days (October–December).
- Log all blue-bulb activations and whether actual snowfall/ice occurred within the predicted window.
- Weekly survey: "Did you notice the signal? Did it influence your footwear choice? How did it make you feel?"

**Metrics:** True positive rate, false positive rate, user action rate (changed footwear), user sentiment (1–5).

**Expected finding:** True positive rate >80%, false positive rate <15%, user sentiment >4.0/5.0 after habituation.

---

### Experiment 6: Scalability — 3 to 15 Devices

**What we are testing:** Does the Expert Reasoning Module maintain speed and quality as device count scales?

**How to run it:** Start with 3 devices and measure schedule generation time and quality. Add devices in batches of 5, 10, 15 (using synthetic profiles beyond the physical testbed).

**Metrics:** Schedule generation time (ms), optimisation quality score, system memory usage (MB), constraint violations.

**Expected finding:** Schedule generation under 2 seconds for 15 devices on Raspberry Pi 5.

---

## 7. Expected Results and Impact

**Energy Outcomes**

- 25–40% reduction in household energy consumption for heating devices through coordinated scheduling.
- 10–20% reduction in peak demand draw through load spreading.
- Estimated annual saving for a typical UK/EU household: £180–£320 per year at current energy prices.
- Potential carbon saving per household: 180–280 kg CO2e per year (equivalent to planting 10–15 trees annually).

**Calm Technology Outcomes**

- Reduction in daily IoT-related smartphone notifications: from 8–12 per day to 0–2.
- 15–25% reduction in NASA-TLX cognitive load score for smart home management tasks.
- Users reporting feeling "more in control" of their home without spending more time on it.

**System Performance**

- IoT-GPT device schedule generation: under 2 seconds for up to 15 devices.
- Device anomaly detection: alert within 3 days of onset of anomalous behaviour.
- Weather-based ambient alert accuracy: above 80% true positive rate.

**Broader Impact**

- A publishable open-source Device Attribute Registry schema and IoT-GPT coordination engine.
- A validated research methodology and replicable testbed for future IoT sustainability teams.
- Foundation for a product-level IoT hub: privacy-first, offline-capable, commercially viable.

---

## 8. Team Structure and Execution Plan

### 8.1 Team Roles

| Role | Responsibilities |
|------|----------------|
| **Principal Researcher / Lead** | Overall project direction, experiment design, final paper, architectural decisions. |
| **IoT Hardware Engineer** | Testbed setup, MQTT/ZigBee configuration, device drivers, Device Attribute Registry entries. |
| **AI / Optimisation Developer (×2)** | Expert Reasoning Module (LLM integration), Coordination Engine (OR-Tools), Experiments 1, 4, 6. |
| **UX Researcher** | User study design, participant recruitment, ethics approvals, qualitative analysis, Experiments 2, 3, 5. |
| **Data Engineer** | InfluxDB logging pipeline, statistical analysis, Grafana visualisations, final data figures. |
| **Project Manager / Docs Lead** | Timeline, wiki, meeting notes, GitHub repository, first-draft writing. |

### 8.2 Month-by-Month Execution Plan

**Month 1 — Foundation**
Set up the physical testbed and configure all devices. Install MQTT broker and ZigBee network. Build the Device Attribute Registry (first version) for all testbed devices. Set up data logging infrastructure (InfluxDB, Grafana). Complete literature review and submit ethics application for user studies.

**Month 2 — Core Development**
Implement the Expert Reasoning Module Phase 1 (rule-based logic). Implement the Coordination Engine with OR-Tools. Implement the Calm Notification Controller. First internal demo: coordinated water heater and room heater scheduling.

**Month 3 — Baseline Experiments**
Run Experiment 1 baseline phase (2 weeks, isolated device operation). Run Experiment 4 Scenarios A and B. Begin recruiting user study participants. Receive ethics approval.

**Month 4 — IoT-GPT Active Experiments**
Run Experiment 1 IoT-GPT phase (2 weeks, coordinated). Run Experiment 4 Scenarios C, D, E. Run Experiment 6 scalability tests. First analysis: compare baseline vs. IoT-GPT energy consumption.

**Month 5 — LLM Integration**
Integrate Mistral-7B into the Expert Reasoning Module. Implement natural language intent parsing. Test LLM vs. rule-based engine for quality. Deploy snowfall alert (Experiment 5 begins, requires ~60 days).

**Month 6 — User Studies Begin**
Launch Experiment 2 crossover study (20 participants). Begin Experiment 3 (15 participants × 1 week each). Instrument pilot households for Experiment 5.

**Months 7–8 — User Studies Complete**
Complete Experiment 2 crossover design. Complete Experiment 3 data collection. Continue Experiment 5 field study. Mid-project review: full team analysis, adjust methodology if needed.

**Months 9–10 — Analysis and Writing**
Full statistical analysis of all experiment data. Complete Experiment 5. Write Results sections. Produce Grafana dashboard visualisations. Identify any experiments needing replication.

**Months 11–12 — Paper and Open-Source Release**
Write Introduction, Related Work, Discussion, and Conclusion. Release IoT-GPT codebase and Device Attribute Registry on GitHub. Submit paper to ACM BuildSys or IEEE Internet of Things Journal. Create public project website and documentation.

---

## 9. Budget Overview

| Item | Qty | Unit Cost | Total |
|------|-----|-----------|-------|
| Raspberry Pi 5 (8GB) | 2 | £80 | £160 |
| Smart Electric Room Heater | 2 | £120 | £240 |
| Smart Water Heater Controller | 2 | £150 | £300 |
| Smart RGB Bulbs (ZigBee) | 8 | £20 | £160 |
| Smart Plug with Energy Monitor | 8 | £25 | £200 |
| Temperature/Humidity Sensors | 2 sets | £40 | £80 |
| Sonoff ZigBee USB Coordinator | 2 | £15 | £30 |
| Cables, adapters, miscellaneous | — | — | £100 |
| **Total** | | | **~£1,270** |

All software is open source with no license cost.

---

## 10. Conclusion

IoT-GPT represents a meaningful step forward in making smart homes genuinely intelligent — not just connected. By building a rich understanding of every device's characteristics and coordinating them as a unified system, IoT-GPT can deliver real, measurable energy savings while radically simplifying the user's relationship with their technology.

The Calm Technology philosophy at the heart of this project is just as important as the energy savings. A blue light near the shoe rack that tells you it will snow is not just convenient — it is a demonstration that technology can be humble. It can whisper rather than shout. It can serve without demanding.

This research project will produce open-source tools, validated experimental methods, and real-world data that can inform both academic research and commercial product development. The vision is a home that breathes with its occupants — responsive, efficient, and quietly intelligent.

---

## References

- Weiser, M. & Brown, J.S. (1995). *Designing Calm Technology*. Xerox PARC.
- Mankoff, J., et al. (2003). Heuristic Evaluation of Ambient Displays. *CHI 2003*.
- Beaudin, M. & Zareipour, H. (2015). Home Energy Management Systems: A Review. *Renewable and Sustainable Energy Reviews*.
- Shakshuki, E. & Younas, M. (2019). Multi-Agent Internet of Things: A Review. *Future Generation Computer Systems*.
- Zhu, J., et al. (2021). Optimal Scheduling of Household Appliances for Energy Efficiency. *IEEE Transactions on Smart Grid*.
- Chen, X., et al. (2024). LLM-Based IoT Orchestration: Towards Natural Language Smart Home Control. *IEEE Internet of Things Journal*.

---

*IoT-GPT Research Project | Gurdev Singh | 2026 | CC BY 4.0*
*Submitted to: [github.com/gsleo1976/iot-gpt-research](https://github.com/gsleo1976/iot-gpt-research)*
