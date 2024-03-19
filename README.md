# Fortnite Statistics Tracker

This Streamlit application provides a comprehensive analysis of Fortnite player statistics, leveraging the Fortnite-API to fetch real-time data. It offers an insightful overview of player performance, including win rate, total wins, kills, and K/D ratio across different platforms and game modes.

![image](https://github.com/pjvillasista/fortnite-streamlit/assets/93170137/6a01d14e-d4e1-44a7-b476-51f792edc2b3)

## Key Features

- **Real-Time Data Fetching**: Utilizes the Fortnite-API to access up-to-date player statistics.
- **Dynamic Platform Filtering**: Users can filter statistics by platform (All, PC, Console, Touch) without re-fetching data, thanks to Streamlit's session state management.
- **Comprehensive Stat Overview**: Displays key performance indicators such as Win Rate, Total Wins, K/D Ratio, and Kills at a glance.
- **Detailed Game Mode Analysis**: Breaks down player statistics by game mode (Solo, Duo, Trios, Squad, LTM) for a deeper understanding of performance.
- **Interactive Charts**: Incorporates Plotly charts to visually represent player statistics, enhancing data interpretation and engagement.
- **Efficient Data Handling**: Leverages Streamlit's session state to maintain data across reruns, minimizing API calls and enhancing user experience.

## Installation

Before running the app, ensure you have Python 3.6+ installed. Then, follow these steps:

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/fortnite-stats-tracker.git
cd fortnite-stats-tracker
```



2. **Install Requirements**:

```bash
pip install -r requirements.txt
```

3. **Setup Environment Variables**:

Create a `.env` file in the project root with your Fortnite-API key:

```plaintext
API_KEY=your_fortnite_api_key_here
```

## Running the App

Execute the app with Streamlit by running:

```bash
streamlit run app.py
```

## Configuration

The app is designed with flexibility in mind, allowing for configuration via Streamlit's `set_page_config` method. Adjust the page title, icon, and layout to suit your preferences. Streamlit's session state is utilized to optimize data handling and user experience.

## Contributing

Contributions to the Fortnite Statistics Tracker are welcome! Whether it's feature enhancements, bug fixes, or documentation improvements, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to [Fortnite-API](https://dash.fortnite-api.com/) for providing the API used in this project.
- This project is not affiliated with, maintained, authorized, endorsed, or sponsored by Epic Games or any of its affiliates.

