import streamlit as st
import random 
import string

st.title("Password generator")
st.write("Man kann die Nummer da unten ändern und auch welche Zeichen das Passwort haben kann.")

st.divider()

with st.echo(code_location="below"):
    with st.container():
        anzahl = st.number_input("Anzahl von Zeichen", value = 8, step = 1, min_value = 1)

        passwort_liste = " "


        auswahl = st.multiselect(" ", placeholder = "Wähle etwas", options = [
            "Nummern",
            "Buchstaben",
            "mit Sonderzeichen"
        ])

    st.space("xxlarge")

    if "Nummern" in auswahl:
        passwort_liste += string.digits

    if  "Buchstaben" in auswahl:
        passwort_liste += string.ascii_letters

    if "mit Sonderzeichen" in auswahl:
        passwort_liste += string.punctuation

    passwort = ""

    for a in range(anzahl):
        passwort += random.choice(passwort_liste)
    if passwort != "":
       st.text("Das Passwort: " + passwort)
    st.divider()

