import streamlit as st

st.title("Rick Roll")

rick_roll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

st.video(rick_roll, autoplay=True)

url = "https://www.bing.com/images/search?q=Lobster+Thermidor+aux+crevettes+with+a+Mornay+sauce&form=HDRSC3&first=1"

st.link_button("Lobster gewonnen!!! Lobster Thermidor aux crevettes with a Mornay sauce", url)