## Simple text extraction (static page)
# Yeh script ek static webpage se title aur pehla paragraph extract karti hai using requests aur BeautifulSoup.

import requests
from bs4 import BeautifulSoup

# Step 1: Webpage ka HTML content le rahe hain
url = "https://webscraper.io/test-sites/e-commerce/allinone"
response = requests.get(url)

# Step 2: HTML ko BeautifulSoup se parse kar rahe hain
soup = BeautifulSoup(response.text, "html.parser")

# Page ka pehla h1 title nikal rahe hain
title = soup.find("h1").text

# Page ka pehla paragraph nikal rahe hain
first_paragraph = soup.find("p").text

# Title aur first paragraph print kar rahe hain
print("Title:", title)
print("First Paragraph:", first_paragraph)

