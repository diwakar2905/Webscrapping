import requests
from bs4 import BeautifulSoup

# Step 1: Get the HTML content from the webpage
url = "https://webscraper.io/test-sites/e-commerce/allinone"
response = requests.get(url)

# Step 2: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

title=soup.find("h1").text
first_paragraph=soup.find("p").text

print("Title:", title)
print("First Paragraph:", first_paragraph)