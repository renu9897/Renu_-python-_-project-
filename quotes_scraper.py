import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

quotes = soup.find_all('span', class_='text')
print(f"Total {len(quotes)} quotes mile:\n")
for q in quotes:
    print(f"-> {q.text}")