"""
IoT-GPT Sample Program 04: MQTT IoT Simulator
==============================================
Simulate IoT devices sending sensor data using MQTT protocol.
MQTT is the language that IoT devices use to talk to each other!

In the real IoT-GPT setup:
- Devices publish data to an MQTT broker (like Mosquitto)
- IoT-GPT subscribes and decides what to do

This program simulates the SAME thing WITHOUT needing a real broker.

How to run:
    pip install paho-mqtt
    python 04_mqtt_iot_simulator.py

What you'll see:
- Temperature sensor publishing data every 2 seconds
- IoT-GPT "brain" receiving and analyzing the data
- Smart decisions being made automatically
"""

import time
import random
import json
from datetime import datetime

# Try to import paho-mqtt; fall back to simulation if not installed
try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False


# ---- Simulated MQTT without broker (for beginners) ----
class SimulatedBroker:
    """A fake MQTT broker that runs locally for learning purposes."""
    def __init__(self):
        self.subscribers = {}
        self.message_log = []

    def publish(self, topic, payload):
        message = {"topic": topic, "payload": payload, "time": datetime.now().strftime("%H:%M:%S")}
        self.message_log.append(message)
        # Deliver to subscribers
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                callback(topic, payload)

    def subscribe(self, topic, callback):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)

# Global simulated broker
broker = SimulatedBroker()

# ---- IoT Device Simulators ----
class TemperatureSensor:
    """Simulates a room temperature sensor."""
    def __init__(self, room_name, base_temp=21.0):
        self.room = room_name
        self.temp = base_temp
        self.topic = f"home/{room_name}/temperature"

    def read_and_publish(self):
        # Simulate realistic temperature changes
        self.temp += random.uniform(-0.3, 0.3)
        self.temp = round(max(15.0, min(35.0, self.temp)), 1)

        data = {
            "room": self.room,
            "temperature": self.temp,
            "unit": "celsius",
            "timestamp": datetime.now().isoformat()
        }
        broker.publish(self.topic, json.dumps(data))
        return self.temp

class SmartHeater:
    """Simulates a smart heater that can be controlled via MQTT."""
    def __init__(self, room_name):
        self.room = room_name
        self.is_on = False
        self.target_temp = 22.0
        self.command_topic = f"home/{room_name}/heater/command"
        self.status_topic = f"home/{room_name}/heater/status"
        # Subscribe to commands
        broker.subscribe(self.command_topic, self.on_command)

    def on_command(self, topic, payload):
        """React when IoT-GPT sends a command."""
        command = json.loads(payload)
        self.is_on = command.get("state") == "ON"
        status_msg = "HEATING" if self.is_on else "OFF"
        print(f"    [Heater-{self.room}] Command received: {command['state']}")
        broker.publish(self.status_topic, json.dumps({"state": status_msg}))

# ---- IoT-GPT Brain ----
class IoTGPTBrain:
    """
    The 'brain' of IoT-GPT.
    Subscribes to sensor data and makes smart decisions.
    """
    def __init__(self):
        self.COMFORT_TEMP = 22.0    # target temperature
        self.TOO_COLD = 20.0        # turn heater ON below this
        self.TOO_HOT = 24.0         # turn heater OFF above this
        self.rooms = {}

        # Subscribe to all room temperature topics
        broker.subscribe("home/+/temperature", self.on_temperature)

    def on_temperature(self, topic, payload):
        data = json.loads(payload)
        room = data["room"]
        temp = data["temperature"]
        self.rooms[room] = temp

        print(f"  [IoT-GPT] {room} temperature: {temp}°C", end="")

        # Decision logic
        if temp < self.TOO_COLD:
            print(f" -> Too cold! Turning heater ON")
            command = json.dumps({"state": "ON", "target": self.COMFORT_TEMP})
            broker.publish(f"home/{room}/heater/command", command)
        elif temp > self.TOO_HOT:
            print(f" -> Too warm! Turning heater OFF")
            command = json.dumps({"state": "OFF"})
            broker.publish(f"home/{room}/heater/command", command)
        else:
            print(f" -> Comfortable. No action needed.")

def run_simulation(cycles=8):
    """Run the IoT simulation for a number of cycles."""
    print("\n" + "="*60)
    print("  IoT-GPT MQTT Simulator")
    print("  Simulating smart home sensor network...")
    print("="*60 + "\n")

    # Create devices
    bedroom_sensor = TemperatureSensor("bedroom", base_temp=19.5)   # starts cold
    living_sensor  = TemperatureSensor("living_room", base_temp=23.0)

    bedroom_heater = SmartHeater("bedroom")
    living_heater  = SmartHeater("living_room")

    brain = IoTGPTBrain()

    print("Devices online:")
    print("  - Bedroom temperature sensor")
    print("  - Living room temperature sensor")
    print("  - Smart heater (bedroom)")
    print("  - Smart heater (living room)")
    print("  - IoT-GPT Brain (analyzing data)\n")
    print(f"{'='*60}\n")

    for cycle in range(cycles):
        print(f"[Cycle {cycle+1}/{cycles}] - {datetime.now().strftime('%H:%M:%S')}")
        bedroom_sensor.read_and_publish()
        living_sensor.read_and_publish()
        print()
        time.sleep(1.5)

    print(f"\n{'='*60}")
    print(f"  Simulation complete! {len(broker.message_log)} MQTT messages sent.")
    print(f"{'='*60}\n")

    print("Message Log (last 5):")
    for msg in broker.message_log[-5:]:
        payload_preview = msg['payload'][:60] + "..." if len(msg['payload']) > 60 else msg['payload']
        print(f"  [{msg['time']}] {msg['topic']}")
        print(f"    {payload_preview}")

    if not MQTT_AVAILABLE:
        print("\n[Tip] Install paho-mqtt to connect to a REAL MQTT broker:")
        print("      pip install paho-mqtt")
        print("      Then connect to a local Mosquitto broker on Raspberry Pi!")

if __name__ == "__main__":
    run_simulation()
