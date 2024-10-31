import streamlit as st
import requests

 # Change this URL to the one of your API
API_URL = " https://my-api-app-ltqnoxdklq-ew.a.run.app/"

st.title("Real Estate Price Prediction MVP")

st.write("Real Estate Price Predictor")


bedrooms = st.slider('How many bedrooms?', min_value=0, max_value=5, value=1, step=1)
bathrooms = st.slider('How many bathrooms?',  min_value=0, max_value=5, value=1, step=1)
living_area = st.number_input('living area in m2?')
surface_of_the_plot = st.number_input('Surface of the plot in m2?')
postal = st.number_input('Postal code? (from 1000 to 9999)')


url = f"{API_URL}/predict"
params = {
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'living_area': living_area,
    'surface_of_the_plot': surface_of_the_plot,
    'postal': postal,
}

response = requests.get(url, params=params).json()
#response = 350000

st.markdown("""

    ## Estimated price:

""")

st.write(f"The estimated price is {str(response)} .")
