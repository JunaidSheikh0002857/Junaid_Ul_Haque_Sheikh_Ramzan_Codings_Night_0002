import streamlit as st

# Function for length conversion
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Miles": 0.000621371
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function for weight conversion
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Function for temperature conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Streamlit App
def main():
    st.title("📏 Unit Converter")

    # Choose conversion type
    conversion_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature"])

    # Input value
    value = st.number_input("Enter value to convert:", min_value=0.0, format="%.2f")

    if conversion_type == "Length":
        from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches", "Miles"])
        to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches", "Miles"])
        result = convert_length(value, from_unit, to_unit)

    elif conversion_type == "Weight":
        from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
        to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
        result = convert_weight(value, from_unit, to_unit)

    elif conversion_type == "Temperature":
        from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
        result = convert_temperature(value, from_unit, to_unit)

    # Display result
    if st.button("Convert"):
        st.success(f"Converted Value: {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()
