# Team-Bulb Automation

This project automates the control of a TP-Link Kasa smart bulb based on the game schedule of a specified sports team. When a game is live, the Kasa bulb turns on and changes to a user-defined color.

## Requirements

- Python 3.6+
- `requests` library
- `python-kasa` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/team-bulb-automation.git
    cd team-bulb-automation
    ```

2. **Install the required Python libraries:**

    ```bash
    pip install requests python-kasa
    ```

3. **Update the script with your configuration:**

    - `DEVICE_IP`: The IP address of your Kasa bulb.
    - `TEAM_ID`: The ID of the team you want to monitor (see the list below).
    - `COLOR_HUE`: The hue value (0-360) for the desired color.
    - `COLOR_SATURATION`: The saturation value (0-100) for the desired color.
    - `COLOR_BRIGHTNESS`: The brightness value (0-100) for the desired color.

### MLB Team IDs

| Team ID | Team Name                  |
|---------|----------------------------|
| 108     | Los Angeles Angels         |
| 109     | Arizona Diamondbacks       |
| 110     | Baltimore Orioles          |
| 111     | Boston Red Sox             |
| 112     | Chicago Cubs               |
| 113     | Cincinnati Reds            |
| 114     | Cleveland Guardians        |
| 115     | Colorado Rockies           |
| 116     | Detroit Tigers             |
| 117     | Houston Astros             |
| 118     | Kansas City Royals         |
| 119     | Los Angeles Dodgers        |
| 120     | Washington Nationals       |
| 121     | New York Mets              |
| 133     | Oakland Athletics          |
| 134     | Pittsburgh Pirates         |
| 135     | San Diego Padres           |
| 136     | Seattle Mariners           |
| 137     | San Francisco Giants       |
| 138     | St. Louis Cardinals        |
| 139     | Tampa Bay Rays             |
| 140     | Texas Rangers              |
| 141     | Toronto Blue Jays          |
| 142     | Minnesota Twins            |
| 143     | Philadelphia Phillies      |
| 144     | Atlanta Braves             |
| 145     | Chicago White Sox          |
| 146     | Miami Marlins              |
| 147     | New York Yankees           |
| 158     | Milwaukee Brewers          |

### Color Reference (HSV Values)

Here are some common colors and their HSV values to help you configure your bulb:

- **Red**: Hue=0, Saturation=100, Brightness=100
- **Green**: Hue=120, Saturation=100, Brightness=100
- **Blue**: Hue=240, Saturation=100, Brightness=100
- **Yellow**: Hue=60, Saturation=100, Brightness=100
- **Cyan**: Hue=180, Saturation=100, Brightness=100
- **Magenta**: Hue=300, Saturation=100, Brightness=100
- **Orange**: Hue=30, Saturation=100, Brightness=100
- **Purple**: Hue=270, Saturation=100, Brightness=100
- **White**: Hue=0, Saturation=0, Brightness=100

4. **Run the script:**

    ```bash
    python3 team-bulb.py
    ```

## Systemd Service

Create a systemd service to run the script continuously.

### team-bulb.service

```ini
[Unit]
Description=Team Bulb Light Control
After=network.target

[Service]
User=yourusername
ExecStart=/usr/bin/python3 /home/yourusername/repos/team-bulb-automation/team-bulb.py
Restart=always
RestartSec=300  # Restart the script every 5 minutes

[Install]
WantedBy=multi-user.target
```

Replace `yourusername` with your actual username and `/home/yourusername/repos/team-bulb-automation/team-bulb.py` with the actual path to your script.

### Enable and Start the Service

1. **Move the service file to the systemd directory:**

    ```bash
    sudo mv team-bulb.service /etc/systemd/system/
    ```

2. **Reload systemd to recognize the new service:**

    ```bash
    sudo systemctl daemon-reload
    ```

3. **Enable the service to start on boot:**

    ```bash
    sudo systemctl enable team-bulb.service
    ```

4. **Start the service:**

    ```bash
    sudo systemctl start team-bulb.service
    ```

5. **Check the status of the service:**

    ```bash
    sudo systemctl status team-bulb.service
    ```
