import asyncio
import time
from kasa import SmartBulb
from plexapi.server import PlexServer

# Plex server details
PLEX_URL = 'http://PLEXIP:32400'
PLEX_TOKEN = 'PLEXTOKEN'

# Kasa bulb details
DEVICE_IP = "KASABULB_IP"

BULB_COLOR = (45, 100, 100)  # Between yellow and orange color in HSV
BULB_BRIGHTNESS = 40  # Brightness level (0-100)

async def toggle_light(turn_on, color=None, brightness=None):
    print(f"Connecting to SmartBulb at {DEVICE_IP}...")
    bulb = SmartBulb(DEVICE_IP)
    await bulb.update()
    print(f"SmartBulb state: {bulb.is_on}")
    if turn_on and not bulb.is_on:
        print("Turning on the light...")
        await bulb.turn_on()
        if color:
            print(f"Setting light color to {color}...")
            await bulb.set_hsv(*color)
        if brightness is not None:
            print(f"Setting light brightness to {brightness}...")
            await bulb.set_brightness(brightness)
    elif not turn_on and bulb.is_on:
        print("Turning off the light...")
        await bulb.turn_off()
    await bulb.update()
    print(f"SmartBulb state after action: {bulb.is_on}")

def check_plex_activity():
    print("Connecting to Plex server...")
    plex = PlexServer(PLEX_URL, PLEX_TOKEN)
    print("Connected to Plex server. Checking for active sessions...")
    sessions = plex.sessions()
    print(f"Number of active sessions: {len(sessions)}")
    return len(sessions) > 0

def main():
    light_on = None  # Initial state is unknown
    while True:
        try:
            print("Checking Plex activity...")
            active = check_plex_activity()
            print(f"Plex activity detected: {active}")
            if active:
                print("Active Plex stream detected. Ensuring the light is on...")
                asyncio.run(toggle_light(True, BULB_COLOR, BULB_BRIGHTNESS))
                light_on = True
            else:
                print("No active Plex streams. Ensuring the light is off...")
                asyncio.run(toggle_light(False))
                light_on = False
            print("Sleeping for 30 seconds...")
            time.sleep(30)  # Check every 30 seconds
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(30)  # Wait before retrying

if __name__ == "__main__":
    main()
