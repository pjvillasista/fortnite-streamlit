import streamlit as st
from fortnite_api import FortniteAPI
import json
from datetime import datetime
from extraction import get_fortnite_api, fetch_player_data


def display_stats_in_columns(mode_data, mode_name):
    st.subheader(f"{mode_name}")
    cols = st.columns(4)
    stats = ["score", "wins", "kd", "matches", "winRate"]
    labels = ["Score", "Wins", "K/D", "Matches Played", "Win Rate"]

    for col, stat, label in zip(cols, stats, labels):
        value = mode_data.get(stat, "N/A")
        # Format winRate as a percentage, if necessary
        if stat == "winRate" and value != "N/A":
            value = f"{value:.2%}"
        col.metric(label, value)


# UI for API Key and Player Name Input
st.title("Fortnite Player Statistics")

st.markdown(
    """
    To use this tool, you will need an API key from [Fortnite-API](https://dash.fortnite-api.com/).
    Please visit the link, sign up for an account if you haven't already, and obtain your API key to proceed.
    """
)
api_key = st.text_input("Enter your Fortnite API Key:", "")
player_name = st.text_input("Enter Fortnite Player Name:", "")

if st.button("Fetch Data") and api_key and player_name:
    api = get_fortnite_api(api_key)
    player_data = fetch_player_data(api, player_name)

    if player_data and "stats" in player_data:
        st.success(f"Data fetched successfully for {player_name}")

        # Display "Overall" game mode first
        overall_stats = player_data["stats"]["all"]["overall"]
        display_stats_in_columns(overall_stats, "Overall")

        # Then display all other game modes
        for mode in ["Solo", "Duo", "Squad", "LTM"]:
            mode_data = player_data["stats"]["all"].get(mode.lower(), {})
            if mode_data:  # Check if data is available for the mode
                display_stats_in_columns(mode_data, mode)
            else:
                st.warning(f"No data available for {mode} mode.")
    else:
        st.error("Failed to fetch player data or player data is missing.")
