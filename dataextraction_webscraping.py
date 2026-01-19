import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the static website (example site)
url = "https://quotes.toscrape.com/"

# Step 1: Send GET request
response = requests.get(url)

# Step 2: Check response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract data
    quotes = []
    authors = []

    quote_elements = soup.find_all("span", class_="text")
    author_elements = soup.find_all("small", class_="author")

    for q, a in zip(quote_elements, author_elements):
        quotes.append(q.text)
        authors.append(a.text)

    # Step 4: Convert to DataFrame
    df = pd.DataFrame({
        "Quote": quotes,
        "Author": authors
    })

    print(df)

    # Step 5: Save to CSV
    df.to_csv("scraped_quotes.csv", index=False)
    print("\nData Saved to scraped_quotes.csv")

else:
    print("Failed to retrieve page:", response.status_code)
