import streamlit as st
from fortnite_api import FortniteAPI
import json
from datetime import datetime
from extraction import get_fortnite_api, fetch_player_data


# Streamlit UI for API Key and Player Name Input
st.title("Fortnite Player Statistics")

api_key = st.text_input("Enter your Fortnite API Key:", "")
player_name = st.text_input("Enter Fortnite Player Name:", "")

if st.button("Fetch Data"):
    if api_key and player_name:
        api = get_fortnite_api(api_key)
        player_data = fetch_player_data(api, player_name)

        if player_data:
            st.success(f"Data fetched successfully for {player_name}")
            # Display data directly in the app
            st.write("## Player Overview")
            st.json(player_data)  # Displaying JSON data directly.
        else:
            st.error("Failed to fetch player data. Please try again.")
    else:
        st.error("Please enter both an API key and a player name.")
