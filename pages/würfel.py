import streamlit as st
import random
import time

st.title("Würfel")

würfel_ascii = [
        (
            "+-------+\n"
            "|       |\n"
            "|   o   |\n"
            "|       |\n"
            "+-------+"
        ),
        (
            "+-------+\n"
            "| o     |\n"
            "|       |\n"
            "|     o |\n"
            "+-------+"
        ),
        (
            "+-------+\n"
            "| o     |\n"
            "|   o   |\n"
            "|     o |\n"
            "+-------+"
        ),
        (
            "+-------+\n"
            "| o   o |\n"
            "|       |\n"
            "| o   o |\n"
            "+-------+"
        ),
        (
            "+-------+\n"
            "| o   o |\n"
            "|   o   |\n"
            "| o   o |\n"
            "+-------+"
        ),
        (
            "+-------+\n"
            "| o   o |\n"
            "| o   o |\n"
            "| o   o |\n"
            "+-------+"
        ),
    ]

länge_rolle = st.slider("Wähle aus wie viel mal der Würfel rollen wird", min_value = 1, value = 5, max_value = 100)
cooldown = st.slider("Wie lange der Cooldown ist", min_value = 0.0, value = 1.0, max_value = 2.0)

if st.button("Würfel", icon="🎲", type = "primary", width = "stretch"):
    #ist leeres element, das man wieder verwenden kann
    placeholder = st.empty()
    
    def würfeln():
    #der zähler, zählt jedes mal diesen loop benutzt wird. aber es wird nicht benutzt
        for zähler in range(länge_rolle):
            random_nummer = random.randrange(0,6)
            placeholder.code(würfel_ascii[random_nummer])
            time.sleep(cooldown)

    würfeln()

    url = "https://www.bing.com/images/search?q=Lobster+Thermidor+aux+crevettes+with+a+Mornay+sauce&form=HDRSC3&first=1"

    st.link_button("Lobster gewonnen!!! " \
    "Lobster Thermidor aux crevettes with a Mornay sauce", url)