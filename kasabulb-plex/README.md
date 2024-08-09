# Plex-Kasa Automation

This project automates the control of a TP-Link Kasa smart bulb based on Plex server activity. When media playback starts on Plex, the Kasa bulb turns on. When playback stops, the bulb turns off.

## Requirements

- Python 3.6+
- `plexapi` library
- `python-kasa` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SwaggyMike/kasabulb.git
    cd kasabulb/plex-kasa
    ```

2. **Install the required Python libraries:**

    ```bash
    pip install plexapi python-kasa
    ```

3. **Update the script with your configuration:**

    Edit `plex-kasa.py` and replace the following placeholders:
    - `YOUR_PLEX_SERVER`: Your Plex server URL.
    - `YOUR_PLEX_TOKEN`: Your Plex server token.
    - `IP of Kasa device`: The IP address of your Kasa bulb.

## Configuration

### plex-kasa.service

Create a systemd service file to run the script as a specific user. Save the following content as `/etc/systemd/system/plex-kasa.service`:

```ini
[Unit]
Description=Plex Kasa Light Control
After=network.target

[Service]
User=yourusername
ExecStart=/usr/bin/python3 /path/to/plex-kasa.py
Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
```

Replace `yourusername` with your actual username and `/path/to/plex-kasa.py` with the actual path to your script.

### plex-kasa.py

The main script `plex-kasa.py` checks Plex activity and controls the Kasa bulb. Ensure you have updated it with your Plex server details and the IP address of your Kasa device.

## Enable and Start the Service

1. **Move the service file to the systemd directory:**

    ```bash
    sudo mv plex-kasa.service /etc/systemd/system/
    ```

2. **Reload systemd to recognize the new service:**

    ```bash
    sudo systemctl daemon-reload
    ```

3. **Enable the service to start on boot:**

    ```bash
    sudo systemctl enable plex-kasa.service
    ```

4. **Start the service:**

    ```bash
    sudo systemctl start plex-kasa.service
    ```

5. **Check the status of the service:**

    ```bash
    sudo systemctl status plex-kasa.service
    ```

## Troubleshooting

- Ensure the IP address of the Kasa bulb is correct and the bulb is reachable from the VM.
- Check the logs of the systemd service for errors:

    ```bash
    journalctl -u plex-kasa.service
    ```
