"""
IoT-GPT Sample Program 10: Sunrise/Sunset Based Automation
===========================================================
Automatically adjust your smart home based on sunrise and sunset times.
This is how IoT-GPT adapts schedules to the ACTUAL time of year!

In winter, sunset is at 4:30pm - lights should turn on earlier.
In summer, sunrise is at 5am - wake-up routine can start later.

Uses the FREE sunrise-sunset.org API - no API key needed!

How to run:
    pip install requests
    python 10_sunrise_and_automation.py
"""

import requests
from datetime import datetime, timedelta
import time

# City coordinates
CITIES = {
    "Toronto":   {"lat": 43.65, "lng": -79.38, "timezone": "America/Toronto"},
    "London":    {"lat": 51.51, "lng": -0.13,  "timezone": "Europe/London"},
    "Mumbai":    {"lat": 19.08, "lng": 72.88,  "timezone": "Asia/Kolkata"},
    "New York":  {"lat": 40.71, "lng": -74.01, "timezone": "America/New_York"},
    "Dubai":     {"lat": 25.20, "lng": 55.27,  "timezone": "Asia/Dubai"},
    "Sydney":    {"lat": -33.87,"lng": 151.21, "timezone": "Australia/Sydney"},
}

def get_sun_times(lat, lng):
    """Get today's sunrise and sunset for given coordinates."""
    url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if data["status"] == "OK":
            results = data["results"]
            # Times are in UTC; convert to local datetime
            sunrise_utc = datetime.fromisoformat(results["sunrise"].replace("Z", "+00:00"))
            sunset_utc  = datetime.fromisoformat(results["sunset"].replace("Z", "+00:00"))
            # Approximate local offset (simplified for demo)
            sunrise_local = sunrise_utc.replace(tzinfo=None)
            sunset_local  = sunset_utc.replace(tzinfo=None)
            day_length_hrs = (sunset_utc - sunrise_utc).total_seconds() / 3600
            return sunrise_local, sunset_local, day_length_hrs
        return None, None, None
    except Exception:
        return None, None, None

def plan_automation(city_name, sunrise, sunset, day_length_hrs):
    """
    Generate IoT-GPT automation schedule based on sun times.
    This replaces fixed schedules with nature-aware ones!
    """
    print(f"\n{'='*60}")
    print(f"  IoT-GPT Sun-Aware Automation: {city_name}")
    print(f"{'='*60}\n")

    if sunrise is None:
        # Sample data for offline demo
        sunrise = datetime.now().replace(hour=7, minute=12, second=0)
        sunset  = datetime.now().replace(hour=17, minute=45, second=0)
        day_length_hrs = 10.5
        print("  [Offline mode - showing sample times]\n")

    print(f"  Sunrise: {sunrise.strftime('%I:%M %p')}")
    print(f"  Sunset : {sunset.strftime('%I:%M %p')}")
    print(f"  Day Length: {day_length_hrs:.1f} hours\n")

    # Wake-up time: 30 min before sunrise (or 6:30am minimum)
    wake_time = sunrise - timedelta(minutes=30)
    if wake_time.hour < 6:
        wake_time = wake_time.replace(hour=6, minute=30)

    # Morning warm-up: room heater starts 20 min before wake
    heater_on  = wake_time - timedelta(minutes=20)
    # Water heater: 30 min before wake
    water_on   = wake_time - timedelta(minutes=30)

    # Outdoor light: turn on 10 min after sunset
    outdoor_light_on = sunset + timedelta(minutes=10)
    # Bedroom wind-down: 2 hours after sunset
    wind_down = sunset + timedelta(hours=2)
    # Bedtime lights dim: 30 min before bed (3h after sunset)
    lights_dim = sunset + timedelta(hours=2, minutes=30)

    automation = [
        (water_on,          "💧 Water Heater",       "ON",      "Heat water for morning shower"),
        (heater_on,         "🔥 Room Heater",         "ON",      "Warm bedroom before wake-up"),
        (wake_time,         "💡 Morning Lights",      "ON-WARM", "Gentle sunrise-warmth color"),
        (wake_time + timedelta(hours=1), "🔥 Room Heater", "OFF", "Room warm enough, save energy"),
        (outdoor_light_on,  "🏠 Outdoor Lights",      "ON",      "Lights on as sun goes down"),
        (wind_down,         "💡 Living Room Lights",  "DIM-60%", "Evening wind-down mode"),
        (lights_dim,        "💡 All Lights",          "DIM-20%", "Pre-sleep dim signal"),
        (lights_dim + timedelta(minutes=30), "🏠 Outdoor Lights", "OFF", "Save overnight energy"),
    ]

    print(f"  {'Time':<12} {'Device':<22} {'Action':<12} {'Why'}")
    print("  " + "─"*65)
    for t, device, action, reason in automation:
        print(f"  {t.strftime('%I:%M %p'):<12} {device:<22} {action:<12} {reason}")

    # Compare with FIXED schedule (not sun-aware)
    print(f"\n  --- If you used a FIXED schedule instead: ---")
    fixed_events = [
        ("06:30 AM", "All devices", "ON"),
        ("07:00 PM", "Outdoor lights", "ON"),
        ("10:00 PM", "All lights", "DIM"),
    ]
    for t, device, action in fixed_events:
        print(f"  {t:<12} {device:<22} {action}")

    # Calculate waste
    season_note = ""
    if day_length_hrs < 10:
        season_note = "Short winter day - lights needed earlier, saved by sun-awareness!"
    elif day_length_hrs > 14:
        season_note = "Long summer day - fixed schedule would waste energy on lights!"
    else:
        season_note = "Near-equinox day - minimal difference between approaches."

    print(f"\n  Day length insight: {season_note}")

    if day_length_hrs < 10:
        saved_light_mins = 60
        saved_kwh = (12 / 1000) * (saved_light_mins / 60) * 5  # 5 lights
        print(f"  Estimated light energy saved today: {saved_kwh:.4f} kWh")

    print(f"\n  [IoT-GPT] Schedule automatically updates EVERY DAY")
    print(f"  as sunrise/sunset changes through the year.")

def show_yearly_pattern(city_name, lat, lng):
    """Show how day length changes across months."""
    print(f"\n  {'─'*50}")
    print(f"  Approximate day lengths in {city_name} by month:")
    print(f"  {'─'*50}")

    # Approximate day lengths (hours) for each month at mid-latitudes
    # Values are estimates for a ~45°N latitude location
    month_data = {
        "Jan": 9.0,  "Feb": 10.2, "Mar": 11.8, "Apr": 13.5,
        "May": 14.9, "Jun": 15.6, "Jul": 15.2, "Aug": 13.8,
        "Sep": 12.1, "Oct": 10.4, "Nov": 9.1,  "Dec": 8.5
    }

    # Adjust for latitude (rough approximation)
    lat_factor = abs(lat) / 45.0
    for month in month_data:
        # Amplify the seasonal swing based on latitude
        mid = 12.0
        month_data[month] = mid + (month_data[month] - mid) * lat_factor

    print(f"  {'Month':<8} {'Hours':<8} {'Bar'}")
    print("  " + "─"*40)
    for month, hours in month_data.items():
        bar = "█" * int(hours)
        print(f"  {month:<8} {hours:<8.1f} {bar}")

    print(f"\n  Longest day : ~{max(month_data.values()):.1f} hrs")
    print(f"  Shortest day: ~{min(month_data.values()):.1f} hrs")
    print(f"  IoT-GPT adjusts ALL schedules to match real daylight!")

def main():
    print("\n" + "="*60)
    print("  IoT-GPT Sunrise/Sunset Automation")
    print("="*60 + "\n")

    print("  Available cities:")
    for i, city in enumerate(CITIES.keys(), 1):
        print(f"    {i}. {city}")

    choice = input("\n  Enter city name or number: ").strip()

    if choice.isdigit():
        idx = int(choice) - 1
        city_list = list(CITIES.items())
        city_name, city_data = city_list[idx] if 0 <= idx < len(city_list) else city_list[0]
    elif choice.title() in CITIES:
        city_name = choice.title()
        city_data = CITIES[city_name]
    else:
        city_name = "Toronto"
        city_data = CITIES["Toronto"]

    print(f"\n  Fetching sun data for {city_name}...")
    sunrise, sunset, day_len = get_sun_times(city_data["lat"], city_data["lng"])

    plan_automation(city_name, sunrise, sunset, day_len or 10.5)
    show_yearly_pattern(city_name, city_data["lat"], city_data["lng"])
    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    main()
