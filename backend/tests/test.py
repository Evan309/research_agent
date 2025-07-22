import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("CORE_API_KEY")
url = "https://api.core.ac.uk/v3/search/works"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "q": "transformers in healthcare",
    "limit": 5
}

response = requests.post(url, headers=headers, json=payload)

print("Status:", response.status_code)
print("Data:", response.json())