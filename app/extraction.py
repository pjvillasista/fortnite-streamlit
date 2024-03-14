from fortnite_api import FortniteAPI
import streamlit as st


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
