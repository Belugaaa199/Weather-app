import streamlit as st
import requests
import os

# Set up API Key & Base URL
API_KEY = os.getenv("f9e1dcc03d468566266d0c04e3637a68")  # Store API key as an environment variable
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to select an icon based on weather condition
def get_weather_icon(condition):
    condition = condition.lower()
    if "clear" in condition:
        return "☀️"
    elif "cloud" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "thunderstorm" in condition:
        return "⛈️"
    elif "snow" in condition:
        return "❄️"
    elif "mist" in condition or "fog" in condition:
        return "🌫️"
    else:
        return "🌍"

# Streamlit UI
st.set_page_config(page_title="Classy Weather App", page_icon="🌤️", layout="centered")

# App Title
st.markdown("<h1 style='text-align: center; color: #FFA500;'>🌎 Classy Weather App 🌤️</h1>", unsafe_allow_html=True)
st.markdown("---")

# Center the text input
st.markdown("<h3 style='text-align: center;'>Enter City Name</h3>", unsafe_allow_html=True)
city = st.text_input("", "Riyadh", help="Type any city name")

# Button to Fetch Weather
if st.button("Get Weather 🌍", help="Click to fetch the latest weather"):
    weather_data = get_weather(city)

    if weather_data:
        # Extract Weather Info
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        weather_condition = weather_data["weather"][0]["description"].title()  # Title case for display
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        icon = get_weather_icon(weather_condition.lower())  # Convert to lowercase

        # Display Weather Data
        st.markdown(f"<h2 style='text-align: center;'>{icon} {city.title()} Weather</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: #FFA500;'>{weather_condition}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; font-size: 50px;'>{temp}°C</h2>", unsafe_allow_html=True)

        st.write(f"**🌡 Feels Like:** {feels_like}°C")
        st.write(f"**💧 Humidity:** {humidity}%")
        st.write(f"**💨 Wind Speed:** {wind_speed} m/s")

    else:
        st.error("❌ City not found. Please try again.")
