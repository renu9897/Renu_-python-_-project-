import requests
import socket
import time
from datetime import datetime

print("=== HACKER TOOL - WEBSITE CHECKER ===")
site = input("Website ka naam likho (ex: google.com): ")

try:
    # 1. Time dikhao
    print(f"\n[START TIME]: {datetime.now()}")
    print(f"Target: {site}")

    # 2. Timer / Delay Lagaya
    print("\nConnecting", end="")
    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print("\n")

    # 3. IP nikalna
    ip = socket.gethostbyname(site)
    print(f"IP Address: {ip}")

    # 4. Status check with 2 second delay
    print("\nChecking status...")
    time.sleep(2)
    r = requests.get("https://" + site, timeout=5)

    if r.status_code == 200:
        print(f"✅ {site} is ONLINE! (Status: {r.status_code})")
    else:
        print(f"❌ {site} is OFFLINE! (Status: {r.status_code})")

    print(f"\n[END TIME]: {datetime.now()}")
    total_time = datetime.now()
    print(f"Checked at: {total_time.strftime('%d-%m-%Y %H:%M:%S')}")

except Exception as e:
    print(f"❌ Error: Website nahi mili ya Net off hai!")

# Bonus: Port Scan with delay timer
print("\n--- Port Scan (Top 3 ports) ---")
for port in [80, 443, 8080]:
    print(f"Scanning Port {port}...", end=" ")
    time.sleep(1) # Har port pe 1 second ka delay
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print("OPEN")
    else:
        print("CLOSED")
    s.close()

print("\n--- Scan Complete ---")