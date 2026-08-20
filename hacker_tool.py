# Renu's Hacker Tool - Week 3 Project
import os, socket, requests, time
from datetime import datetime

print("=== RENU'S HACKER TOOL ===")
print(f"Time: {datetime.now()}")
print("\n--- 1. My Phone Info ---")
print(os.listdir('/storage/emulated/0/Download')[:5])

print("\n--- 2. Website Check ---")
site = "google.com"
print(f"{site} Status: {requests.get('https://'+site).status_code} (200 = ONLINE)")

print("\n--- 3. IP Finder ---")
ip = socket.gethostbyname(site)
print(f"{site} ka IP hai: {ip}")

print("\nTool Finished!")