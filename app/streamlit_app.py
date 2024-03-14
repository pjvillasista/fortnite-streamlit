import streamlit as st
from fortnite_api import FortniteAPI
import json
from datetime import datetime


def get_fortnite_api(user_api_key):
    # Initialize the API with the user-provided API key
    return FortniteAPI(api_key=user_api_key)


def fetch_player_data(api, player_name):
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


# Streamlit UI for API Key and Player Name Input
st.title("Fortnite Player Statistics")

api_key = st.text_input("Enter your Fortnite API Key:", "")
player_name = st.text_input("Enter Fortnite Player Name:", "")

if st.button("Fetch Data"):
    if api_key and player_name:
        api = get_fortnite_api(api_key)
        player_data = fetch_player_data(api, player_name)

        if player_data:
            file_path = save_player_data(player_name, player_data)
            st.success(f"Data for {player_name} has been saved to {file_path}")

            # Display some data directly in the app
            st.write("## Player Overview")
            st.json(player_data)  # Displaying JSON data directly.
        else:
            st.error("Failed to fetch player data. Please try again.")
    else:
        st.error("Please enter both an API key and a player name.")
