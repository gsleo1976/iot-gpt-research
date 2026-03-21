"""
IoT-GPT Sample Program 09: Device Attribute Registry (DAR)
===========================================================
This is the KNOWLEDGE BASE of IoT-GPT.
Every smart device has attributes that describe what it does,
how much power it uses, and how it relates to other devices.

The Device Attribute Registry (DAR) stores this knowledge
so IoT-GPT can always make smart decisions.

Think of it like a smart catalog that knows:
  - "Water heater takes 30 mins and uses 2000W"
  - "Room heater conflicts with water heater (both high power)"
  - "Bedroom light should NOT be bright after 10pm"

How to run:
    python 09_device_attribute_registry.py

No extra libraries needed!
"""

import json
from datetime import datetime

# The Device Attribute Registry - stored as a Python dictionary
# (In real IoT-GPT this would be a JSON-LD file in a database)
DEVICE_REGISTRY = {
    "water_heater_01": {
        "name": "Water Heater",
        "type": "heater",
        "location": "utility_room",
        "manufacturer": "Generic",
        "power_watts": 2000,
        "voltage": 240,
        "warmup_time_minutes": 30,
        "hold_temp_celsius": 60,
        "protocol": "ZigBee",
        "controllable": True,
        "interruptible": False,  # once ON, best to complete full cycle
        "constraints": {
            "max_daily_cycles": 3,
            "avoid_simultaneous_with": ["room_heater_01"],  # circuit load concern
            "preferred_hours": list(range(1, 6)),           # 1am-6am (cheapest)
            "avoid_hours": list(range(6, 9)) + list(range(17, 20))  # peak hours
        },
        "attributes": {
            "heats_water": True,
            "thermal_storage": True,
            "heat_retention_hours": 4
        }
    },
    "room_heater_01": {
        "name": "Room Heater (Bedroom)",
        "type": "heater",
        "location": "bedroom",
        "manufacturer": "Dimplex",
        "power_watts": 1500,
        "voltage": 240,
        "warmup_time_minutes": 20,
        "target_temp_celsius": 22,
        "protocol": "ZigBee",
        "controllable": True,
        "interruptible": True,  # can be stopped/started freely
        "constraints": {
            "avoid_simultaneous_with": ["water_heater_01"],
            "preferred_hours": [5, 6, 7],   # just before wake-up
            "min_temp_trigger": 19.0,        # turn ON if temp drops below this
            "max_temp_trigger": 23.0         # turn OFF if temp exceeds this
        },
        "attributes": {
            "heats_room": True,
            "room_volume_m3": 45,
            "insulation_quality": "medium"
        }
    },
    "shoe_rack_light_01": {
        "name": "Shoe Rack Smart Bulb",
        "type": "smart_light",
        "location": "entryway",
        "manufacturer": "Philips Hue",
        "power_watts": 9,
        "protocol": "ZigBee",
        "controllable": True,
        "rgb_capable": True,
        "calm_tech_role": "ambient_notifier",  # special role in IoT-GPT!
        "notification_colors": {
            "snow_forecast": {"r": 0, "g": 150, "b": 255, "brightness": 40},
            "rain_forecast": {"r": 100, "g": 180, "b": 255, "brightness": 30},
            "all_clear": {"r": 0, "g": 0, "b": 0, "brightness": 0},    # OFF
            "high_co2": {"r": 255, "g": 50, "b": 0, "brightness": 80}
        },
        "constraints": {
            "avoid_hours": list(range(0, 6)),  # don't glow between midnight-6am
        },
        "attributes": {
            "visible_from_bedroom": True,
            "peripheral_visibility": True  # designed for calm tech - peripheral view
        }
    },
    "raspberry_pi_01": {
        "name": "Raspberry Pi 5 (IoT-GPT Hub)",
        "type": "edge_computer",
        "location": "study",
        "model": "Raspberry Pi 5 - 8GB",
        "power_watts": 12,
        "protocol": "WiFi/Ethernet + ZigBee (USB dongle)",
        "services": ["MQTT broker", "IoT-GPT AI", "InfluxDB", "Grafana", "Node-RED"],
        "controllable": False,
        "attributes": {
            "is_hub": True,
            "connected_devices": ["water_heater_01", "room_heater_01", "shoe_rack_light_01"],
            "local_llm": "Mistral-7B-Instruct",
            "always_on": True
        }
    }
}

def display_device(device_id, device):
    """Display a single device's attributes in a readable format."""
    print(f"\n  {'─'*50}")
    print(f"  Device ID   : {device_id}")
    print(f"  Name        : {device['name']}")
    print(f"  Type        : {device['type']}")
    print(f"  Location    : {device.get('location', 'N/A')}")
    print(f"  Protocol    : {device.get('protocol', 'N/A')}")
    print(f"  Power       : {device.get('power_watts', 0)}W")
    print(f"  Controllable: {'Yes' if device.get('controllable') else 'No'}")

    if "constraints" in device:
        c = device["constraints"]
        if "avoid_simultaneous_with" in c:
            print(f"  Conflicts   : {', '.join(c['avoid_simultaneous_with'])}")
        if "preferred_hours" in c:
            hours = c["preferred_hours"]
            print(f"  Best hours  : {hours[0]:02d}:00 - {hours[-1]+1:02d}:00")

    if "calm_tech_role" in device:
        print(f"  Calm Tech   : {device['calm_tech_role']}")
        print(f"  Colors      : {list(device['notification_colors'].keys())}")

    if "attributes" in device:
        print(f"  Attributes  : {json.dumps(device['attributes'], indent=0)[:80]}...")

def find_conflicts():
    """Find all devices that conflict with each other."""
    print("\n  Conflict Analysis:")
    print("  " + "─"*40)
    conflicts_found = False
    for dev_id, device in DEVICE_REGISTRY.items():
        conflicts = device.get("constraints", {}).get("avoid_simultaneous_with", [])
        for conflict_id in conflicts:
            if conflict_id in DEVICE_REGISTRY:
                other = DEVICE_REGISTRY[conflict_id]
                combined_watts = device["power_watts"] + other["power_watts"]
                print(f"  ⚠  {device['name']} + {other['name']}")
                print(f"     Combined load: {combined_watts}W (may trip 15A circuit!)")
                conflicts_found = True

    if not conflicts_found:
        print("  No conflicts found.")

def iot_gpt_reason(query):
    """
    Simulate how IoT-GPT uses the DAR to answer questions.
    This is a simplified version of the LLM reasoning module.
    """
    query_lower = query.lower()

    if "heat" in query_lower and ("water" in query_lower or "bath" in query_lower):
        wh = DEVICE_REGISTRY["water_heater_01"]
        rh = DEVICE_REGISTRY["room_heater_01"]
        combined = wh["power_watts"] + rh["power_watts"]
        conflict = rh["id"] if "id" in rh else "room_heater_01" in wh["constraints"].get("avoid_simultaneous_with", [])
        return (f"Water Heater ({wh['power_watts']}W) and Room Heater ({rh['power_watts']}W) "
                f"should NOT run together ({wh['power_watts']+rh['power_watts']}W combined). "
                f"I'll schedule Water Heater at {wh['constraints']['preferred_hours'][0]}:00 "
                f"and Room Heater at {rh['constraints']['preferred_hours'][0]}:00.")

    elif "snow" in query_lower or "boot" in query_lower:
        light = DEVICE_REGISTRY["shoe_rack_light_01"]
        color = light["notification_colors"]["snow_forecast"]
        return (f"Snow is forecast! I'll set the Shoe Rack Light to "
                f"BLUE (RGB: {color['r']},{color['g']},{color['b']}) "
                f"at {color['brightness']}% brightness. "
                f"This is a calm ambient signal — no buzzing needed.")

    elif "energy" in query_lower or "save" in query_lower or "cost" in query_lower:
        total_controllable_w = sum(
            d["power_watts"] for d in DEVICE_REGISTRY.values()
            if d.get("controllable") and d["power_watts"] > 100
        )
        return (f"I'll shift {total_controllable_w}W of controllable devices to off-peak hours "
                f"(1am-6am). This can save up to 30% on electricity costs.")

    elif "hub" in query_lower or "raspberry" in query_lower:
        pi = DEVICE_REGISTRY["raspberry_pi_01"]
        return (f"{pi['name']} is the IoT-GPT hub. It runs: "
                f"{', '.join(pi['services'])}. "
                f"Connected devices: {len(pi['attributes']['connected_devices'])}.")

    else:
        return "I don't have enough information to answer that. Try asking about heating, energy, snow alerts, or the hub."

def main():
    print("\n" + "="*60)
    print("  IoT-GPT Device Attribute Registry (DAR)")
    print("="*60 + "\n")

    print("  What would you like to do?")
    print("  1. Browse all devices")
    print("  2. Check device conflicts")
    print("  3. Ask IoT-GPT a question (Q&A demo)")
    print("  4. Export registry to JSON")

    choice = input("\n  Enter choice (1/2/3/4): ").strip() or "1"

    if choice == "1":
        print(f"\n  Registry has {len(DEVICE_REGISTRY)} device(s):\n")
        for device_id, device in DEVICE_REGISTRY.items():
            display_device(device_id, device)

    elif choice == "2":
        print("\n" + "="*50)
        print("  Device Conflict Analysis")
        print("="*50)
        find_conflicts()
        print("\n  [IoT-GPT] These conflicts are automatically managed")
        print("  by the scheduling engine. Devices will never run together.")

    elif choice == "3":
        print("\n  Ask IoT-GPT anything about your home devices.")
        print("  Examples: 'How should I heat the water?', 'Will it snow?',")
        print("            'How can I save energy?', 'Tell me about the hub'")
        question = input("\n  Your question: ").strip()
        if not question:
            question = "How should I heat water and the room together?"
        answer = iot_gpt_reason(question)
        print(f"\n  [IoT-GPT]: {answer}\n")

    elif choice == "4":
        filename = "device_registry.json"
        with open(filename, 'w') as f:
            json.dump(DEVICE_REGISTRY, f, indent=2)
        print(f"\n  Registry exported to: {filename}")
        print("  You can load this into a database or edit it directly.")

if __name__ == "__main__":
    main()
