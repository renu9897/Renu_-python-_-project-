import os
import subprocess

print("Files in this folder:")
print(os.listdir())

print("\n--- Checking Google Connection ---")
subprocess.run(["ping", "-c", "1", "google.com"])