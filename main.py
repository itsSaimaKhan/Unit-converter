# #Project 01: Unit Convertor
# #Build a Google Unit Convertor Using Python and Streamlit:

# import streamlit as st
# st.markdown(
#     """
#     <style>
#     body {
#        background-color:#1e1e2f;
#        color : white;
#     }
#     .stApp {
#         background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
#         padding: 30px;
#         border-radius: 15px;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
#     }
#     h1 {
#         text-align: center;
#         font-size: 36px;
#         color:white;
#     }
#     .stButton>button{
#         background: liner-gradient(45deg, #92fe9d, #00c9ff);
#         color: black
#         }
#     .result-box{
#         font-size: 20px;
#         font-weight: bold;
#         text-align: center;
#         background: rgba(255, 255, 255, 0.1);
#         padding: 25px;
#         border-radius: 10px;
#         margin-top: 20px;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
#     }
#     .footer{
#         text-align: center;
#         margin-top: 50px;
#         font-size: 14px;
#         color: black;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# #title and description:
# st.markdown("<h1> Unit Convertor using python and Streamlit </h1>", unsafe_allow_html=True)
# st.write("Easily convert between different units of length , weight, and temperature.")

# #sidebar menu:
# conversion_option = st.sidebar.selectbox("Choose Conversion Type", ["length", "weight", "Temprature"])
# value = st.sidebar.number_input("Enter value",  value=0.0, min_value=0.0, step=0.1 )
# col1, col2 = st.columns(2)

# if conversion_type == "Length": 
#     with col1:
#         from_unit = st.selectbox("From", ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
#     with col2: 
#         to_unit = st.selectbox("To",  ["Meters", "Kilograms", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"]) 
# elif conversion_type == "Weight": 
#     with col1:
#         from_unit = st.selectbox("From", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
#     with col2:
#         to_unit = st.selectbox("To", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
# elif conversion_type == "Temprature": 
#     with col1:
#         from_unit = st.selectbox("From", ["Celsis", "Fahrenheit", "Kelvin"])   
#         with col2:
#             to_unit = st.selectbox("To", ["Celsis", "Fahrenheit", "Kelvin"])

# #converted function
# def length_convertor(value, from_unit, to_unit):
#     length_units = {
#           'Meters': 1; 'Kilometers': 0.001, 'Centermeters': 100, 'Milimeters': 1000,
#           'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37

#     }
#     return (value / length_units[from_unit] * length_units[to_unit])

# def weight_convertor(value, from_unit, to_unit):
#     weight_units = {
#          'Kilogram': 1, 'Grams' : 1000, 'Miligrams' : 1000000, 'Pounds' : 2.2046, 'Ounces': 35.27
#     }  
#     return (value / weight_units[from_unit]) * weight_units[to_unit]

# def  tem_convertor(value, from_unit, to_unit):
#      if from-unit == "Celsius":
#         return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
#      elif from_unit == "Fahrenheit":
#         return (value - 32) * 5/9 if to_unit == "Celsius" else (value -32) * 5/9 + 273.15 if to_unit == "kelvin" else value
#      elif from_unit == "Kelvin":
#         return value -273.15 if to_unit == "Celsius" else (value -273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
#     return value

# #button for conversion
# if st.button("Convert"):
#     if conversion_type == "Length":
#         result = length_convertor(value, from_unit, to_unit)
#     elif conversion_type == "Weight":
#          result = weight_convertor(value, from_unit, to_unit)
#     elif conversion_type == "Temprature":
#         result = temp_convertor(value, from_unit, to_unit)

#     st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:4f} {to_unit}</div>", unsafe_allow_html=True)

# st.markdown("<div class='footer'> Created with love by Saima Khan /div>", unsafe_allow_html=True)

import streamlit as st

# Styling with markdown
st.markdown(
    """
    <style>
    body {
       background-color:#1e1e2f;
       color : white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color:white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of Length, Weight, and Temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.sidebar.number_input("Enter value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Dropdowns for unit selections
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1_000_000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value


# Button for conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Created with ❤️ by Saima Khan</div>", unsafe_allow_html=True)
