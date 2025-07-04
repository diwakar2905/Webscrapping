import requests
from bs4 import BeautifulSoup

# GeeksforGeeks ki python tutorial wali website ka URL
url = "https://www.geeksforgeeks.org/python/python-programming-language-tutorial/"

# Website ka HTML content le rahe hain
response = requests.get(url)

# HTML ko parse kar rahe hain BeautifulSoup se
soup = BeautifulSoup(response.text, "html.parser")

# Sare <code> tags dhundh rahe hain aur unka text print kar rahe hain
for code in soup.find_all("code"):
    print(code.text.strip())
