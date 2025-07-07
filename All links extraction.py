import requests
from bs4 import BeautifulSoup

# Website ka URL jahan se links nikalne hain
url = "https://webscraper.io/test-sites/e-commerce/allinone"

# Website ka HTML content le rahe hain
html = requests.get(url)

# HTML ko parse kar rahe hain BeautifulSoup se
soup = BeautifulSoup(html.text, "html.parser")

# Sare anchor tags (<a>) dhundh rahe hain jinke paas href attribute hai
for link in soup.find_all("a", href=True):
    # Har link ka href print kar
    print(link['href'])