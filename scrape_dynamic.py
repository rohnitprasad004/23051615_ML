
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://quotes.toscrape.com/js/"   # THIS IS TRULY DYNAMIC
driver.get(url)

time.sleep(3)   

quotes = []
authors = []

quote_tags = driver.find_elements(By.CLASS_NAME, "text")
author_tags = driver.find_elements(By.CLASS_NAME, "author")

for q, a in zip(quote_tags, author_tags):
    quotes.append(q.text)
    authors.append(a.text)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

print(df)
df.to_csv("dynamic_quotes.csv", index=False)

driver.quit()
