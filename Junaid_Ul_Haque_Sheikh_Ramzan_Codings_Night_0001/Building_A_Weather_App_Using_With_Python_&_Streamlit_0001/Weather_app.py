import streamlit as st
import requests

# OpenWeatherMap API key (Replace with your own API key)
API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("Weather App")
st.write("Get real-time weather updates!")

# Cities in Pakistan and the United States
pakistan_cities = ["Karachi", "Islamabad", "Lahore", "Larkana", "Peshawar"]
us_cities = ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco"]

# City input
city = st.text_input("Enter City Name", "")

# Buttons for quick city selection
st.write("### Quick Select:")
col1, col2 = st.columns(2)

with col1:
    for city_name in pakistan_cities:
        if st.button(city_name):
            city = city_name

with col2:
    for city_name in us_cities:
        if st.button(city_name):
            city = city_name

# Fetch and display weather
if city:
    weather_data = get_weather(city)
    if weather_data:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_desc = weather_data['weather'][0]['description'].capitalize()

        # Additional calculations
        feels_like = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        pressure = weather_data['main']['pressure']

        st.subheader(f"Weather in {city}")
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Feels Like:** {feels_like}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Pressure:** {pressure} hPa")
        st.write(f"**Wind Speed:** {wind_speed} m/s")
        st.write(f"**Weather:** {weather_desc}")
    else:
        st.error("City not found! Please try again.")
