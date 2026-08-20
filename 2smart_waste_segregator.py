import requests

# Koi bhi website ka status dekho
r = requests.get("https://google.com")
print(r.status_code) # 200 aaya toh website ON hai