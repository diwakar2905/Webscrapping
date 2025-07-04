import requests
from bs4 import BeautifulSoup

# Website ka URL jahan se data nikalna hai
url = "https://webscraper.io/test-sites/e-commerce/allinone"

# Website ka HTML content le rahe hain
response = requests.get(url)

# HTML ko parse kar rahe hain BeautifulSoup se
soup = BeautifulSoup(response.text, "html.parser")

# Sare <h2> headings dhundh rahe hain aur unka text print kar rahe hain
for heading in soup.find_all("h2"):
    print(heading.text.strip())