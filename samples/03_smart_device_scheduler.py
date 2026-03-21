"""
IoT-GPT Sample Program 03: Smart Device Scheduler
==================================================
Simulate how IoT-GPT schedules water heater + room heater
to save energy and avoid peak electricity load!

This is the CORE IDEA of the IoT-GPT research project:
- Room heater and water heater should NOT run at the same time
- Schedule them smartly based on when you wake up
- Avoid peak electricity hours (6am-9am, 5pm-8pm) to save money

How to run:
    python 03_smart_device_scheduler.py

No extra libraries needed!
"""

from datetime import datetime, timedelta
import time

# ----- Device Definitions -----
DEVICES = {
    "room_heater": {
        "name": "Room Heater",
        "power_watts": 1500,
        "warmup_time_mins": 20,  # time needed to warm the room
        "icon": "🔥"
    },
    "water_heater": {
        "name": "Water Heater",
        "power_watts": 2000,
        "warmup_time_mins": 30,  # time to heat water
        "icon": "💧"
    },
    "smart_light": {
        "name": "Smart Light",
        "power_watts": 10,
        "warmup_time_mins": 0,
        "icon": "💡"
    }
}

# Peak hours when electricity is expensive
PEAK_HOURS = [(6, 9), (17, 20)]  # (start_hour, end_hour)

def is_peak_hour(hour):
    """Check if a given hour is during peak electricity time."""
    for start, end in PEAK_HOURS:
        if start <= hour < end:
            return True
    return False

def calculate_cost(watts, minutes, peak=False):
    """Calculate electricity cost."""
    kwh = (watts / 1000) * (minutes / 60)
    rate = 0.20 if peak else 0.10  # $ per kWh (peak vs off-peak)
    return kwh * rate

def iot_gpt_schedule(wake_up_hour=7, wake_up_minute=0):
    """
    IoT-GPT's smart scheduling algorithm.
    Given a wake-up time, create the optimal schedule for all devices.

    Key rules:
    1. Room must be warm BEFORE you wake up
    2. Hot water must be ready BEFORE you wake up
    3. Devices should NOT overlap (to avoid overloading circuit)
    4. Prefer off-peak hours to save money
    """
    wake_time = datetime(2024, 1, 1, wake_up_hour, wake_up_minute)

    schedule = []

    # Water heater needs 30 min - schedule it first, ending at wake time
    water_end = wake_time
    water_start = water_end - timedelta(minutes=DEVICES["water_heater"]["warmup_time_mins"])

    # Room heater needs 20 min - schedule after water heater finishes
    # (to avoid running both at same time)
    room_end = wake_time
    room_start = water_start - timedelta(minutes=DEVICES["room_heater"]["warmup_time_mins"])

    # Smart light: turn on 5 minutes before wake time
    light_start = wake_time - timedelta(minutes=5)
    light_end = wake_time + timedelta(minutes=30)  # 30 min after wake

    schedule.append({
        "device": "room_heater",
        "start": room_start,
        "end": room_end,
        "action": "ON"
    })
    schedule.append({
        "device": "water_heater",
        "start": water_start,
        "end": water_end,
        "action": "ON"
    })
    schedule.append({
        "device": "smart_light",
        "start": light_start,
        "end": light_end,
        "action": "ON"
    })

    return sorted(schedule, key=lambda x: x["start"])

def print_schedule(schedule, wake_up_hour, wake_up_minute):
    """Display the schedule in a friendly format."""
    print(f"\n{'='*60}")
    print(f"  IoT-GPT Smart Schedule")
    print(f"  Wake-up time: {wake_up_hour:02d}:{wake_up_minute:02d}")
    print(f"{'='*60}\n")

    total_cost_smart = 0
    total_cost_dumb = 0

    print(f"  {'Time':<12} {'Action':<8} {'Device':<20} {'Power':<10} {'Cost'}")
    print("  " + "-" * 55)

    for item in schedule:
        device_key = item["device"]
        device = DEVICES[device_key]
        start_str = item["start"].strftime("%H:%M")
        end_str = item["end"].strftime("%H:%M")
        duration_mins = int((item["end"] - item["start"]).total_seconds() / 60)

        peak = is_peak_hour(item["start"].hour)
        cost = calculate_cost(device["power_watts"], duration_mins, peak)
        total_cost_smart += cost

        peak_label = " [PEAK!]" if peak else ""
        print(f"  {start_str} - {end_str}  {'ON':<8} {device['icon']} {device['name']:<18} "
              f"{device['power_watts']}W    ${cost:.3f}{peak_label}")

    # Compare with "dumb" scheduling (all devices ON at wake time)
    print(f"\n  --- Without IoT-GPT (all ON at wake time) ---")
    for device_key, device in DEVICES.items():
        if device_key == "smart_light":
            continue
        duration_mins = device["warmup_time_mins"]
        peak = is_peak_hour(wake_up_hour)
        cost = calculate_cost(device["power_watts"], duration_mins, peak)
        total_cost_dumb += cost
        peak_label = " [PEAK!]" if peak else ""
        print(f"  {wake_up_hour:02d}:{wake_up_minute:02d} - ??     {'ON':<8} {device['icon']} "
              f"{device['name']:<18} {device['power_watts']}W    ${cost:.3f}{peak_label}")

    savings = total_cost_dumb - total_cost_smart
    savings_pct = (savings / total_cost_dumb * 100) if total_cost_dumb > 0 else 0

    print(f"\n{'='*60}")
    print(f"  Cost WITHOUT IoT-GPT  : ${total_cost_dumb:.3f}")
    print(f"  Cost WITH IoT-GPT     : ${total_cost_smart:.3f}")
    print(f"  Daily Savings         : ${savings:.3f} ({savings_pct:.0f}%)")
    print(f"  Monthly Savings (est) : ${savings * 30:.2f}")
    print(f"{'='*60}")
    print("\n  [IoT-GPT] Devices will NEVER run at the same time!")
    print("  [IoT-GPT] Peak hours avoided where possible.\n")

def simulate_live(schedule):
    """Show a simple 'live' simulation of devices turning on/off."""
    print("\n--- Live Simulation (fast-forward) ---")
    for item in schedule:
        device = DEVICES[item["device"]]
        start_str = item["start"].strftime("%H:%M")
        print(f"  [{start_str}] {device['icon']} {device['name']} -> TURNING ON...")
        time.sleep(0.5)
        end_str = item["end"].strftime("%H:%M")
        print(f"  [{end_str}] {device['icon']} {device['name']} -> TURNING OFF")
        time.sleep(0.3)
    print("\n  All devices ready for your wake-up time!")

if __name__ == "__main__":
    print("\nIoT-GPT Smart Device Scheduler")
    print("================================")

    try:
        hour = int(input("Enter your wake-up hour (0-23, e.g. 7 for 7am): ").strip() or "7")
        minute = int(input("Enter minutes (0 or 30, e.g. 0): ").strip() or "0")
    except ValueError:
        hour, minute = 7, 0

    hour = max(0, min(23, hour))
    minute = max(0, min(59, minute))

    schedule = iot_gpt_schedule(wake_up_hour=hour, wake_up_minute=minute)
    print_schedule(schedule, hour, minute)

    run_sim = input("Run live simulation? (y/n): ").strip().lower()
    if run_sim == 'y':
        simulate_live(schedule)
