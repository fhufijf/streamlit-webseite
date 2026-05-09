import streamlit as st

#Wenn h nicht in session_state, session_state ist gleich null
#session_state ist ein speicher, wenn man ein variable am ende dieser speicher macht wird dieser variable gespeichert
if 'h' not in st.session_state:
    st.session_state.h = 0

#-----------------------------------------------------------------------------
p = "primary"
s = "secondary"
t = "tertiary"
#-----------------------------------------------------------------------------

st.title("Ein Webseite von")
st.header("Niels Linke")

with st.expander("Sachen die ich gemacht habe"):
    if st.button("Apps", type=t, key="1"):
        st.page_link("pages/rechner.py", label="Rechner")
        st.page_link("pages/DVD_video.py", label="DVD video")
        st.page_link("pages/Zahlen_raten_spiel.py", label="Zahlen raten spielt")
        st.page_link("pages/rick_roll.py", label="Not a rick roll")
        st.page_link("pages/jokes.py", label="5 jokes")
        st.page_link("pages/tictactoe.py", label="tictactoe")
        st.page_link("pages/passwort_generator.py", label="Passwort Generator")
        st.page_link("pages/mini_youtube.py", label="Mini Youtube")
        st.page_link("pages/duden.py", label="Duden")
        st.page_link("pages/karte.py", label="Karte")
        st.page_link("pages/würfel.py", label="Würfel")
        st.page_link("pages/crash.py", label="crash")
#       st.page_link("pages/", label="")

with st.expander("Sachen die ich machen will"):
    st.write("Quiz")
    st.write("Timer")
    st.write("pintrest")
    st.write("countdown zu mein geburtstag")
    st.write("geometredash")
    st.write("custem Minecraft launcher, link: " \
    "https://minecraft-launcher-lib.readthedocs.io/_/downloads/en/latest/pdf/")
    st.write("minecraft texturepack")

with st.container():
    st.write("https://docs.streamlit.io/")
