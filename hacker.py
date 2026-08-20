print("\n--- 4. Ping Test (subprocess) ---")
import subprocess
result = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True)
print(result.stdout[:200])p