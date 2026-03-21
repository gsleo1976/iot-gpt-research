"""
IoT-GPT Sample Program 07: Calm Technology Light Simulator
===========================================================
Simulate the IoT-GPT "Calm Notification" system.
Instead of buzzing your phone, a smart bulb on your shoe rack
glows a gentle color to give you ambient information.

Based on the research by Mark Weiser & John Seely Brown (1995):
"Designing Calm Technology" - technology that moves between
the periphery and center of attention.

Examples in this program:
  - BLUE light  : Snow expected today (wear boots!)
  - RED light   : High CO2 in bedroom (open window)
  - AMBER light : Energy peak hour starting soon
  - GREEN light : All good, everything normal
  - PURPLE light: Air quality is poor outside

How to run:
    python 07_calm_light_simulator.py

No extra libraries needed!
"""

import time
import random
from datetime import datetime

# Color codes for terminal output (ANSI escape codes)
COLORS = {
    "BLUE":   "\033[94m",
    "RED":    "\033[91m",
    "AMBER":  "\033[93m",
    "GREEN":  "\033[92m",
    "PURPLE": "\033[95m",
    "WHITE":  "\033[97m",
    "CYAN":   "\033[96m",
    "OFF":    "\033[90m",
    "RESET":  "\033[0m",
    "BOLD":   "\033[1m",
}

# Peak electricity hours
PEAK_HOURS = [(6, 9), (17, 20)]

def get_color(name):
    return COLORS.get(name.upper(), COLORS["RESET"])

def print_bulb(color_name, state, room="Shoe Rack"):
    """Display a visual representation of the IoT bulb."""
    c = get_color(color_name)
    reset = COLORS["RESET"]
    bold = COLORS["BOLD"]
    off = COLORS["OFF"]

    if state == "OFF":
        print(f"\n  {off}   [ O ]   {reset}  {room} Light: {off}OFF{reset}")
    else:
        print(f"\n  {c}{bold}  [({color_name[0]})]  {reset}  {room} Light: {c}{bold}{color_name}{reset} - {state}")

def is_peak_hour():
    hour = datetime.now().hour
    for start, end in PEAK_HOURS:
        if start <= hour < end:
            return True
    return False

def calm_notification_engine(sensors):
    """
    The calm notification engine.
    Reads all sensor values and decides what color the light should be.

    Priority order (highest to lowest):
    1. CO2 too high (health emergency)
    2. Snow forecast (practical daily info)
    3. Air quality poor
    4. Energy peak hour
    5. All good
    """
    notifications = []

    # Check CO2
    co2 = sensors.get("co2_ppm", 0)
    if co2 > 1200:
        notifications.append({
            "priority": 1,
            "color": "RED",
            "reason": f"CO2 very high: {co2} ppm in bedroom",
            "action": "Open windows NOW!",
            "brightness": "BRIGHT"
        })

    # Check snow
    if sensors.get("snow_forecast", False):
        notifications.append({
            "priority": 2,
            "color": "BLUE",
            "reason": "Snow expected today",
            "action": "Wear snow boots!",
            "brightness": "SOFT GLOW"
        })

    # Check air quality
    aqi = sensors.get("aqi", 0)
    if aqi > 150:
        notifications.append({
            "priority": 3,
            "color": "PURPLE",
            "reason": f"Outdoor air quality poor: AQI {aqi}",
            "action": "Keep windows closed, run air purifier",
            "brightness": "MEDIUM PULSE"
        })

    # Check energy peak
    if sensors.get("peak_hour", False):
        minutes_to_peak = sensors.get("minutes_to_peak", 0)
        if minutes_to_peak <= 15:
            notifications.append({
                "priority": 4,
                "color": "AMBER",
                "reason": f"Electricity peak hour starts in {minutes_to_peak} min",
                "action": "Delay high-power devices",
                "brightness": "SLOW PULSE"
            })

    # Check for water leak
    if sensors.get("water_leak", False):
        notifications.append({
            "priority": 0,  # HIGHEST priority
            "color": "RED",
            "reason": "WATER LEAK DETECTED!",
            "action": "Check under sink immediately!",
            "brightness": "FAST BLINK"
        })

    if not notifications:
        return {
            "color": "GREEN",
            "reason": "All systems normal",
            "action": "No action needed",
            "brightness": "OFF"  # Off means all good - true calm tech!
        }

    # Return highest priority notification
    return sorted(notifications, key=lambda x: x["priority"])[0]

def run_scenarios():
    """Run through different scenarios to demonstrate calm technology."""
    scenarios = [
        {
            "name": "Morning - All Normal",
            "sensors": {
                "co2_ppm": 450, "snow_forecast": False,
                "aqi": 35, "peak_hour": False, "water_leak": False
            }
        },
        {
            "name": "Morning - Snow Forecast",
            "sensors": {
                "co2_ppm": 500, "snow_forecast": True,
                "aqi": 40, "peak_hour": False, "water_leak": False
            }
        },
        {
            "name": "Evening - Peak Hour Warning",
            "sensors": {
                "co2_ppm": 600, "snow_forecast": False,
                "aqi": 55, "peak_hour": True, "minutes_to_peak": 10, "water_leak": False
            }
        },
        {
            "name": "Stuffy Bedroom - High CO2",
            "sensors": {
                "co2_ppm": 1350, "snow_forecast": False,
                "aqi": 40, "peak_hour": False, "water_leak": False
            }
        },
        {
            "name": "Emergency - Water Leak!",
            "sensors": {
                "co2_ppm": 450, "snow_forecast": False,
                "aqi": 40, "peak_hour": False, "water_leak": True
            }
        },
    ]

    print("\n" + "="*60)
    print(f"  {COLORS['BOLD']}IoT-GPT Calm Technology Light Simulator{COLORS['RESET']}")
    print("  (Based on Weiser & Brown Calm Tech principles)")
    print("="*60)

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'─'*50}")
        print(f"  Scenario {i}: {scenario['name']}")
        print(f"{'─'*50}")

        # Show sensor values
        s = scenario["sensors"]
        print(f"  Sensor readings:")
        print(f"    CO2          : {s.get('co2_ppm', '?')} ppm")
        print(f"    Snow forecast: {'YES' if s.get('snow_forecast') else 'No'}")
        print(f"    Air Quality  : AQI {s.get('aqi', '?')}")
        print(f"    Peak hour    : {'YES' if s.get('peak_hour') else 'No'}")
        print(f"    Water leak   : {'DETECTED!' if s.get('water_leak') else 'None'}")

        # Get calm notification
        notification = calm_notification_engine(scenario["sensors"])

        print(f"\n  IoT-GPT Decision:")
        print(f"    Reason   : {notification['reason']}")
        print(f"    Bulb     : {notification['color']} ({notification['brightness']})")
        print(f"    Message  : {notification['action']}")

        # Visual display
        if notification["brightness"] == "OFF":
            print_bulb("OFF", "OFF")
            print(f"  {COLORS['GREEN']}  -> Bulb is dark. You won't be disturbed!{COLORS['RESET']}")
        else:
            print_bulb(notification["color"], notification["brightness"])
            print(f"  -> No buzzing, no popup - just a gentle ambient glow!")

        time.sleep(0.8)

    print(f"\n{'='*60}")
    print("  Key Insight: Calm Technology works at the PERIPHERY")
    print("  of attention. You notice it without being interrupted.")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    run_scenarios()
