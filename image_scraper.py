import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = "https://books.toscrape.com"
print(f"Scraping {url}...")

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

images = soup.find_all('img')
print(f"Total {len(images)} images mili!\n")

if not os.path.exists('downloaded_images'):
    os.mkdir('downloaded_images')

for i, img in enumerate(images[:5]):
    img_url = img.get('src')
    full_url = urljoin(url, img_url)
    print(f"{i+1}. {full_url}")
    
    data = requests.get(full_url).content
    with open(f'downloaded_images/image_{i+1}.jpg', 'wb') as f:
        f.write(data)

print("\nDONE! Folder check karo!")