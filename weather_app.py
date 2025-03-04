import streamlit as st
import requests

# Set up API Key & Base URL
API_KEY = "89843f8e78a2f3f96b7aa7c1910589cc"  # Replace with your OpenWeatherMap API Key
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
st.set_page_config(page_title="Classy Weather App", page_icon="🌤️", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E1E;
            color: white;
            text-align: center;
        }
        .stTextInput, .stButton {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown("<h1 style='text-align: center;'>🌎 Classy Weather App 🌤️</h1>", unsafe_allow_html=True)
st.markdown("---")

# City Input
city = st.text_input("Enter City Name", "Riyadh")

# Button to Fetch Weather
if st.button("Get Weather", help="Click to fetch the latest weather"):
    weather_data = get_weather(city)

    if weather_data:
        # Extract Weather Info
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        weather_condition = weather_data["weather"][0]["description"].title()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        icon = get_weather_icon(weather_condition)

        # Display Weather Data
        st.markdown(f"<h2 style='text-align: center;'>{icon} {city.title()} Weather</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{weather_condition}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'>{temp}°C</h2>", unsafe_allow_html=True)
        st.write(f"**Feels Like:** {feels_like}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/s")

    else:
        st.error("City not found. Please try again.")
