import requests
import streamlit as st
import time

p = "primary"
s = "secondary"
t = "tertiary"


def joke():
    url = "https://official-joke-api.appspot.com/jokes/random/1"
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # wirft Fehler bei 4xx/5xx
        data = response.json()

        element = data[0]
        return element["setup"], element["punchline"]

    except requests.RequestException as e:
        return "Fehler beim Laden des Witzes 😢", str(e)

with st.spinner("Wait for it...", show_time=True):
    with st.container():
        setup, punchline = joke()
        st.info(setup)
        time.sleep(2)
        st.success(punchline)

st.button("restart", type = p)