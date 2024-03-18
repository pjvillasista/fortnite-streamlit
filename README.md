# Fortnite Statistics Tracker

This Streamlit application provides a comprehensive overview of player statistics in Fortnite, including detailed metrics across various game modes such as Solo, Duo, Squad, and LTM. It fetches real-time data using the Fortnite-API, offering insights into player performance, win rates, kills, and much more.

## Features

- **Overview Stats**: Get a quick glance at your overall performance in Fortnite, including your win rate, total wins, K/D ratio, and total kills.
- **Game Mode Breakdown**: Detailed statistics for each game mode, allowing you to understand your performance across Solo, Duo, Squad, and LTM matches.
- **Real-Time Data**: Utilizes the Fortnite-API to fetch the latest player data, ensuring you're always viewing the most current statistics.

## Getting Started

### Prerequisites

- Python 3.6 or later.
- Streamlit
- A Fortnite-API key ([obtain one here](https://dash.fortnite-api.com/))

### Installation

1. Clone the repository:

```bash
git clone https://github.com/pjvillasista/fortnite-stats-tracker.git
cd fortnite-stats-tracker
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the App

To run the app, navigate to the project directory and run:

```bash
streamlit run streamlit_app.py
```

## Configuration

This app uses Streamlit for the web interface and visualization. You can configure Streamlit settings through `~/.streamlit/config.toml` or environment variables. For more details on Streamlit configuration, refer to [Streamlit's documentation](https://docs.streamlit.io/library/advanced-features/configuration).

## Contributing

Contributions are welcome! If you have suggestions for improvements or bug fixes, please open an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Fortnite-API](https://dash.fortnite-api.com/) for providing the API used in this project.
- This project is not affiliated with, maintained, authorized, endorsed, or sponsored by Epic Games or any of its affiliates.
