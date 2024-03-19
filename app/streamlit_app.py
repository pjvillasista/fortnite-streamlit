import streamlit as st
import plotly.express as px
import pandas as pd
from fortnite_api import FortniteAPI
from extraction import get_fortnite_api, fetch_player_data
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("API_KEY")


def get_fortnite_api():
    return FortniteAPI(api_key=api_key)


def display_mode_stats(mode_data, mode_name, stats_keys):
    st.subheader(f"{mode_name}")
    cols = st.columns(max(6, len(stats_keys)))

    for col, stat_key in zip(cols, stats_keys):
        value = mode_data.get(stat_key, "N/A")
        if value != "N/A":
            if stat_key == "winRate" and value != "N/A":
                value = f"{value:.1f}%"
            elif stat_key in [
                "wins",
                "kills",
                "top10",
                "top25",
                "top5",
                "top12",
                "top3",
                "top6",
            ]:  # Numeric values
                value = f"{value:,}"  # Adds commas for thousands
            elif stat_key == "kd" and value != "N/A":
                value = f"{value:.2f}"
        else:
            value = "N/A"

        formatted_key = (
            stat_key.capitalize()
            .replace("Kd", "K/D")
            .replace("Top", "Top ")
            .replace("winRate", "Win Rate")
        )
        col.metric(formatted_key, value)


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

    if st.button("Fetch Data") and player_name:
        api = get_fortnite_api()
        st.session_state.player_data = fetch_player_data(api, player_name)
        st.success(f"Data fetched successfully for {player_name}")

# Use session state to check if player_data exists
# Main app
if "player_data" in st.session_state and st.session_state.player_data:
    player_data = st.session_state.player_data
    if "stats" in player_data:
        # Platform filter
        platform_options = {
            "All": "all",
            "PC": "keyboardMouse",
            "Console": "gamepad",
            "Touch": "touch",
        }
        selected_platform = st.radio(
            "Select Platform:",
            list(platform_options.keys()),
            key="platform_filter",
            horizontal=True,
        )
        st.divider()

        platform_data = player_data["stats"][platform_options[selected_platform]]

        if platform_data:
            # Layout for statistics and charts
            stats_col, charts_col = st.columns([3, 1])

            with stats_col:
                if "overall" in platform_data:
                    overall_stats = platform_data["overall"]
                    overview_keys = ["winRate", "wins", "kd", "kills"]
                    display_mode_stats(overall_stats, "Overview", overview_keys)
                st.divider()

                game_mode_stats = {
                    "Solo": ["wins", "winRate", "kills", "kd", "top10", "top25"],
                    "Duo": ["wins", "winRate", "kills", "kd", "top5", "top12"],
                    "Trios": ["wins", "winRate", "kills", "kd", "top3", "top6"],
                    "Squad": ["wins", "winRate", "kills", "kd", "top3", "top6"],
                    "LTM": ["wins", "winRate", "kills", "kd", "top10", "top25"],
                }

                for mode, stats_keys in game_mode_stats.items():
                    mode_data = platform_data.get(mode.lower(), {})
                    if mode_data:
                        display_mode_stats(mode_data, mode, stats_keys)
                        st.divider()
                    else:
                        st.warning(
                            f"⚠️No data available for {mode} mode on {selected_platform}."
                        )

            # Chart visualizations in the right smaller column
            with charts_col:
                st.subheader("Charts")
                if platform_data:
                    # Prepare data for Wins Across Game Modes
                    wins_data = [
                        platform_data.get(mode.lower(), {}).get("wins", 0)
                        for mode in ["Solo", "Duo", "Trios", "Squad", "LTM"]
                    ]
                    wins_df = pd.DataFrame(
                        {
                            "Game Mode": ["Solo", "Duo", "Trios", "Squad", "LTM"],
                            "Wins": wins_data,
                        }
                    ).sort_values(by="Wins", ascending=False)
                    # Prepare data for Total Games Played vs. Total Games Won
                    games_played_data = [
                        platform_data.get(mode.lower(), {}).get("matches", 0)
                        for mode in ["Solo", "Duo", "Trios", "Squad", "LTM"]
                    ]
                    games_df = pd.DataFrame(
                        {
                            "Game Mode": ["Solo", "Duo", "Trios", "Squad", "LTM"],
                            "Total Games Played": games_played_data,
                            "Total Games Won": wins_data,
                        }
                    )

                    games_df = games_df.sort_values(by="Total Games Played")

                    # Plot Total Games Played vs. Total Games Won
                    fig_games = px.bar(
                        games_df,
                        x=["Total Games Played", "Total Games Won"],
                        y="Game Mode",
                        title="Total Games Played vs. Total Games Won",
                        barmode="group",
                        text_auto=True,
                        orientation="h",
                    )
                    fig_games.update_layout(
                        xaxis_title="Games Played", yaxis_title="Game Mode"
                    )
                    fig_games.update_traces(
                        marker_line_width=0.5, marker_line_color="black"
                    )
                    st.plotly_chart(fig_games, use_container_width=True)

                    # Prepare data for Top 10 Placements Distribution
                    top10_data = [
                        platform_data.get(mode.lower(), {}).get(
                            "top10", platform_data.get(mode.lower(), {}).get("top5", 0)
                        )
                        for mode in ["Solo", "Duo", "Trios", "Squad", "LTM"]
                    ]
                    top10_df = pd.DataFrame(
                        {
                            "Game Mode": ["Solo", "Duo", "Trios", "Squad", "LTM"],
                            "Top 10 Placements": top10_data,
                        }
                    )

                    # Plot Top 10 Placements Distribution
                    fig_top10 = px.pie(
                        top10_df,
                        values="Top 10 Placements",
                        names="Game Mode",
                        title="Top 10 Placements Distribution",
                    )
                    st.plotly_chart(fig_top10, use_container_width=True)

                else:
                    st.error(f"No data available for {selected_platform} platform.")
    else:
        st.error("Failed to fetch player data or player data is unavailable.")
else:
    st.info("Please enter a player name and click 'Fetch Data'.")
