from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome browser ko open kar rahe hain
driver = webdriver.Chrome()

# GeeksforGeeks ki python tutorial wali website open kar rahe hain
driver.get("https://www.geeksforgeeks.org/python/python-programming-language-tutorial/")

# Sare h1 headings ko dhundh rahe hain page par
li = driver.find_elements(By.CSS_SELECTOR, "h1")

# Har heading ka text print kar rahe hain
for q in li:
    print(q.text.strip())

# Browser band kar rahe hain
driver.quit()
# Ye code Selenium se webpage ka dynamic content extract karne ke liye hai.