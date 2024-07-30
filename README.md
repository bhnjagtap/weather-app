# WeatherProject

## Overview

WeatherProject is a web application that provides real-time weather information using data fetched from the OpenWeatherMap API. Developed using Django for the backend, and HTML, CSS, and JavaScript for the frontend, this project allows users to search for weather conditions in any city and view detailed weather information, including temperature, humidity, and weather conditions. The application also displays a background image corresponding to the city.

## Features

- **Real-time Weather Data**: Fetches current weather conditions using the OpenWeatherMap API.
- **City Search**: Allows users to search for weather information by city name.
- **Detailed Weather Information**: Displays temperature, humidity, weather description, and more.
- **Dynamic Background Images**: Shows a city-specific background image based on the weather condition.
- **Responsive Design**: Ensures a user-friendly experience across different devices.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: OpenWeatherMap API
- **Libraries**: Requests (Python library for HTTP requests)

## Installation

### Prerequisites

- Python 3.x
- Django
- Requests library

### Steps to Install

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/weatherproject.git
   cd weatherproject
Create and Activate a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure API Key

Sign up at OpenWeatherMap to get an API key.

Add your API key to weatherproject/settings.py:


Run Migrations

bash
Copy code
python manage.py migrate
Start the Development Server

bash
Copy code
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to see the application in action.

Usage
Enter the name of a city in the search bar and press "Search."
View the current weather information, including temperature, humidity, and weather conditions.
See a city-specific background image corresponding to the weather conditions.
Contributing
If you'd like to contribute to WeatherProject, please fork the repository and submit a pull request. Ensure your code adheres to the existing style and includes appropriate tests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
OpenWeatherMap API for providing weather data.
Django, HTML, CSS, and JavaScript communities for their invaluable resources and support.
