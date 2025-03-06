import streamlit as st
import os

def load_css(file_name):
    if os.path.exists(file_name):  # CHECK if the file exists
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"⚠ Error: '{file_name}' not found!")

load_css(os.path.join(os.path.dirname(__file__), "styles.css"))

# All Units
units= {
    "Length": {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Nanometer": 1e-9,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34,
    },
    "Mass": {
        "Gram": 1,
        "Kilogram": 1000,
        "Milligram": 0.001,
        "Pound": 453.592,
        "Ounce": 28.3495,
    },
    "Time": {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
    },
    "Temperature": "special",
    "Speed":{
        "Meter per second (m/s)": 1,
        "Kilometer per hour (km/h)": 0.277778,
        "Mile per hour (mph)": 0.44704,
    },
    "Force": {
        "Newton": 1,
        "Dyne": 1e-5,
        "Pound-force": 4.44822
    },
    "Energy": {
        "Joule": 1,
        "Calorie": 4.184,
        "Electronvolt": 1.602e-19
    },
    "Power": {
        "Watt": 1,
        "Horsepower": 745.7
    },
    "Pressure": {
        "Pascal": 1,
        "Bar": 100000,
        "Atmosphere": 101325,
    },
}

st.title("⚖ Unit Converter")

category = st.selectbox("Select a category", list(units.keys()))

if category == "Temperature":
    temp_input = st.number_input("Enter the temperature value:", step=1.00)
    temp_from = st.selectbox("Convert From:", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_to = st.selectbox("Convert To:", ["Celsius", "Fahrenheit", "Kelvin"])

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return value + 273.15 if to_unit == "Kelvin" else (value * 9/5) + 32
        if from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        if from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else value - 273.15 * 9/5 + 32
        
    if st.button("Convert"):
        result = convert_temperature(temp_input, temp_from, temp_to)
        st.success(f"✅ {temp_input} {temp_from} = {result:.2f} {temp_to}")

else:
    value = st.number_input("Enter the value:", min_value=0.0, step=1.00)
    option1 = st.selectbox("Convert From:", list(units[category].keys()))
    option2 = st.selectbox("Convert To:", list(units[category].keys()))

    if st.button("Convert"):
        baseAmount = value * units[category][option1]
        result = baseAmount / units[category][option2]
        st.success(f"✅ {value} {option1} = {result:.2f} {option2}")