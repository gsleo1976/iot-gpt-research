# IoT-GPT Learning Path

**A practical, step-by-step guide to learning everything this research needs — from zero to ready.**

This path assumes you know how to use a computer but have little or no background in IoT, Python, or electronics. Each phase builds on the previous one. By the end of Phase 4, you will have all the knowledge needed to contribute to any part of the IoT-GPT research project.

---

## Topics Overview

| # | Topic | Why You Need It | Difficulty |
|---|-------|----------------|-----------|
| 1 | Linux command line | All our tools run on Linux (Raspberry Pi OS) | ⭐ Easy |
| 2 | Python programming | Every IoT-GPT script is written in Python | ⭐ Easy |
| 3 | Git & GitHub | Collaborate on code, track changes, contribute | ⭐ Easy |
| 4 | Networking basics | Understand IP, ports, how devices talk | ⭐⭐ Beginner |
| 5 | Raspberry Pi & GPIO | Our edge computing hardware | ⭐⭐ Beginner |
| 6 | IoT concepts | What IoT is, how devices connect | ⭐⭐ Beginner |
| 7 | Sensors & electronics | Wire a DHT22, read data from hardware | ⭐⭐ Beginner |
| 8 | MQTT protocol | How IoT devices send messages to each other | ⭐⭐ Beginner |
| 9 | REST APIs | Call weather, air quality, and sunrise APIs | ⭐⭐ Beginner |
| 10 | ZigBee protocol | How smart bulbs and sensors connect wirelessly | ⭐⭐⭐ Intermediate |
| 11 | InfluxDB | Store and query time-series sensor data | ⭐⭐⭐ Intermediate |
| 12 | Grafana | Visualize sensor data in dashboards | ⭐⭐⭐ Intermediate |
| 13 | Constraint optimization | Schedule devices without overloading the circuit | ⭐⭐⭐ Intermediate |
| 14 | Local LLMs (Mistral-7B) | Give IoT-GPT natural language reasoning | ⭐⭐⭐⭐ Advanced |
| 15 | Research methods & statistics | Design experiments and analyse results properly | ⭐⭐⭐ Intermediate |

---

## Phase 1 — Foundations
**Time: 1–2 weeks · No prior experience needed**

Start here. These are the tools every developer uses every day. Master these and everything else becomes much easier.

---

### 1. Linux Command Line

**Why:** The Raspberry Pi runs Linux. You will SSH into it, run scripts, install software, and check logs — all from the command line.

**What to learn:**
- Navigating folders (`cd`, `ls`, `pwd`)
- Creating and editing files (`nano`, `touch`, `cat`)
- Installing software (`apt install`)
- Running Python scripts (`python3 script.py`)
- Checking running services (`systemctl status`)
- Reading logs (`journalctl`, `tail -f`)

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| The Linux Command Line (free book) | Book/PDF | 5–10 hrs | [linuxcommand.org/tlcl.php](https://linuxcommand.org/tlcl.php) |
| Linux for Beginners — freeCodeCamp | Video | 5 hrs | [youtube.com/watch?v=sWbUDq4S6Y8](https://www.youtube.com/watch?v=sWbUDq4S6Y8) |
| Raspberry Pi Terminal basics | Article | 1 hr | [raspberrypi.com/documentation/computers/using_linux.html](https://www.raspberrypi.com/documentation/computers/using_linux.html) |
| Interactive terminal practice | Browser | 30 min | [overthewire.org/wargames/bandit](https://overthewire.org/wargames/bandit/) |

**Milestone:** You can SSH into a Raspberry Pi, navigate folders, install a package with `apt`, and run a Python script.

---

### 2. Python Programming

**Why:** 100% of IoT-GPT's logic is Python. You need to understand variables, loops, functions, and working with files and APIs.

**What to learn:**
- Variables, data types, lists, dictionaries
- `if/else`, `for` loops, `while` loops
- Functions (`def`)
- Reading and writing files (especially CSV and JSON)
- Importing libraries (`import requests`, `import json`)
- Error handling (`try/except`)

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Automate the Boring Stuff with Python (free) | Book | 10–15 hrs | [automatetheboringstuff.com](https://automatetheboringstuff.com) |
| Python for Everybody — Dr. Chuck (Coursera) | Video course | 20 hrs | [coursera.org/specializations/python](https://www.coursera.org/specializations/python) |
| Python Tutorial — Official Docs | Reference | As needed | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) |
| freeCodeCamp Python Full Course | Video | 4 hrs | [youtube.com/watch?v=rfscVS0vtbw](https://www.youtube.com/watch?v=rfscVS0vtbw) |
| Practice problems | Interactive | Ongoing | [exercism.org/tracks/python](https://exercism.org/tracks/python) |

**Milestone:** You can write a Python script that reads a CSV file, does calculations, and prints results. You can call a web API and parse the JSON response.

---

### 3. Git & GitHub

**Why:** All IoT-GPT code lives on GitHub. You need to clone the repo, make changes, commit them, and push — every single day.

**What to learn:**
- `git clone`, `git add`, `git commit`, `git push`, `git pull`
- Branches and pull requests
- Reading and writing a README in Markdown
- Opening and commenting on GitHub Issues

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Learn Git Branching — visual, interactive | Browser game | 2 hrs | [learngitbranching.js.org](https://learngitbranching.js.org) |
| Git & GitHub for Beginners — freeCodeCamp | Video | 1 hr | [youtube.com/watch?v=RGOj5yH7evk](https://www.youtube.com/watch?v=RGOj5yH7evk) |
| GitHub Skills (official interactive course) | Interactive | 3 hrs | [skills.github.com](https://skills.github.com) |
| Markdown Guide | Reference | 30 min | [markdownguide.org](https://www.markdownguide.org) |

**Milestone:** You can clone the IoT-GPT repo, run the sample programs, make a small change, and push it back to GitHub.

---

## Phase 2 — IoT Basics
**Time: 2–3 weeks · Requires Phase 1**

Now that you can code and use Linux, learn how physical hardware and IoT devices actually work.

---

### 4. Networking Basics

**Why:** IoT devices talk to each other over your home network using IP addresses and ports. Understanding this makes MQTT and ZigBee much easier.

**What to learn:**
- IP addresses, subnet masks, what a LAN is
- What a port is (port 1883 = MQTT, port 8086 = InfluxDB)
- How DNS works
- What a router does
- What a server is vs. a client

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Networking Fundamentals — Professor Messer | Video | 3 hrs | [youtube.com/watch?v=9SIjoeE93lo](https://www.youtube.com/watch?v=9SIjoeE93lo) |
| How the Internet Works — Khan Academy | Video | 1 hr | [khanacademy.org/computing/computers-and-internet](https://www.khanacademy.org/computing/computers-and-internet) |
| Computer Networking: a Top-Down Approach (intro chapters) | Book | 4 hrs | Free PDF available on library genesis |

**Milestone:** You can explain what happens when your Raspberry Pi sends a message to your laptop using an IP address and a port number.

---

### 5. Raspberry Pi & GPIO

**Why:** The Raspberry Pi 5 is the hardware brain of IoT-GPT. You need to know how to set it up, access it remotely, and connect sensors to its GPIO pins.

**What to learn:**
- Installing Raspberry Pi OS using the Imager tool
- SSH and remote access
- GPIO pins — what they are and which ones to use
- Reading sensor data using Python

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Official Raspberry Pi Getting Started Guide | Article | 2 hrs | [raspberrypi.com/documentation/computers/getting-started.html](https://www.raspberrypi.com/documentation/computers/getting-started.html) |
| Raspberry Pi GPIO explained — freeCodeCamp | Video | 1 hr | [youtube.com/watch?v=m0SKuFM8q_U](https://www.youtube.com/watch?v=m0SKuFM8q_U) |
| GPIO Zero Python library docs | Reference | As needed | [gpiozero.readthedocs.io](https://gpiozero.readthedocs.io) |
| Raspberry Pi full course — NetworkChuck | Video | 5 hrs | [youtube.com/watch?v=BpJCAafw2qE](https://www.youtube.com/watch?v=BpJCAafw2qE) |

**Milestone:** You have a Raspberry Pi running, can SSH into it from your laptop, and can run a Python script that blinks an LED.

---

### 6. IoT Concepts

**Why:** Understanding what IoT is — the architecture, terminology, and patterns — makes every other topic easier to learn.

**What to learn:**
- What edge computing means (vs. cloud computing)
- IoT device categories: sensors, actuators, controllers
- Common IoT architectures: local, cloud, hybrid
- Security basics: why local IoT is safer
- Real-world IoT examples (smart home, agriculture, healthcare)

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Introduction to IoT — Cisco NetAcad (free) | Course | 8 hrs | [netacad.com/courses/iot/introduction-iot](https://www.netacad.com/courses/iot) |
| IoT for Beginners — Microsoft (GitHub) | Course + Code | 12 hrs | [github.com/microsoft/IoT-For-Beginners](https://github.com/microsoft/IoT-For-Beginners) |
| A Smarter Planet blog — IBM IoT concepts | Articles | 2 hrs | [developer.ibm.com/learningpaths/iot-getting-started-iot-development](https://developer.ibm.com/learningpaths/iot-getting-started-iot-development/) |
| IoT Architecture — Coursera (free audit) | Video | 6 hrs | [coursera.org/learn/iot](https://www.coursera.org/learn/iot) |

**Milestone:** You can explain the difference between a sensor and an actuator, and describe how a smart thermostat uses edge computing to save energy.

---

### 7. Sensors & Basic Electronics

**Why:** IoT-GPT reads temperature, humidity, CO₂, and light from physical sensors. You need to know how to wire them up and read data from them.

**What to learn:**
- What a sensor is and how it outputs data
- Reading a datasheet (just the essentials)
- Wiring a DHT22 (temperature + humidity) to Raspberry Pi GPIO
- Using Python's `adafruit-circuitpython-dht` library
- What a breadboard is and how to use jumper wires

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| DHT22 sensor with Raspberry Pi — Adafruit | Guide | 1 hr | [learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging) |
| Electronics basics for beginners — SparkFun | Guide | 3 hrs | [learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law) |
| Raspberry Pi sensor projects — Tom's Hardware | Articles | 2 hrs | [tomshardware.com/how-to/raspberry-pi-gpio-pinout](https://www.tomshardware.com/how-to/raspberry-pi-gpio-pinout) |
| Electronics for Absolute Beginners — YouTube | Video | 3 hrs | [youtube.com/watch?v=r-X9coqTOdc](https://www.youtube.com/watch?v=r-X9coqTOdc) |

**Milestone:** You can wire a DHT22 sensor to your Raspberry Pi and run a Python script that prints temperature and humidity every 5 seconds.

---

### 8. MQTT Protocol

**Why:** MQTT is the messaging system all IoT devices use in IoT-GPT. Every sensor reading, every command to a heater, every alert goes through MQTT.

**What to learn:**
- What a broker, publisher, and subscriber are
- Topics and how to structure them (`home/bedroom/temperature`)
- Installing Mosquitto on Raspberry Pi
- Publishing and subscribing with Python (`paho-mqtt`)
- Quality of Service (QoS) levels 0, 1, 2

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| MQTT Essentials — HiveMQ (10-part series) | Articles | 3 hrs | [hivemq.com/mqtt-essentials](https://www.hivemq.com/mqtt-essentials/) |
| MQTT with Python paho — Tutorial | Article + Code | 2 hrs | [emqx.com/en/blog/how-to-use-mqtt-in-python](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python) |
| MQTT explained in 10 minutes | Video | 10 min | [youtube.com/watch?v=EIxdz-2rhLs](https://www.youtube.com/watch?v=EIxdz-2rhLs) |
| Mosquitto MQTT broker docs | Reference | As needed | [mosquitto.org/documentation](https://mosquitto.org/documentation/) |

**Milestone:** You have Mosquitto running on your Pi. You can publish a sensor reading from one Python script and receive it in another — just like IoT-GPT does.

---

### 9. REST APIs in Python

**Why:** IoT-GPT calls external APIs to get weather data, air quality, and sunrise/sunset times. This is how the shoe-rack light knows it might snow.

**What to learn:**
- What an API is and what JSON is
- Using Python `requests` library to call APIs
- Parsing JSON responses
- Handling errors and timeouts
- Free APIs: wttr.in (weather), open-meteo.com (air quality), sunrise-sunset.org

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| APIs for Beginners — freeCodeCamp | Video | 2 hrs | [youtube.com/watch?v=GZvSYJDk-us](https://www.youtube.com/watch?v=GZvSYJDk-us) |
| Python `requests` library docs | Reference | 1 hr | [docs.python-requests.org](https://docs.python-requests.org) |
| Free public APIs list | Reference | Browse | [github.com/public-apis/public-apis](https://github.com/public-apis/public-apis) |
| RealPython REST API tutorial | Article | 1 hr | [realpython.com/api-integration-in-python](https://realpython.com/api-integration-in-python/) |

**Milestone:** You can run `01_weather_forecast.py` and `05_air_quality_monitor.py` from our samples folder and understand every line of code.

---

## Phase 3 — IoT Systems
**Time: 3–4 weeks · Requires Phase 2**

Now connect individual pieces into a real working system — the way IoT-GPT is actually built.

---

### 10. ZigBee Protocol & Zigbee2MQTT

**Why:** Smart bulbs (Philips Hue, IKEA TRÅDFRI) and many sensors use ZigBee wireless. Zigbee2MQTT bridges them to MQTT so IoT-GPT can control them.

**What to learn:**
- What ZigBee is and how it differs from Wi-Fi/Bluetooth
- ZigBee coordinators, routers, and end devices
- Installing and configuring Zigbee2MQTT
- Pairing a smart bulb and controlling it from Python
- Reading ZigBee sensor data (temperature, motion)

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Zigbee2MQTT Getting Started | Official Guide | 2 hrs | [zigbee2mqtt.io/guide/getting-started](https://www.zigbee2mqtt.io/guide/getting-started/) |
| ZigBee explained simply | Video | 15 min | [youtube.com/watch?v=jzkgVvv-lS8](https://www.youtube.com/watch?v=jzkgVvv-lS8) |
| Control smart lights with Zigbee2MQTT + Python | Article | 2 hrs | [zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html](https://www.zigbee2mqtt.io/guide/usage/mqtt_topics_and_messages.html) |
| SONOFF ZigBee Dongle setup | Video | 30 min | [youtube.com/watch?v=hkKmN0RzqB0](https://www.youtube.com/watch?v=hkKmN0RzqB0) |

**Milestone:** You can pair a ZigBee smart bulb with your Raspberry Pi and change its colour from a Python script using MQTT.

---

### 11. InfluxDB — Time-Series Database

**Why:** IoT-GPT logs every sensor reading, every device action, and every energy measurement to InfluxDB. You query this data to find patterns and prove the research results.

**What to learn:**
- What a time-series database is (vs. regular SQL databases)
- Installing InfluxDB 2.x on Raspberry Pi
- Writing data from Python using `influxdb-client`
- Basic Flux query language (SELECT equivalent)
- Creating buckets and organizations

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| InfluxDB University (free courses) | Video course | 4 hrs | [university.influxdata.com](https://university.influxdata.com) |
| InfluxDB 2.x getting started | Official Docs | 2 hrs | [docs.influxdata.com/influxdb/v2/get-started](https://docs.influxdata.com/influxdb/v2/get-started/) |
| Writing IoT data to InfluxDB with Python | Tutorial | 1 hr | [docs.influxdata.com/influxdb/v2/api-guide/client-libraries/python](https://docs.influxdata.com/influxdb/v2/api-guide/client-libraries/python/) |
| Flux query language basics | Video | 1 hr | [youtube.com/watch?v=qsA0zOEbczA](https://www.youtube.com/watch?v=qsA0zOEbczA) |

**Milestone:** You can log DHT22 temperature readings from Python to InfluxDB every 60 seconds and query the last 24 hours of data.

---

### 12. Grafana — Data Visualization

**Why:** Grafana turns raw InfluxDB numbers into live charts and dashboards. This is how the research team monitors experiments and shows results.

**What to learn:**
- Installing Grafana on Raspberry Pi
- Connecting Grafana to InfluxDB as a data source
- Creating panels: time-series graphs, stat cards, gauges
- Building a dashboard that shows temperature, humidity, and energy usage
- Setting up alerts (e.g., email when temperature drops below 18°C)

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Grafana for Beginners — official tutorials | Video | 2 hrs | [grafana.com/tutorials](https://grafana.com/tutorials/) |
| Grafana + InfluxDB dashboard tutorial | Article | 1 hr | [grafana.com/docs/grafana/latest/datasources/influxdb](https://grafana.com/docs/grafana/latest/datasources/influxdb/) |
| Build a Raspberry Pi monitoring dashboard | YouTube | 45 min | [youtube.com/watch?v=HwkvHnl5Kk4](https://www.youtube.com/watch?v=HwkvHnl5Kk4) |

**Milestone:** You have a live Grafana dashboard showing real sensor data updating every minute, accessible from your laptop's browser.

---

### 13. Constraint Optimization — OR-Tools

**Why:** IoT-GPT uses Google OR-Tools to schedule devices under constraints (circuit load limits, preferred hours, conflicts). This is the "smart" in smart scheduling.

**What to learn:**
- What constraint satisfaction means
- Installing `ortools` Python library
- Defining variables, domains, and constraints
- Solving a simple scheduling problem
- Applying time windows and conflict constraints

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| OR-Tools Python getting started | Official Docs | 2 hrs | [developers.google.com/optimization/introduction/python](https://developers.google.com/optimization/introduction/python) |
| Constraint programming explained | Video | 30 min | [youtube.com/watch?v=lmy1ddn4cyw](https://www.youtube.com/watch?v=lmy1ddn4cyw) |
| OR-Tools scheduling tutorial | Guide | 3 hrs | [developers.google.com/optimization/scheduling](https://developers.google.com/optimization/scheduling/job_shop) |
| Python OR-Tools examples on GitHub | Code | Browse | [github.com/google/or-tools/tree/stable/examples/python](https://github.com/google/or-tools/tree/stable/examples/python) |

**Milestone:** You can write a Python script using OR-Tools that schedules 3 devices across a 24-hour period, respecting a 15-amp circuit limit and preferred time windows.

---

## Phase 4 — Advanced Topics
**Time: 4–8 weeks · Requires Phase 3**

These are the research-level topics. They make IoT-GPT intelligent rather than just automated.

---

### 14. Local LLMs — Mistral-7B with Ollama

**Why:** IoT-GPT uses a local language model (Mistral-7B) to reason about device states in plain English. "The bedroom is cold and the circuit has headroom — what should I do?" The LLM reasons through it.

**What to learn:**
- What a large language model (LLM) is — in plain terms
- Installing Ollama on Raspberry Pi or a laptop
- Running Mistral-7B locally (no internet, no API key)
- Calling Ollama from Python
- Prompt engineering for IoT decision-making
- Fine-tuning basics (optional, advanced)

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Ollama — run LLMs locally (easy install) | Tool + Docs | 1 hr | [ollama.com](https://ollama.com) |
| What are LLMs? — 3Blue1Brown (visual) | Video | 30 min | [youtube.com/watch?v=wjZofJX0v4M](https://www.youtube.com/watch?v=wjZofJX0v4M) |
| Ollama Python API tutorial | Article | 1 hr | [github.com/ollama/ollama/blob/main/docs/api.md](https://github.com/ollama/ollama/blob/main/docs/api.md) |
| Prompt Engineering Guide — free | Guide | 3 hrs | [promptingguide.ai](https://www.promptingguide.ai) |
| Hugging Face — understand AI models | Course (free) | 5 hrs | [huggingface.co/learn/nlp-course](https://huggingface.co/learn/nlp-course/chapter1/1) |
| Run AI on Raspberry Pi — tutorial | Article | 2 hrs | [medium.com/run-llm-raspberry-pi](https://medium.com/@rahul.biswas/run-llms-on-a-raspberry-pi-5-using-ollama-96d1f51e68fc) |

**Milestone:** You can run Mistral-7B locally on your machine, ask it "The bedroom temperature is 18°C and the circuit has 8A free. Should I turn on the room heater?" and get a sensible answer back through Python.

---

### 15. Research Methods & Statistics

**Why:** IoT-GPT research involves controlled experiments, user studies, and statistical proof. You need to know how to design a fair experiment, collect data, and prove your results are real and not random chance.

**What to learn:**
- What a controlled experiment is (treatment vs. control group)
- Mean, median, standard deviation — when to use which
- T-tests and p-values — how to tell if a result is significant
- The NASA Task Load Index (NASA-TLX) — measuring cognitive load
- How to write up results (tables, charts, discussion)
- Basic Python statistics with `scipy` and `pandas`

**Resources:**

| Resource | Format | Time | Link |
|----------|--------|------|------|
| Statistics and Probability — Khan Academy | Video course | 10 hrs | [khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability) |
| Research Methods for HCI — Coursera | Course | 8 hrs | [coursera.org/learn/hci-research-methods](https://www.coursera.org/learn/user-research) |
| NASA-TLX official tool & instructions | Tool | 30 min | [humansystems.arc.nasa.gov/groups/tlx](https://humansystems.arc.nasa.gov/groups/tlx/) |
| pandas for data analysis — official tutorial | Docs | 3 hrs | [pandas.pydata.org/docs/getting_started/intro_tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) |
| SciPy stats — t-test in Python | Docs | 1 hr | [docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html) |
| How to read a scientific paper | Article | 30 min | [science.org/doi/10.1126/science.caredit.a1600032](https://www.science.org/content/article/how-seriously-read-scientific-paper) |

**Milestone:** You can take a CSV of sensor readings from Experiment 1, run a t-test in Python, and write a one-paragraph summary explaining whether the energy savings are statistically significant.

---

## Recommended Weekly Schedule

> Adjust based on available time. 10 hrs/week gets you through all phases in ~5 months.

| Week | Focus | Sample Activity |
|------|-------|----------------|
| 1 | Linux basics | Set up Raspberry Pi, SSH in, navigate with terminal |
| 2 | Python basics | Complete 3 chapters of Automate the Boring Stuff |
| 3 | Git + GitHub | Clone IoT-GPT repo, run all 10 sample programs |
| 4 | Networking | Sketch your home network on paper, identify every device |
| 5 | Raspberry Pi + sensors | Wire DHT22, read temperature every 5 seconds |
| 6 | IoT concepts | Complete Microsoft IoT for Beginners (first 4 lessons) |
| 7 | MQTT | Get Mosquitto running, publish/subscribe with Python |
| 8 | REST APIs | Add real weather data to Program 01 using wttr.in |
| 9–10 | ZigBee | Pair a ZigBee bulb, change colour from Python |
| 11–12 | InfluxDB | Log DHT22 data to InfluxDB, query last 24 hours |
| 13–14 | Grafana | Build a live sensor dashboard |
| 15–16 | OR-Tools | Write a device scheduler using constraint programming |
| 17–20 | Local LLMs | Run Mistral-7B, ask IoT questions from Python |
| 21–24 | Statistics | Analyse Experiment 1 data, write up results |

---

## Learning Tips

**Start with the sample code.** The 10 programs in `samples/` are designed to teach each concept through working code. Read them before diving into tutorials.

**Break, fix, learn.** The best way to learn IoT is to deliberately break something and figure out why. Change a GPIO pin number, send a malformed MQTT message, give OR-Tools an impossible constraint. See what happens.

**Ask questions on GitHub.** Every topic here has a GitHub Discussions or Issues tab. The communities for Zigbee2MQTT, InfluxDB, Grafana, and Ollama are very welcoming to beginners.

**Don't learn everything before starting.** You do not need to finish all four phases before contributing. A Phase 2 person can absolutely contribute to hardware setup or Python sample code. Join when you're ready.

---

## Quick Reference: Free Learning Platforms

| Platform | Best For | Link |
|----------|---------|------|
| freeCodeCamp | Python, Linux, networking videos | [freecodecamp.org](https://www.freecodecamp.org) |
| Khan Academy | Math, statistics, computer science | [khanacademy.org](https://www.khanacademy.org) |
| Coursera (free audit) | Structured IoT and ML courses | [coursera.org](https://www.coursera.org) |
| edX (free audit) | University-level CS and IoT | [edx.org](https://www.edx.org) |
| Adafruit Learning System | Raspberry Pi, sensors, hardware | [learn.adafruit.com](https://learn.adafruit.com) |
| SparkFun Learn | Electronics basics | [learn.sparkfun.com](https://learn.sparkfun.com) |
| Real Python | Python tutorials, intermediate-advanced | [realpython.com](https://realpython.com) |
| Exercism | Python practice problems with mentors | [exercism.org/tracks/python](https://exercism.org/tracks/python) |
| Hugging Face | Machine learning, LLMs | [huggingface.co/learn](https://huggingface.co/learn) |
| GitHub Skills | Git, GitHub, Actions | [skills.github.com](https://skills.github.com) |

---

*IoT-GPT Research Project · All resources listed are free · No account required for most · Last updated March 2026*
