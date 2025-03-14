import streamlit as st
import requests

# ExchangeRatesAPI (Replace with your own API key)
API_KEY = "your_api_key_here"
BASE_URL = "https://v6.exchangerate-api.com/v6/{}/latest/".format(API_KEY)

def get_exchange_rates(base_currency):
    response = requests.get(BASE_URL + base_currency)
    if response.status_code == 200:
        return response.json()["conversion_rates"]
    else:
        return None

# Streamlit UI
st.title("Currency Converter")
st.write("Convert currencies using real-time exchange rates.")

base_currency = st.selectbox("Select Base Currency", ["USD", "EUR", "GBP", "INR", "CAD", "AUD", "JPY", "CNY"])
target_currency = st.selectbox("Select Target Currency", ["USD", "EUR", "GBP", "INR", "CAD", "AUD", "JPY", "CNY"])
amount = st.number_input("Enter Amount", min_value=0.01, format="%.2f")

if st.button("Convert"):
    exchange_rates = get_exchange_rates(base_currency)
    if exchange_rates and target_currency in exchange_rates:
        converted_amount = amount * exchange_rates[target_currency]
        st.success(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        st.error("Error fetching exchange rates. Try again!")
