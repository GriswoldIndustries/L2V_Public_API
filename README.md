# L2V Public API Scripts

Small Python scripts for calling Link2Valves public API endpoints using mutual TLS (mTLS) certificates.

This repository currently includes:
- Device data retrieval (`/public/api/devices`)
- Asset data retrieval (`/public/api/assets`)

## Repository Structure

- `L2V_Data_API.py`: Calls the devices endpoint and writes timestamped JSON output.
- `L2V_Assets_API.py`: Calls the assets endpoint and writes timestamped JSON output.
- `.env.example`: Template for environment variables.

## Requirements

- Python 3.9+
- `requests`
- `python-dotenv`
- Valid Link2Valves CA certificate and client certificate/key pair

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

The scripts load certificate settings from `.env`:

### Device Data Script Variables

```env
DATA_CERT_DIR=path/to/data/certs/
DATA_CA_CERT=ClaValCABundle.crt
DATA_CLIENT_CERT=your_device_cert.link2valves.com.crt
DATA_KEY_FILE=your_device_key.link2valves.com.key
```

### Asset Data Script Variables

```env
ASSETS_CERT_DIR=path/to/assets/certs/
ASSETS_CA_CERT=ClaValCABundle.crt
ASSETS_CLIENT_CERT=your_assets_cert.link2valves.com.crt
ASSETS_KEY_FILE=your_assets_key.link2valves.com.key
```

Current script behavior:

- The scripts read `DATA_*` and `ASSETS_*` variable sets directly.
- Certificate filenames are joined to their corresponding `*_CERT_DIR` path.

## Usage

Run the device data script:

```bash
python L2V_Data_API.py
```

Run the asset data script:

```bash
python L2V_Assets_API.py
```

On success, scripts write formatted JSON files under `responses/`:

- Device script: `responses/data_response_data_YYYYMMDD_HHMMSS.json`
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
