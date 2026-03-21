"""
IoT-GPT Sample Program 01: Weather Forecast
==========================================
Get current weather and 3-day forecast for any city or country.
Uses the FREE wttr.in API - no API key needed!

How to run:
    python 01_weather_forecast.py

Requirements:
    pip install requests
"""

import requests
import json

def get_weather(city):
    """Fetch weather data for a city using wttr.in (free, no API key)."""
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("No internet connection. Showing sample data instead.\n")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def show_weather(city):
    """Display weather info in a friendly format."""
    print(f"\n{'='*50}")
    print(f"  Weather Forecast for: {city.upper()}")
    print(f"{'='*50}")

    data = get_weather(city)

    if data is None:
        # Show sample data so beginners can see the output format
        print("\n[SAMPLE OUTPUT - Connect to internet for real data]\n")
        print("Current Conditions:")
        print("  Temperature : 22°C")
        print("  Feels Like  : 20°C")
        print("  Weather     : Partly Cloudy")
        print("  Humidity    : 65%")
        print("  Wind Speed  : 15 km/h")
        print("\n3-Day Forecast:")
        print("  Today     : High 24°C / Low 16°C - Mostly Sunny")
        print("  Tomorrow  : High 20°C / Low 14°C - Light Rain")
        print("  Day 3     : High 18°C / Low 12°C - Cloudy")
        print("\n[IoT-GPT Alert] Snow probability is LOW. No blue light signal needed.")
        return

    current = data["current_condition"][0]
    temp_c = current["temp_C"]
    feels_like = current["FeelsLikeC"]
    weather_desc = current["weatherDesc"][0]["value"]
    humidity = current["humidity"]
    wind_speed = current["windspeedKmph"]

    print("\nCurrent Conditions:")
    print(f"  Temperature : {temp_c}°C")
    print(f"  Feels Like  : {feels_like}°C")
    print(f"  Weather     : {weather_desc}")
    print(f"  Humidity    : {humidity}%")
    print(f"  Wind Speed  : {wind_speed} km/h")

    print("\n3-Day Forecast:")
    days = ["Today", "Tomorrow", "Day 3"]
    for i, weather in enumerate(data["weather"][:3]):
        max_temp = weather["maxtempC"]
        min_temp = weather["mintempC"]
        desc = weather["hourly"][4]["weatherDesc"][0]["value"]  # midday
        print(f"  {days[i]:<10}: High {max_temp}°C / Low {min_temp}°C - {desc}")

    # IoT-GPT Calm Technology check: should the shoe-rack light glow blue?
    print("\n--- IoT-GPT Calm Technology Check ---")
    snow_chance = check_snow_probability(data)
    if snow_chance:
        print("  [ALERT] Snow is likely! Shoe-rack IoT light -> GLOW BLUE")
        print("  (Reminder: Wear boots when leaving home!)")
    else:
        print("  No snow expected. Shoe-rack light stays OFF.")

def check_snow_probability(data):
    """Check if snow is likely in the next 24 hours."""
    for weather in data["weather"][:2]:
        for hour in weather["hourly"]:
            desc = hour["weatherDesc"][0]["value"].lower()
            if "snow" in desc or "blizzard" in desc or "sleet" in desc:
                return True
    return False

if __name__ == "__main__":
    print("IoT-GPT Weather Forecast Tool")
    print("------------------------------")
    city = input("Enter a city name (e.g., Toronto, Mumbai, London): ").strip()
    if not city:
        city = "Toronto"  # default
    show_weather(city)
    print(f"\n{'='*50}\n")
