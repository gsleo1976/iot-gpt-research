"""
IoT-GPT Sample Program 05: Air Quality Monitor
===============================================
Check real-time air quality (AQI) for any city worldwide.
Connects to the free Open-Meteo air quality API.

AQI (Air Quality Index):
  0-50   : Good (Green)
  51-100 : Moderate (Yellow)
  101-150: Unhealthy for Sensitive Groups (Orange)
  151-200: Unhealthy (Red)
  200+   : Very Unhealthy / Hazardous (Purple)

How to run:
    pip install requests
    python 05_air_quality_monitor.py

This is useful for IoT-GPT to decide when to open windows,
run air purifiers, or send calm alerts.
"""

import requests

# City coordinates (latitude, longitude) for common cities
CITIES = {
    "Toronto":      (43.65, -79.38),
    "Mumbai":       (19.08, 72.88),
    "London":       (51.51, -0.13),
    "New York":     (40.71, -74.01),
    "Delhi":        (28.67, 77.22),
    "Beijing":      (39.91, 116.39),
    "Sydney":       (-33.87, 151.21),
    "Vancouver":    (49.25, -123.12),
    "Singapore":    (1.35, 103.82),
    "Dubai":        (25.20, 55.27),
}

def get_aqi_color(aqi):
    """Return color category and description for an AQI value."""
    if aqi <= 50:
        return "GREEN", "Good", "Air quality is satisfactory."
    elif aqi <= 100:
        return "YELLOW", "Moderate", "Acceptable air quality. Sensitive people may be affected."
    elif aqi <= 150:
        return "ORANGE", "Unhealthy (Sensitive Groups)", "Children/elderly should limit outdoor time."
    elif aqi <= 200:
        return "RED", "Unhealthy", "Everyone may experience health effects."
    elif aqi <= 300:
        return "PURPLE", "Very Unhealthy", "Health alert: everyone is affected."
    else:
        return "MAROON", "Hazardous", "Health emergency! Avoid outdoor activities."

def get_air_quality(lat, lon):
    """Fetch air quality data from Open-Meteo (free, no API key needed)."""
    url = (
        f"https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={lat}&longitude={lon}"
        f"&current=us_aqi,pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone"
    )
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None

def display_air_quality(city_name, lat, lon):
    """Display air quality report for a city."""
    print(f"\n{'='*55}")
    print(f"  Air Quality Report: {city_name}")
    print(f"  Coordinates: {lat}, {lon}")
    print(f"{'='*55}")

    data = get_air_quality(lat, lon)

    if data is None:
        print("\n  [Offline] Sample data shown:\n")
        print(f"  AQI         : 42 (Good)")
        print(f"  PM2.5       : 8 µg/m3")
        print(f"  PM10        : 15 µg/m3")
        print(f"  Ozone       : 52 µg/m3")
        print(f"  NO2         : 18 µg/m3")
        print(f"\n  Status      : GREEN - Good")
        print(f"  Advice      : Air quality is satisfactory.")
        print(f"\n  [IoT-GPT] Open windows / no air purifier needed.")
        return

    current = data.get("current", {})
    aqi = current.get("us_aqi", 0)
    pm25 = current.get("pm2_5", "N/A")
    pm10 = current.get("pm10", "N/A")
    ozone = current.get("ozone", "N/A")
    no2 = current.get("nitrogen_dioxide", "N/A")
    co = current.get("carbon_monoxide", "N/A")

    color, category, advice = get_aqi_color(aqi)

    print(f"\n  AQI         : {aqi} ({category})")
    print(f"  PM2.5       : {pm25} µg/m3  (fine particles)")
    print(f"  PM10        : {pm10} µg/m3  (coarse particles)")
    print(f"  Ozone       : {ozone} µg/m3")
    print(f"  NO2         : {no2} µg/m3")
    print(f"  CO          : {co} µg/m3")
    print(f"\n  Status      : {color} - {category}")
    print(f"  Health Info : {advice}")

    # IoT-GPT decision
    print(f"\n  [IoT-GPT Smart Actions]")
    if aqi <= 50:
        print("  - Open windows: YES (fresh air is good!)")
        print("  - Air purifier: OFF")
        print("  - Calm light  : OFF (all clear)")
    elif aqi <= 100:
        print("  - Open windows: MAYBE (use judgment)")
        print("  - Air purifier: LOW mode")
        print("  - Calm light  : DIM AMBER (slight concern)")
    else:
        print("  - Open windows: NO (keep closed)")
        print("  - Air purifier: HIGH mode")
        print("  - Calm light  : BRIGHT RED (action needed!)")

def main():
    print("\nIoT-GPT Air Quality Monitor")
    print("============================")
    print("\nAvailable cities:")
    for i, city in enumerate(CITIES.keys(), 1):
        print(f"  {i:2}. {city}")

    print("\nOr type any city name to look up (it will use Toronto as fallback).")
    city_input = input("\nEnter city name or number: ").strip()

    # Check if user typed a number
    if city_input.isdigit():
        idx = int(city_input) - 1
        city_list = list(CITIES.items())
        if 0 <= idx < len(city_list):
            city_name, (lat, lon) = city_list[idx]
        else:
            city_name, (lat, lon) = "Toronto", CITIES["Toronto"]
    elif city_input.title() in CITIES:
        city_name = city_input.title()
        lat, lon = CITIES[city_name]
    else:
        city_name = city_input if city_input else "Toronto"
        lat, lon = CITIES.get("Toronto")

    display_air_quality(city_name, lat, lon)
    print(f"\n{'='*55}\n")

if __name__ == "__main__":
    main()
