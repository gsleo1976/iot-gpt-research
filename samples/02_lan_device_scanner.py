"""
IoT-GPT Sample Program 02: LAN Device Scanner
==============================================
Discover all devices connected to your local network.
This is how IoT-GPT finds and identifies smart devices!

How to run:
    python 02_lan_device_scanner.py

Requirements:
    pip install scapy   (for ARP scan - most accurate)
    OR just uses socket (built-in) for hostname resolution

Note: You may need to run with sudo/admin for ARP scan on some systems.
      The basic ping scan works without any extra permissions.
"""

import socket
import subprocess
import platform
import ipaddress
import concurrent.futures
from datetime import datetime

def get_local_ip():
    """Get the IP address of this computer on the local network."""
    try:
        # Connect to a public DNS server (doesn't actually send data)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "192.168.1.100"  # fallback

def ping_host(ip):
    """Ping a single IP address. Returns True if host is alive."""
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", "500", str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", str(ip)]

    try:
        result = subprocess.run(cmd, capture_output=True, timeout=2)
        return result.returncode == 0
    except Exception:
        return False

def get_hostname(ip):
    """Try to get the hostname of a device."""
    try:
        hostname = socket.gethostbyaddr(str(ip))[0]
        return hostname
    except Exception:
        return "Unknown"

def guess_device_type(hostname, ip):
    """
    Guess what kind of IoT device this might be based on hostname.
    This is a simplified version of IoT-GPT's Device Attribute Registry!
    """
    hostname_lower = hostname.lower()
    ip_str = str(ip)

    if any(x in hostname_lower for x in ["router", "gateway", "fritz", "tp-link", "netgear"]):
        return "Router/Gateway"
    elif any(x in hostname_lower for x in ["android", "samsung", "pixel"]):
        return "Android Phone/Tablet"
    elif any(x in hostname_lower for x in ["iphone", "ipad", "apple", "macbook"]):
        return "Apple Device"
    elif any(x in hostname_lower for x in ["raspberry", "raspi", "rpi"]):
        return "Raspberry Pi (IoT Hub!)"
    elif any(x in hostname_lower for x in ["smart", "bulb", "light", "hue", "sonoff", "tasmota"]):
        return "Smart Light/Switch"
    elif any(x in hostname_lower for x in ["camera", "cam", "hikvision", "dahua"]):
        return "IP Camera"
    elif any(x in hostname_lower for x in ["thermostat", "nest", "ecobee"]):
        return "Smart Thermostat"
    elif any(x in hostname_lower for x in ["tv", "chromecast", "firestick", "roku"]):
        return "Smart TV/Streaming"
    elif any(x in hostname_lower for x in ["printer", "hp-", "canon", "brother"]):
        return "Printer"
    elif any(x in hostname_lower for x in ["laptop", "desktop", "pc", "computer"]):
        return "Computer"
    else:
        return "Unknown Device"

def scan_network(network_base, max_hosts=50):
    """
    Scan the local network for active devices.
    Scans the first 'max_hosts' addresses for speed.
    """
    alive_hosts = []

    print(f"  Scanning {network_base}.1 to {network_base}.{max_hosts}...")
    print("  (This may take 15-30 seconds)\n")

    ips_to_scan = [f"{network_base}.{i}" for i in range(1, max_hosts + 1)]

    # Use threading to scan multiple IPs at once (much faster!)
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_ip = {executor.submit(ping_host, ip): ip for ip in ips_to_scan}
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                if future.result():
                    alive_hosts.append(ip)
                    print(f"  Found: {ip}")
            except Exception:
                pass

    return alive_hosts

def main():
    print("\n" + "="*60)
    print("  IoT-GPT LAN Device Scanner")
    print("  Discovering devices on your home network...")
    print("="*60 + "\n")

    # Get local IP and derive network base
    my_ip = get_local_ip()
    parts = my_ip.split(".")
    network_base = ".".join(parts[:3])  # e.g., "192.168.1"

    print(f"Your IP address : {my_ip}")
    print(f"Scanning network: {network_base}.0/24\n")

    scan_start = datetime.now()
    alive_hosts = scan_network(network_base, max_hosts=50)
    scan_end = datetime.now()

    print(f"\n{'='*60}")
    print(f"  Scan Complete! Found {len(alive_hosts)} device(s)")
    print(f"  Time taken: {(scan_end - scan_start).seconds} seconds")
    print(f"{'='*60}\n")

    if not alive_hosts:
        print("No devices found. Try running with administrator/sudo privileges.")
        print("Or check that you are connected to a local network.\n")
        # Show sample output
        print("[Sample Output]")
        alive_hosts = ["192.168.1.1", "192.168.1.5", "192.168.1.20", "192.168.1.42"]
        print(f"Found {len(alive_hosts)} devices (sample data)\n")

    print(f"{'IP Address':<18} {'Hostname':<30} {'Device Type'}")
    print("-" * 70)

    for ip in sorted(alive_hosts):
        hostname = get_hostname(ip)
        device_type = guess_device_type(hostname, ip)
        print(f"{ip:<18} {hostname:<30} {device_type}")

    print("\n[IoT-GPT Tip] Raspberry Pi devices are perfect as IoT hubs!")
    print("  Connect sensors and smart bulbs to automate your home.\n")

if __name__ == "__main__":
    main()
