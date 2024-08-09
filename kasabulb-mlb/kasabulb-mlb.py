import asyncio
import requests
from datetime import datetime
from kasa import SmartBulb

# Kasa bulb details
DEVICE_IP = "KASABULB_IP"
TEAM_ID = 110  # ID of the team to monitor (see team list in README.md)
COLOR_HUE = 30  # Hue value for the desired color (0-360)
COLOR_SATURATION = 100  # Saturation value for the desired color (0-100)
COLOR_BRIGHTNESS = 40  # Brightness value for the desired color (0-100)

TEAM_IDS = {
    108: "Los Angeles Angels",
    109: "Arizona Diamondbacks",
    110: "Baltimore Orioles",
    111: "Boston Red Sox",
    112: "Chicago Cubs",
    113: "Cincinnati Reds",
    114: "Cleveland Guardians",
    115: "Colorado Rockies",
    116: "Detroit Tigers",
    117: "Houston Astros",
    118: "Kansas City Royals",
    119: "Los Angeles Dodgers",
    120: "Washington Nationals",
    121: "New York Mets",
    133: "Oakland Athletics",
    134: "Pittsburgh Pirates",
    135: "San Diego Padres",
    136: "Seattle Mariners",
    137: "San Francisco Giants",
    138: "St. Louis Cardinals",
    139: "Tampa Bay Rays",
    140: "Texas Rangers",
    141: "Toronto Blue Jays",
    142: "Minnesota Twins",
    143: "Philadelphia Phillies",
    144: "Atlanta Braves",
    145: "Chicago White Sox",
    146: "Miami Marlins",
    147: "New York Yankees",
    158: "Milwaukee Brewers"
}

async def set_bulb_color(turn_on):
    bulb = SmartBulb(DEVICE_IP)
    await bulb.update()
    print(f"SmartBulb state: {bulb.is_on}")
    if turn_on:
        if not bulb.is_on:
            print("Turning on the light...")
            await bulb.turn_on()
        print(f"Setting bulb to color: Hue={COLOR_HUE}, Saturation={COLOR_SATURATION}, Brightness={COLOR_BRIGHTNESS}")
        await bulb.set_hsv(COLOR_HUE, COLOR_SATURATION, COLOR_BRIGHTNESS)
    else:
        if bulb.is_on:
            print("Turning off the light...")
            await bulb.turn_off()

def check_team_game():
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}"
    response = requests.get(url)
    data = response.json()

    games = data.get('dates', [])[0].get('games', [])
    for game in games:
        if game['teams']['home']['team']['id'] == TEAM_ID or game['teams']['away']['team']['id'] == TEAM_ID:
            status = game['status']['abstractGameState']
            if status == 'Live' or status == 'In Progress':
                return True
    return False

def main():
    try:
        team_name = TEAM_IDS.get(TEAM_ID, "Unknown Team")
        print(f"Checking {team_name} game status...")
        game_live = check_team_game()
        print(f"Is the game live? {game_live}")
        if game_live:
            print(f"{team_name} game is live. Setting bulb to the configured color...")
            asyncio.run(set_bulb_color(True))
        else:
            print(f"No live {team_name} game.")
            asyncio.run(set_bulb_color(False))
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
