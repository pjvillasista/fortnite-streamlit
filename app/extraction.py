import requests
from fortnite_api import FortniteAPI
from dotenv import load_dotenv
import os
import json
from datetime import datetime


# Load Environment Files
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize the API
api = FortniteAPI(api_key=API_KEY)


def fetch_player_data():
    player_name = input("Enter Fortnite Player Name: ")

    player_stats = api.stats.fetch_by_name(player_name)
    raw_data = player_stats.raw_data

    # Format the current date and time for the filename
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_path = f"./raw_data/{player_name}_raw_data_{current_datetime}.json"

    with open(file_path, "w") as f:
        json.dump(raw_data, f)
    print(f"Data for {player_name} has been saved to {file_path}")


fetch_player_data()
