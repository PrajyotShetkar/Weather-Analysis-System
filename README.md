# Weather Analysis System

## Objective

Develop a Django application that fetches real-time weather data from a public API, processes the data, provides insights, and displays an alert for extreme weather conditions.

## Features

- **Weather Data Fetching**: 
  - Integrates with a public weather API (e.g., WeatherAPI).
  - Fetches real-time weather data for a given city.
  - Retrieves and displays useful weather information.

- **Data Processing**:
  - Parses and stores fetched weather data in a database.
  - Calculates trends such as average temperature over the last 24 hours, humidity trends, etc.

- **Alerts**:
  - Shows an alert if the weather condition is extreme.

## Deployment

The application is deployed on Render and can be tested [here](https://weather-analysis-system-s78b.onrender.com/weather).

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/PrajyotShetkar/Weather-Analysis-System.git
   cd Weather-Analysis-System
