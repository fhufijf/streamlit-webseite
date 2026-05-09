#wörterbuch mit api
#sprache verändern können

import requests
import streamlit as st
import time
import streamlit.components.v1 as components

st.title("🌐 Kostenloses Wörterbuch & Übersetzer")

def translate(text, source, target):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }
    response = requests.get(url, params=params)
    return response.json()["responseData"]["translatedText"]

# Sprachauswahl
source_lang = st.selectbox("Ausgangssprache", ["de", "en", "fr", "es", "it"])
target_lang = st.selectbox("Zielsprache", ["de", "en", "fr", "es", "it"])

# Wort eingeben
wort = st.text_input("Das Wort, das du übersetzen willst:")

if wort:
    with st.spinner("Übersetzen..."):
        translated = translate(wort, source_lang, target_lang)

        st.write(translated)
