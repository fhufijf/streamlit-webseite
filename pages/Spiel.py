import streamlit as st
from streamlit_extras.let_it_rain import rain
from datetime import datetime

# ==========================================================
# Konfiguration
# ==========================================================

# Spezielles Datum (19. Juni)
wn = "2000-06-19 00:00:00"

# ==========================================================
# Session State initialisieren
# ==========================================================

# Gesammelte Blätter
if "blatt" not in st.session_state:
    st.session_state.blatt = 0

# Anzahl gekaufter Bäume (= Blätter pro Sekunde)
if "upgrade" not in st.session_state:
    st.session_state.upgrade = 0

# Allgemeiner Preis (wird momentan nicht verwendet)
if "preis" not in st.session_state:
    st.session_state.preis = 5

# Preis für das Klick-Upgrade
if "preis_clicker" not in st.session_state:
    st.session_state.preis_clicker = 5

# Preis für einen Baum
if "preis_baum" not in st.session_state:
    st.session_state.preis_baum = 10

# Blätter pro Klick
if "click" not in st.session_state:
    st.session_state.click = 0

# ==========================================================
# Debug-Ausgabe
# ==========================================================

def debug():
    """Zeigt alle wichtigen Werte zum Testen an."""

    col1, col2 = st.columns(2)

    with col1:
        st.write("Blätter:", st.session_state.blatt)
        st.write("BPC (Blätter pro Klick):", st.session_state.click)
        st.write("Bäume:", st.session_state.upgrade)

    with col2:
        st.write("BPS (Blätter pro Sekunde):", st.session_state.upgrade)
        st.write("Preis Klick-Upgrade:", st.session_state.preis_clicker)
        st.write("Preis Baum:", st.session_state.preis_baum)


# ==========================================================
# Upgrade-System
# ==========================================================
def upgrades(preis, name, upgrade_anzahl, variable, operation):
    """
    Kauft ein Upgrade.

    parameter:
    preis            -> Kosten des Upgrades
    name             -> Text des Buttons
    upgrade_anzahl   -> Stärke des Upgrades
    variable         -> "click" oder "baum"
    operation        -> "+" oder "*"
    """

    # Nur kaufen, wenn genügend Blätter vorhanden sind
    if st.session_state.blatt >= preis:

        if st.button(name, key=name):

            # ----------------------------------------------
            # Klick-Upgrade
            # ----------------------------------------------
            if variable == "click":

                if operation == "*":
                    st.session_state.click *= upgrade_anzahl

                if operation == "+":
                    st.session_state.click += upgrade_anzahl

                # Preis bezahlen
                st.session_state.blatt -= preis

                # Preis erhöhen
                if name == "+2 blätter pro Click":
                    st.session_state.preis_clicker *= 1.25

                st.session_state.preis_clicker = round(
                    st.session_state.preis_clicker
                )

            # ----------------------------------------------
            # Baum-Upgrade
            # ----------------------------------------------
            if variable == "baum":

                if operation == "*":
                    st.session_state.upgrade *= upgrade_anzahl

                if operation == "+":
                    st.session_state.upgrade += upgrade_anzahl

                # Preis bezahlen
                st.session_state.blatt -= preis

                # Baum wird teurer
                if name == "🌳":
                    st.session_state.preis_baum *= 1.25

                st.session_state.preis_baum = round(
                    st.session_state.preis_baum
                )

            # Seite neu laden
            st.rerun()

def a(name, grund):
    if st.session_state.blatt >= 1:
        st.write("")


# ==========================================================
# Buttons
# ==========================================================

def knopfe():

    # -----------------------------
    # Blatt sammeln
    # -----------------------------
    if st.button("🍃"):

        # Falls ein Klick-Upgrade vorhanden ist,
        # erhält der Spieler mehrere Blätter.
        if st.session_state.click != 0:
            st.session_state.blatt += st.session_state.click
        else:
            st.session_state.blatt += 1

    # -----------------------------
    # Baum kaufen
    # -----------------------------
    upgrades(st.session_state.preis_baum, "🌳", 1, "baum", "+")

    # -----------------------------
    # Klick-Upgrade kaufen
    # -----------------------------
    upgrades(st.session_state.preis_clicker, "+2 blätter pro Click", 2, "click", "+")

    # -----------------------------
    # Spezialevent am 19. Juni
    # -----------------------------
    heute = datetime.today()
    heute_datum = datetime(2000, heute.month, heute.day)

    if st.session_state.blatt >= 1:
        if str(heute_datum) == wn:

            if st.button("🎄"):
                st.session_state.blatt -= 1
                st.session_state.upgrade += 2


# ==========================================================
# Spielschleife
# ==========================================================

@st.fragment(run_every="1s")
def loop():

    # Werte anzeigen
    debug()

    # Eingaben verarbeiten
    knopfe()

    # Jede Sekunde produziert jeder Baum ein Blatt
    st.session_state.blatt += st.session_state.upgrade

    # Neue Werte anzeigen
    debug()


# Spiel starten
loop()

# ==========================================================
# Animation
# ==========================================================
def hbhh():
    with st.container():
        rain(
            emoji="🍃",
            font_size=54,
            falling_speed=5,
            animation_length="infinite",
        )

#🌲 jede 2 von dieses baum wird den CPC und CPS um 10% besser machen aber es kostet 100 bläter. es stackt und es wird aufgerundet