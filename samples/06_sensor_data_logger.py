"""
IoT-GPT Sample Program 06: Sensor Data Logger
==============================================
Log simulated sensor readings to a CSV file and analyze trends.
This is how IoT-GPT stores historical data for learning patterns!

Real-world use:
  - Replace the simulated sensor with a real DHT22 or BME280 sensor
  - Connect to Raspberry Pi GPIO pins
  - Log to InfluxDB for Grafana dashboards (as used in IoT-GPT)

How to run:
    python 06_sensor_data_logger.py

No extra libraries needed (uses built-in csv and random modules).
"""

import csv
import random
import time
import os
from datetime import datetime, timedelta

LOG_FILE = "sensor_log.csv"
FIELDNAMES = ["timestamp", "room", "temperature_c", "humidity_pct",
              "light_lux", "motion_detected", "co2_ppm"]

def simulate_sensor_reading(room, base_temp=22.0, base_humidity=50.0, hour=None):
    """
    Simulate a realistic sensor reading.
    Patterns change based on time of day (like a real home!)
    """
    if hour is None:
        hour = datetime.now().hour

    # Temperature varies through the day
    temp_offset = 0
    if 6 <= hour <= 9:     temp_offset = -1.5   # cooler in morning
    elif 12 <= hour <= 15: temp_offset = 2.0    # warmer in afternoon
    elif 22 <= hour or hour <= 5: temp_offset = -2.0  # cooler at night

    temperature = round(base_temp + temp_offset + random.uniform(-0.5, 0.5), 1)
    humidity = round(base_humidity + random.uniform(-3, 3), 1)

    # Light varies by time of day
    if 7 <= hour <= 20:
        light_lux = random.randint(200, 800)
    else:
        light_lux = random.randint(0, 50)

    # Motion: more likely during waking hours
    motion_prob = 0.7 if 7 <= hour <= 22 else 0.05
    motion = random.random() < motion_prob

    # CO2 rises when people are in the room
    co2_base = 600 if motion else 420
    co2 = random.randint(co2_base - 50, co2_base + 150)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "room": room,
        "temperature_c": temperature,
        "humidity_pct": humidity,
        "light_lux": light_lux,
        "motion_detected": int(motion),
        "co2_ppm": co2
    }

def init_log_file():
    """Create the CSV log file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        print(f"  Created new log file: {LOG_FILE}")
    else:
        print(f"  Appending to existing log: {LOG_FILE}")

def log_reading(reading):
    """Append a sensor reading to the CSV log file."""
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(reading)

def analyze_log():
    """Read the log file and show statistics."""
    if not os.path.exists(LOG_FILE):
        print("  No log file found. Run the logger first!")
        return

    readings = []
    with open(LOG_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            readings.append(row)

    if not readings:
        print("  Log file is empty.")
        return

    print(f"\n  Total readings logged: {len(readings)}")

    # Group by room
    rooms = set(r["room"] for r in readings)
    for room in rooms:
        room_readings = [r for r in readings if r["room"] == room]
        temps = [float(r["temperature_c"]) for r in room_readings]
        humidity = [float(r["humidity_pct"]) for r in room_readings]
        co2 = [int(r["co2_ppm"]) for r in room_readings]
        motions = [int(r["motion_detected"]) for r in room_readings]

        print(f"\n  Room: {room.upper()}")
        print(f"    Temperature : avg={sum(temps)/len(temps):.1f}°C, "
              f"min={min(temps)}°C, max={max(temps)}°C")
        print(f"    Humidity    : avg={sum(humidity)/len(humidity):.1f}%")
        print(f"    CO2         : avg={sum(co2)//len(co2)} ppm, max={max(co2)} ppm")
        print(f"    Occupancy   : {sum(motions)}/{len(motions)} readings showed motion "
              f"({sum(motions)/len(motions)*100:.0f}%)")

        # IoT-GPT pattern detection
        if sum(motions) / len(motions) > 0.5:
            print(f"    [IoT-GPT] Room is frequently occupied - keep climate optimal")
        if max(co2) > 1000:
            print(f"    [IoT-GPT] CO2 peaked high - improve ventilation!")
        if max(temps) - min(temps) > 5:
            print(f"    [IoT-GPT] Large temp swings - consider smart heating schedule")

def main():
    print("\n" + "="*60)
    print("  IoT-GPT Sensor Data Logger")
    print("="*60 + "\n")

    print("Choose mode:")
    print("  1. Start logging (simulated sensor, 10 readings)")
    print("  2. Analyze existing log file")
    print("  3. Generate 24-hour historical data (for testing)")

    choice = input("\nEnter choice (1/2/3): ").strip() or "1"

    if choice == "1":
        init_log_file()
        rooms = ["bedroom", "living_room", "kitchen"]
        print(f"\nLogging sensor data every 2 seconds... (Ctrl+C to stop)\n")
        print(f"  {'Timestamp':<22} {'Room':<14} {'Temp':>6} {'Humidity':>9} {'Light':>8} {'Motion':>7} {'CO2':>7}")
        print("  " + "-"*72)
        try:
            for i in range(10):
                for room in rooms:
                    reading = simulate_sensor_reading(room)
                    log_reading(reading)
                    print(f"  {reading['timestamp']:<22} {reading['room']:<14} "
                          f"{reading['temperature_c']:>5}°C "
                          f"{reading['humidity_pct']:>7}% "
                          f"{reading['light_lux']:>6}lux "
                          f"{'YES' if reading['motion_detected'] else 'no':>7} "
                          f"{reading['co2_ppm']:>6}ppm")
                print()
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n\nLogging stopped by user.")

        print(f"\nData saved to: {LOG_FILE}")
        analyze_log()

    elif choice == "2":
        analyze_log()

    elif choice == "3":
        print("\nGenerating 24 hours of historical data (1 reading per hour)...")
        init_log_file()
        base_time = datetime.now() - timedelta(hours=24)
        count = 0
        for h in range(24):
            sim_time = base_time + timedelta(hours=h)
            for room in ["bedroom", "living_room", "kitchen"]:
                reading = simulate_sensor_reading(room, hour=sim_time.hour)
                reading["timestamp"] = sim_time.strftime("%Y-%m-%d %H:%M:%S")
                log_reading(reading)
                count += 1
        print(f"Generated {count} readings.")
        analyze_log()

    print(f"\n{'='*60}\n")

if __name__ == "__main__":
    main()
