import streamlit as st

st.title("DVD Video")
st.subheader(r"Schau einfach zu ¯\\_(ツ)_/¯")

dvd = "https://www.youtube.com/watch?v=5mGuCdlCcNM&t=1s"

st.video(dvd, autoplay=True)