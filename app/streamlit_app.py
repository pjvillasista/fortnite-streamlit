import streamlit as st
from fortnite_api import FortniteAPI
from extraction import get_fortnite_api, fetch_player_data
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("API_KEY")


def get_fortnite_api():
    return FortniteAPI(api_key=api_key)


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


player_data = {}

# Page configuration
st.set_page_config(
    page_title="Fortnite Statistics Tracker",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
with st.sidebar:
    st.title("🎮 Fortnite Stats Tracker")
    player_name = st.text_input("Enter Fortnite Player Name:", key="player_name")

    if st.button("Fetch Data"):
        # Use session state to store API response
        api = get_fortnite_api()
        st.session_state.player_data = fetch_player_data(
            api, st.session_state.player_name
        )

# Use session state to check if player_data exists
if "player_data" in st.session_state and st.session_state.player_data:
    player_data = st.session_state.player_data
    if "stats" in player_data:
        st.success(f"Data fetched successfully for {st.session_state.player_name}")

        # Platform filter
        platform_options = {
            "All": "all",
            "PC": "keyboardMouse",
            "Console": "gamepad",
            "Touch": "touch",
        }
        selected_platform = st.selectbox(
            "Select Platform:", list(platform_options.keys()), key="platform_filter"
        )

        platform_data = player_data["stats"][platform_options[selected_platform]]

        if platform_data:
            # Display overview stats for the selected platform
            if "overall" in platform_data:
                st.markdown("### Overview Stats")
                overall_stats = platform_data["overall"]
                overview_keys = ["winRate", "wins", "kd", "kills"]
                display_mode_stats(overall_stats, "Overview", overview_keys)

            st.markdown("---")  # Visual separator

            # Display game mode-specific stats for the selected platform
            game_mode_stats = {
                "Solo": ["wins", "winRate", "kills", "kd", "top10", "top25"],
                "Duo": ["wins", "winRate", "kills", "kd", "top5", "top12"],
                "Trios": ["wins", "winRate", "kills", "kd", "top3", "top6"],
                "Squad": ["wins", "winRate", "kills", "kd", "top3", "top6"],
                "LTM": ["wins", "winRate", "kills", "kd", "top10", "top25"],
            }

            for mode, stats_keys in game_mode_stats.items():
                mode_data = platform_data.get(mode.lower(), {})
                if mode_data:  # If data is available for the mode
                    display_mode_stats(mode_data, mode, stats_keys)
                else:
                    st.warning(
                        f"No data available for {mode} mode on {selected_platform}."
                    )

        else:
            st.error(f"No data available for {selected_platform} platform.")
    else:
        st.error("Failed to fetch player data or player data is missing.")
else:
    st.info("Please enter a player name and click 'Fetch Data'.")
