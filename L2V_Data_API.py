import json, os, requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
cert_dir = os.getenv('DATA_CERT_DIR')
ca_cert_filename = os.getenv('DATA_CA_CERT')
client_cert_filename = os.getenv('DATA_CLIENT_CERT')
key_file_filename = os.getenv('DATA_KEY_FILE')

ca_cert = os.path.join(cert_dir, ca_cert_filename)
client_cert = os.path.join(cert_dir, client_cert_filename)
key_file = os.path.join(cert_dir, key_file_filename)

# URL to send the GET request to
url = 'https://link2valves.com/public/api/devices'

# Output file path (folder and filename where the response will be saved)
# Edit this variable to change the destination
output_file = 'response_data.json'

# Send the GET request with client certificate authentication
response = requests.get(url, cert=(client_cert, key_file), verify=ca_cert)

# Check if the request was successful
if response.status_code == 200:
    # Parse and save the JSON response with pretty formatting
    with open(output_file, 'w') as f:
        json.dump(response.json(), f, indent=2)
    print(f"Response saved to {output_file}")
else:
    print(f"Error: {response.status_code} - {response.text}")
