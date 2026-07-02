import streamlit as st

st.set_page_config(
    page_title="Niels Linke",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Eine Webseite von")
    st.title("Niels Linke")

    st.space("large")

    st.subheader("Programmierer.")
    st.subheader("Bald Architekt.")

with col2:
    st.image("https://avatars.githubusercontent.com/u/269984691?s=400&u=26258dc96717b93dd863bb2e14e099ebcbf2a043&v=4", caption="Niels' Github Profil")


st.divider()
st.header("Meine Projekte")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/Rechner.py", label="🧮 Rechner")
    st.page_link("pages/DVD_video.py", label="📀 DVD Video")
    st.page_link("pages/Zahlen_raten_spiel.py", label="🔢 Zahlen raten")
    st.page_link("pages/Rick_Roll.py", label="🎵 Not a Rick Roll")
    st.page_link("pages/Quiz.py", label="❓ Quiz")

with col2:
    st.page_link("pages/Jokes.py", label="😂 5 Jokes")
    st.page_link("pages/Tic_Tac_Toe.py", label="❌⭕ Tic Tac Toe")
    st.page_link("pages/Passwort_Generator.py", label="🔐 Passwort Generator")
    st.page_link("pages/Mini_Youtube.py", label="📺 Mini YouTube")
    st.page_link("pages/Timer.py", label="⏱️ Timer")

with col3:
    st.page_link("pages/Translator.py", label="🌍 Translator")
    st.page_link("pages/Karte.py", label="🗺️ Karte")
    st.page_link("pages/Würfel.py", label="🎲 Würfel")
    st.page_link("pages/Crash.py", label="💥 Crash")

st.divider()

url = "https://github.com/fhufijf/streamlit-webseite"

st.link_button("Fhufijf's Github: ", url)
