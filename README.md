# L2V Public API Scripts

Small Python scripts for calling Link2Valves public API endpoints. Authentication is supported via mutual TLS (mTLS) certificates or API key token.

This repository currently includes:
- Device data retrieval (`/public/api/devices`)
- Asset data retrieval (`/public/api/assets`)

## Repository Structure

- `L2V_Devices_API_Cert.py`: Calls the devices endpoint using mTLS certificate auth and writes timestamped JSON output.
- `L2V_Devices_API_Token.py`: Calls the devices endpoint using API key token auth and writes timestamped JSON output.
- `L2V_Assets_API_Cert.py`: Calls the assets endpoint using mTLS certificate auth and writes timestamped JSON output.
- `L2V_Assets_API_Token.py`: Calls the assets endpoint using API key token auth and writes timestamped JSON output.
- `API Specification - Devices.pdf`: API specification for the devices endpoint.
- `API Specification - Assets.pdf`: API specification for the assets endpoint.
- `.env.example`: Template for environment variables.

## Requirements

- Python 3.9+
- `requests`
- `python-dotenv`
- Valid API key token, or Link2Valves CA certificate and client certificate/key pair

## Set Up a Virtual Environment (venv)

Use a virtual environment to keep this project's packages separate from your global Python install.

In Command Prompt, from the repository root:

```bat
py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
```

Your prompt should show `(.venv)` when the environment is active.

With the virtual environment active, install dependencies:

```bash
python -m pip install -r requirements.txt
```

If you prefer manual installation:

```bash
python -m pip install requests python-dotenv
```

## Environment Setup

Create a `.env` file in the repository root (copy `.env.example` and update values).

## Usage

Refer to the API specification PDFs for detailed endpoint information and request/response schemas:
- `API Specification - Devices.pdf` for the devices endpoint
- `API Specification - Assets.pdf` for the assets endpoint

Run the device data script:

```bash
# Token auth
python L2V_Devices_API_Token.py

# Certificate auth
python L2V_Devices_API_Cert.py
```

Run the asset data script:

```bash
# Token auth
python L2V_Assets_API_Token.py

# Certificate auth
python L2V_Assets_API_Cert.py
```

On success, scripts write formatted JSON files under `responses/`:

- Device script: `responses/devices_response_data_YYYYMMDD_HHMMSS.json`
- Asset script: `responses/assets_response_data_YYYYMMDD_HHMMSS.json`

## Git-Tracked vs Ignored Files

The following are intentionally ignored by `.gitignore` and are not committed:

- `*.crt` (certificate files)
- `*.key` (private key files)
- `.env`
- `responses` (all response output files)

Because of this, local certificate material and API output JSON will exist on your machine but not appear in repository history.

## Troubleshooting

- `Error: 401/403`: Check that your client cert/key pair is valid and authorized for the endpoint.
- SSL errors: Confirm `*_CA_CERT`, `*_CLIENT_CERT`, and `*_KEY_FILE` point to the correct files.
- File not found: Verify `*_CERT_DIR` and filenames match exactly.
- Non-200 response: The scripts print status code and server response body for diagnosis.

## Security Notes

- Never share private key (`.key`) files.
- Never commit your real `.env` file.
- Avoid sharing API responses if they contain sensitive data.
