import requests
from bs4 import BeautifulSoup

# Website ka URL jahan se images ke URLs nikalne hain
url = "https://webscraper.io/test-sites/e-commerce/allinone"

# Website ka HTML content le rahe hain
response = requests.get(url)

# HTML ko parse kar rahe hain BeautifulSoup se
soup = BeautifulSoup(response.text, "html.parser")

# Sare <img> tags dhundh rahe hain aur unka src attribute print kar rahe hain
for img in soup.find_all("img"):
    print(img.get("src"))