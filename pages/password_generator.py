import streamlit as st
import random 
import string

st.title("Password generator")

with st.container():
    anzahl = st.number_input("Anzahl von Zeichen", value = 8, step = 1, min_value = 1)

    passwort_liste = " "


    auswahl = st.multiselect(" ", placeholder = "Wähle etwas", options = [
        "Nummern",
        "Buchstaben",
        "mit Sonderzeichen"
    ])

st.container(height = 100, border = False)

if "Nummern" in auswahl:
    passwort_liste += string.digits

if  "Buchstaben" in auswahl:
    passwort_liste += string.ascii_letters

if "mit Sonderzeichen" in auswahl:
    passwort_liste += string.punctuation

passwort = ""

for a in range(anzahl):
    passwort += random.choice(passwort_liste)
st.success("Das Passwort: " + passwort)    
