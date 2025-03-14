import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Streamlit UI
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and understand your health status.")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.5, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi, category = calculate_bmi(weight, height)
        st.success(f"Your BMI: {bmi:.2f}")
        st.info(f"Category: {category}")
    else:
        st.error("Please enter valid weight and height values.")
