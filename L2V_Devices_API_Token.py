import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv


# Load environment variables from the repository's .env file.
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# URL to send the GET request to
url = "https://link2valves.com/public/api/devices"

# Read token for Api-Key header authentication.
api_key = os.getenv("DATA_API_KEY")

if not api_key:
    raise SystemExit("Missing DATA_API_KEY in .env")

headers = {"Api-Key": api_key}

# Output file path (folder and filename where the response will be saved)
output_folder = "responses"
os.makedirs(output_folder, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_folder, f"devices_response_data_{timestamp}.json")

try:
    response = requests.get(url, headers=headers, timeout=30)
except requests.RequestException as exc:
    raise SystemExit(f"Request failed: {exc}")

# Check if the request was successful
if response.status_code == 200:
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(response.json(), f, indent=2)
    print(f"Response saved to {output_file}")
else:
    print(f"Error: {response.status_code} - {response.text}")
