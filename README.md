# Fortnite Statistics Tracker

This Streamlit application provides a comprehensive analysis of Fortnite player statistics, leveraging the Fortnite-API to fetch real-time data. It offers an insightful overview of player performance, including win rate, total wins, kills, and K/D ratio across different platforms and game modes.

![image](https://github.com/pjvillasista/fortnite-streamlit/assets/93170137/6a01d14e-d4e1-44a7-b476-51f792edc2b3)


## Features at a Glance

- **Real-Time Data Integration**: Directly integrates with Fortnite-API, ensuring access to the latest player statistics.
- **Adaptive Platform Filters**: Empowers users to seamlessly filter statistics by platform (All, PC, Console, Touch), leveraging Streamlit's efficient session state management.
- **Insightful Performance Metrics**: Offers a comprehensive dashboard of performance indicators including Win Rate, Total Wins, K/D Ratio, and Kills.
- **Granular Game Mode Insights**: Provides detailed analysis across game modes (Solo, Duo, Trios, Squad, LTM), offering tailored insights into player strategies and performance.
- **Engaging Data Visualizations**: Utilizes Plotly for interactive charts, transforming complex data into intuitive visual stories.
- **Optimized Data Management**: Efficiently handles data with Streamlit's session state, ensuring minimal API requests and a fluid user experience.

## Getting Started

To use the application, you'll need Python 3.6 or later. Follow these steps to set up:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/pjvillasista/fortnite-stats-tracker.git
   cd fortnite-stats-tracker
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Access**:

   Set up your Fortnite-API key in a `.env` file at the project's root:

   ```plaintext
   API_KEY=your_fortnite_api_key_here
   ```

## Launching the App

Run the following command to start the application:

```bash
streamlit run app.py
```

## Customization

The app is built with adaptability in mind, allowing users to configure settings via Streamlit's `set_page_config` method for a personalized experience. It efficiently uses Streamlit's session state for data retention and smooth interactions.

## How to Contribute

We welcome contributions! If you have ideas for new features, improvements, or bug fixes, please fork the repository, commit your updates, and submit a pull request.

## License

This project is available under the MIT License. For more details, see the [LICENSE](LICENSE.md) file.


## Acknowledgments

- Special thanks to [Fortnite-API](https://dash.fortnite-api.com/) for providing the API used in this project.
- This project is not affiliated with, maintained, authorized, endorsed, or sponsored by Epic Games or any of its affiliates.

