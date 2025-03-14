import streamlit as st
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Streamlit UI
st.title("Age Calculator")
st.write("Enter your birth date to calculate your age.")

birth_date = st.date_input("Select your birth date")

if st.button("Calculate Age"):
    age = calculate_age(birth_date)
    st.success(f"Your age is {age} years.")
