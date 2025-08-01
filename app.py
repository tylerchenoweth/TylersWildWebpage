# app.py
import streamlit as st
import requests
import json

st.title("Tyler's Wild Webpage!")
st.write("Welcome to your first interactive app!")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

number = st.slider("Pick a number", 0, 100)
st.write(f"Your number is: {number}")








def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    # print(json.dumps(response.json(), indent=4))
    chuck_norris_joke = response['value']

    return chuck_norris_joke




# Initialize session_state variables if they don't exist
if "counter" not in st.session_state:
    st.session_state.counter = 0

if "chuck_norris_joke" not in st.session_state:
    st.session_state.chuck_norris_joke = get_chuck_norris_joke()

if "slider_value" not in st.session_state:
    st.session_state.slider_value = 50

# Increment Button
if st.button("Get New Joke"):
    st.session_state.chuck_norris_joke = get_chuck_norris_joke()

st.write(st.session_state.chuck_norris_joke)

# Display values
st.write(f"Slider value: {st.session_state.slider_value}")
st.write(f"Counter: {st.session_state.counter}")
