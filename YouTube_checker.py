import requests
import socket
import time
from datetime import datetime

print("=== HACKER TOOL - WEBSITE CHECKER ===")
site = input("Website ka naam likho (ex: google.com): ")

try:
    # 1. IP nikalna
    ip = socket.gethostbyname(site)
    print(f"\nIP Address: {ip}")

    # 2. Status check
    print("Checking status...")
    time.sleep(1)
    r = requests.get("https://" + site, timeout=5)

    if r.status_code == 200:
        print(f"✅ {site} is ONLINE! (Status: {r.status_code})")
    else:
        print(f"❌ {site} is OFFLINE! (Status: {r.status_code})")

    print(f"\nChecked at: {datetime.now()}")

except Exception as e:
    print(f"❌ Error: Website nahi mili ya Net off hai!")

# Bonus: Wifi / Port scanner jaisa
print("\n--- Port Scan (Top 3 ports) ---")
for port in [80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} : OPEN")
    else:
        print(f"Port {port} : CLOSED")
    s.close()