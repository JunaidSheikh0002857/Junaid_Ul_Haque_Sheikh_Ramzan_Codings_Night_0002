import streamlit as st

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
        "Length": {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084},
        "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
        "Temperature": {"celsius": lambda x: x, "fahrenheit": lambda x: (x * 9/5) + 32, "kelvin": lambda x: x + 273.15}
    }
    
    if category == "Temperature":
        value_in_celsius = conversion_factors[category][from_unit](value) if callable(conversion_factors[category][from_unit]) else value
        converted_value = conversion_factors[category][to_unit](value_in_celsius) if callable(conversion_factors[category][to_unit]) else value_in_celsius
    else:
        value_in_base = value / conversion_factors[category][from_unit]
        converted_value = value_in_base * conversion_factors[category][to_unit]
    
    return converted_value

st.title("Unit Converter App")

category = st.selectbox("Select a category", ["Length", "Weight", "Temperature"])
units = {
    "Length": ["meters", "kilometers", "miles", "feet"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"]
}

from_unit = st.selectbox("From Unit", units[category])
to_unit = st.selectbox("To Unit", units[category])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
