import requests
import pandas as pd

# Example public API (Fake Online REST API)
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check status code
if response.status_code == 200:
    data = response.json()   # Convert JSON → Python dict/list
    print("Data received from API:\n", data)

    # Convert to DataFrame
    df = pd.DataFrame(data)
    print("\nConverted to DataFrame:\n", df)

    # Save into CSV file
    df.to_csv("api_users_data.csv", index=False)
    print("\nFile saved as api_users_data.csv")

else:
    print("Error:", response.status_code)
