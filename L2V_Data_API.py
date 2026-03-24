import json, os, requests

# Path to the certificate directory
# Adjust this path if your certificates are stored elsewhere
cert_dir = os.path.join(os.path.expanduser('~'), 'GitHub', 'L2V_Public_API', 'City of Data - Series 35')

# Define the paths to the certificate files
# Adjust the file names if they are different
ca_cert = os.path.join(cert_dir, 'ClaValCABundle.crt')
client_cert = os.path.join(cert_dir, 'kdarmstadt_device.City_of_Data_-_Series_35.link2valves.com.crt')
key_file = os.path.join(cert_dir, 'kdarmstadt_device.City_of_Data_-_Series_35.link2valves.com.key')

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
