import streamlit as st
from fortnite_api import FortniteAPI
import os
import json
from datetime import datetime

# Ensuree you uploaded environment variables using dotenv in Docker setup
API_KEY = os.getenv("API_KEY")

# Initialize the API
api = FortniteAPI(api_key=API_KEY)


def fetch_player_data(player_name):
    try:
        player_stats = api.stats.fetch_by_name(player_name)
        return player_stats.raw_data
    except Exception as e:
        st.error(f"Failed to fetch data for {player_name}: {e}")
        return None


def save_player_data(player_name, data):
    # Format the current date and time for the filename
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_path = f"./raw_data/{player_name}_raw_data_{current_datetime}.json"

    with open(file_path, "w") as f:
        json.dump(data, f)

    return file_path


# Streamlit UI
st.title("Fortnite Player Statistics")

player_name = st.text_input("Enter Fortnite Player Name:", "")

if st.button("Fetch Data"):
    if player_name:
        player_data = fetch_player_data(player_name)
        if player_data:
            file_path = save_player_data(player_name, player_data)
            st.success(f"Data for {player_name} has been saved to {file_path}")

            # Optionally display some data directly in the app
            st.write("## Player Overview")
            st.json(
                player_data
            )  # Simple way to display JSON data. Consider formatting for better readability.
        else:
            st.error("Failed to fetch player data. Please try again.")
    else:
        st.error("Please enter a player name.")
