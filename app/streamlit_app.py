import streamlit as st
from fortnite_api import FortniteAPI
from extraction import get_fortnite_api, fetch_player_data


def display_mode_stats(mode_data, mode_name, stats_keys):
    st.subheader(f"{mode_name} Stats")
    cols = st.columns(
        max(6, len(stats_keys))
    )  # Ensure at least 4 columns for aesthetics

    for col, stat_key in zip(cols, stats_keys):
        # Handle the display of each stat key correctly
        value = mode_data.get(stat_key, "N/A")
        if stat_key == "winRate" and value != "N/A":
            # Format win rate correctly according to its representation as a direct percentage
            # Updated to format with 1 decimal place
            value = f"{value:.1f}%"
        elif stat_key == "kd" and value != "N/A":  # Ensure there's a value
            # Format K/D ratio with two decimal places
            value = f"{value:.2f}"

        # Adjusting stat key titles for a more readable format
        formatted_key = (
            stat_key.capitalize().replace("Kd", "K/D").replace("Top", "Top ")
        )
        col.metric(formatted_key, value)


st.title("Fortnite Player Statistics")

st.markdown(
    """
    To use this tool, you will need an API key from [Fortnite-API](https://dash.fortnite-api.com/).
    Please visit the link, sign up for an account if you haven't already, and obtain your API key to proceed.
"""
)

api_key = st.text_input("Enter your Fortnite API Key:", type="password")
player_name = st.text_input("Enter Fortnite Player Name:", "")

if st.button("Fetch Data") and api_key and player_name:
    api = get_fortnite_api(api_key)
    player_data = fetch_player_data(api, player_name)

    if player_data and "stats" in player_data:
        st.success(f"Data fetched successfully for {player_name}")

        # Overview stats at the top
        overall_stats = player_data["stats"]["all"]["overall"]

        overview_keys = ["winRate", "wins", "kd", "kills"]
        display_mode_stats(overall_stats, "Overview", overview_keys)

        st.markdown("---")  # Visual separator

        game_mode_stats = {
            "Solo": ["wins", "winRate", "kills", "kd", "top10", "top25"],
            "Duo": ["wins", "winRate", "kills", "kd", "top5", "top12"],
            "Trios": ["wins", "winRate", "kills", "kd", "top3", "top6"],
            "Squad": ["wins", "winRate", "kills", "kd", "top3", "top6"],
            "LTM": ["wins", "winRate", "kills", "kd", "top10", "top25"],
        }

        for mode, stats_keys in game_mode_stats.items():
            mode_data = player_data["stats"]["all"].get(mode.lower(), {})
            if mode_data:  # If data available for the mode
                display_mode_stats(mode_data, mode, stats_keys)
            else:
                st.warning(f"No data available for {mode} mode.")
    else:
        st.error("Failed to fetch player data or player data is missing.")
