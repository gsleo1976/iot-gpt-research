"""
IoT-GPT Sample Program 08: Energy Usage Tracker
================================================
Track and visualize energy consumption of smart home devices.
See exactly which devices cost you the most money and when!

This demonstrates how IoT-GPT measures "before vs after"
energy savings in Experiment 1 of the research project.

How to run:
    python 08_energy_usage_tracker.py

No extra libraries needed!
"""

import random
import csv
import os
from datetime import datetime, timedelta

# Device energy profiles (watts when running)
DEVICE_PROFILES = {
    "Room Heater":   {"watts": 1500, "avg_hours_day": 4.0, "controllable": True,  "icon": "🔥"},
    "Water Heater":  {"watts": 2000, "avg_hours_day": 1.5, "controllable": True,  "icon": "💧"},
    "Refrigerator":  {"watts": 150,  "avg_hours_day": 24,  "controllable": False, "icon": "❄"},
    "Washing Machine":{"watts": 500, "avg_hours_day": 1.0, "controllable": True,  "icon": "🌀"},
    "Smart TV":      {"watts": 120,  "avg_hours_day": 3.5, "controllable": True,  "icon": "📺"},
    "Laptop":        {"watts": 65,   "avg_hours_day": 6.0, "controllable": False, "icon": "💻"},
    "Smart Lights":  {"watts": 12,   "avg_hours_day": 5.0, "controllable": True,  "icon": "💡"},
    "Router":        {"watts": 15,   "avg_hours_day": 24,  "controllable": False, "icon": "📡"},
    "Air Purifier":  {"watts": 30,   "avg_hours_day": 8.0, "controllable": True,  "icon": "🌬"},
    "Microwave":     {"watts": 1200, "avg_hours_day": 0.25,"controllable": False, "icon": "📻"},
}

# Electricity pricing ($ per kWh)
PRICE_PEAK    = 0.22   # peak hours
PRICE_OFFPEAK = 0.09   # off-peak hours
PEAK_FRACTION = 0.35   # 35% of usage happens during peak hours

def calculate_daily_cost(device_name, profile, optimized=False):
    """
    Calculate daily energy cost for a device.
    If optimized=True, IoT-GPT shifts usage to off-peak hours.
    """
    watts = profile["watts"]
    hours = profile["avg_hours_day"]

    # Add some realistic variation
    hours_variation = hours + random.uniform(-0.2, 0.2)
    kwh = (watts / 1000) * hours_variation

    if optimized and profile["controllable"]:
        # IoT-GPT shifts controllable devices to off-peak
        cost = kwh * PRICE_OFFPEAK
        peak_used = 0.0
    else:
        # Normal usage: mix of peak and off-peak
        peak_kwh = kwh * PEAK_FRACTION
        offpeak_kwh = kwh * (1 - PEAK_FRACTION)
        cost = (peak_kwh * PRICE_PEAK) + (offpeak_kwh * PRICE_OFFPEAK)
        peak_used = peak_kwh

    return round(kwh, 3), round(cost, 4), round(peak_used, 3)

def show_energy_report(optimized=False):
    """Display a full energy usage report."""
    mode = "WITH IoT-GPT (Optimized)" if optimized else "WITHOUT IoT-GPT (Normal)"
    print(f"\n{'='*70}")
    print(f"  Energy Usage Report: {mode}")
    print(f"{'='*70}\n")

    print(f"  {'Device':<20} {'Power':<8} {'Hours/Day':<12} {'kWh/Day':<10} {'Cost/Day':<12} {'Monthly'}")
    print("  " + "-"*65)

    total_kwh = 0
    total_cost = 0
    total_monthly = 0

    device_results = []

    for device_name, profile in DEVICE_PROFILES.items():
        kwh, cost, peak_kwh = calculate_daily_cost(device_name, profile, optimized)
        monthly = cost * 30
        total_kwh += kwh
        total_cost += cost
        total_monthly += monthly

        status = ""
        if optimized and profile["controllable"]:
            status = " [shifted]"

        device_results.append((device_name, profile, kwh, cost, monthly, status))
        print(f"  {profile['icon']} {device_name:<19} {profile['watts']}W   "
              f"  {profile['avg_hours_day']:<11.1f} {kwh:<10.3f} ${cost:<11.4f} ${monthly:.2f}{status}")

    print("  " + "-"*65)
    print(f"  {'TOTAL':<20} {'':<8} {'':<12} {total_kwh:<10.3f} ${total_cost:<11.4f} ${total_monthly:.2f}")

    return total_cost, total_monthly

def compare_savings():
    """Compare normal vs IoT-GPT optimized energy usage."""
    print("\n" + "="*70)
    print("  IoT-GPT Energy Savings Comparison")
    print("="*70)

    # Fix random seed for consistent comparison
    random.seed(42)
    cost_normal, monthly_normal = show_energy_report(optimized=False)

    random.seed(42)
    cost_optimized, monthly_optimized = show_energy_report(optimized=True)

    daily_savings = cost_normal - cost_optimized
    monthly_savings = monthly_normal - monthly_optimized
    annual_savings = monthly_savings * 12
    savings_pct = (daily_savings / cost_normal) * 100 if cost_normal > 0 else 0

    print(f"\n{'='*70}")
    print(f"  SAVINGS SUMMARY")
    print(f"{'='*70}")
    print(f"  Daily cost  (normal)   : ${cost_normal:.4f}")
    print(f"  Daily cost  (IoT-GPT)  : ${cost_optimized:.4f}")
    print(f"  Daily savings          : ${daily_savings:.4f} ({savings_pct:.1f}%)")
    print(f"  Monthly savings        : ${monthly_savings:.2f}")
    print(f"  Annual savings         : ${annual_savings:.2f}")
    print(f"\n  [IoT-GPT method] Shifts controllable devices to off-peak hours.")
    print(f"  [Target in research]   15-25% energy reduction.")

    # Show CO2 impact
    co2_saved_kg = annual_savings * 0.42  # rough: $1 saved ~ 0.42 kg CO2
    print(f"\n  Environmental Impact:")
    print(f"  CO2 saved per year (est.) : {co2_saved_kg:.1f} kg")
    print(f"  Equivalent to planting    : {co2_saved_kg/21:.0f} trees")
    print(f"{'='*70}\n")

def export_to_csv(days=7):
    """Generate and export 7 days of energy data to CSV."""
    filename = "energy_usage_history.csv"
    fieldnames = ["date", "device", "kwh", "cost_usd", "optimized"]

    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for day in range(days):
            date = (datetime.now() - timedelta(days=days - day)).strftime("%Y-%m-%d")
            optimized = day >= (days // 2)  # first half normal, second half optimized

            for device_name, profile in DEVICE_PROFILES.items():
                kwh, cost, _ = calculate_daily_cost(device_name, profile, optimized)
                writer.writerow({
                    "date": date,
                    "device": device_name,
                    "kwh": kwh,
                    "cost_usd": cost,
                    "optimized": optimized
                })

    print(f"\n  Exported {days} days of data to: {filename}")
    print(f"  Open this in Excel or Python pandas to create charts!")

if __name__ == "__main__":
    print("\nIoT-GPT Energy Usage Tracker")
    print("=============================")
    print("\nOptions:")
    print("  1. View normal usage (without IoT-GPT)")
    print("  2. View optimized usage (with IoT-GPT)")
    print("  3. Compare both (savings analysis)")
    print("  4. Export 7-day history to CSV")

    choice = input("\nEnter choice (1/2/3/4): ").strip() or "3"

    if choice == "1":
        show_energy_report(optimized=False)
    elif choice == "2":
        show_energy_report(optimized=True)
    elif choice == "3":
        compare_savings()
    elif choice == "4":
        export_to_csv()
    else:
        compare_savings()
