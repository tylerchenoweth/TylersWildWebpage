# app.py
import streamlit as st
import requests
import json
import random
import numpy as np



def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    # print(json.dumps(response.json(), indent=4))
    chuck_norris_joke = response['value']

    return chuck_norris_joke

def add_gap():
    st.write("")
    st.write("")
    st.write("")

def get_random_pokemon():
    randNum = int(np.round(random.random() * 151, decimals=0) + 1)
    url = f"https://pokeapi.co/api/v2/pokemon/{randNum}"
    response = requests.get(url)
    data = response.json()
    context = {
        "name": data['name'].capitalize(),
        "image": data['sprites']['front_default'],
        "order": data['id'],
        "type": data['types'][0]['type']['name'], 
        "weight": data['weight'],
        "gif": data['sprites']['other']['showdown']['front_default']
    }

    return context


# Initialize session_state variables if they don't exist
if "counter" not in st.session_state:
    st.session_state.counter = 0

if "chuck_norris_joke" not in st.session_state:
    st.session_state.chuck_norris_joke = get_chuck_norris_joke()

if "pokemon" not in st.session_state:
    st.session_state.pokemon = get_random_pokemon()




st.title("Tyler's Wild Webpage!")
st.image("tww_logo.png")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")


add_gap()










if st.button("Get New Joke"):
    st.session_state.chuck_norris_joke = get_chuck_norris_joke()

st.write(st.session_state.chuck_norris_joke)


add_gap()


if st.button("Get New Pokemon"):
    st.session_state.pokemon = get_random_pokemon()

# st.write(st.session_state.pokemon)
# st.markdown(f"**{st.session_state.pokemon['name']}**")

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("**NAME:**")
    st.markdown("**ORDER:**")
    st.markdown("**TYPE:**")
    st.markdown("**WEIGHT:**")
    st.image(st.session_state.pokemon["image"])
with col2:
    st.markdown(st.session_state.pokemon["name"])
    st.markdown(st.session_state.pokemon["order"])
    st.markdown(st.session_state.pokemon["type"])
    st.markdown(st.session_state.pokemon["weight"])
    st.image(st.session_state.pokemon["gif"])

