import streamlit as st
from streamlit_extras.let_it_rain import rain
from datetime import datetime
import json
from random import random

st.set_page_config(
    page_title="Blatt Spiel",
    page_icon="🍃",
    layout="wide",
)

# Titel der Webseite
st.title("fhufijf's Blatt Spiel")

# ==========================================================
# Konfiguration
# ==========================================================

# Vergleichsdatum für das Weihnachts-Event (25. Dezember)
#wn = "2000-12-25 00:00:00"
wn = "2000-07-04 00:00:00"
# ==========================================================
# Session State initialisieren
# ==========================================================

# Anzahl gesammelter Blätter
if "blatt" not in st.session_state:
    st.session_state.blatt = 0

# Anzahl gekaufter Bäume
# Jeder Baum produziert 1 Blatt pro Sekunde
if "BPS" not in st.session_state:
    st.session_state.BPS = 0

# Startpreis des Klick-Upgrades
if "preis_klicker" not in st.session_state:
    st.session_state.preis_klicker = 5

# Startpreis eines Baumes
if "preis_baum" not in st.session_state:
    st.session_state.preis_baum = 10

# Blätter pro Klick
# Anfangs 0, dadurch gibt der Button standardmäßig 1 Blatt
if "klick" not in st.session_state:
    st.session_state.klick = 1

# Anzahl freigeschalteter Achievements
if "achievements_zähler" not in st.session_state:
    st.session_state.achievements_zähler = 0

# Speichert, welche Achievements bereits freigeschaltet wurden
if "achievement_toggle" not in st.session_state:
    st.session_state.achievement_toggle = [False] * 7

if "prestige_toggle" not in st.session_state:
    st.session_state.prestige_toggle = [False]

if "kritischer_klick" not in st.session_state:
    st.session_state.kritischer_klick = 0

if "kritischer_klick_preis" not in st.session_state:
    st.session_state.kritischer_klick_preis = 10

if "krit" not in st.session_state:
    st.session_state.krit = 0

if "prestige" not in st.session_state:
    st.session_state.prestige = 0

if "prestige_preis" not in st.session_state:
    st.session_state.prestige_preis = 1000



# ==========================================================
# Benutzeroberfläche
# ==========================================================

def ui():

    a, b, c = st.columns(3)

    with a:
        st.metric("Blätter:", st.session_state.blatt, st.session_state.BPS, border=True)

        st.metric("Kritischer Klick Preis:", st.session_state.kritischer_klick_preis, round(st.session_state.kritischer_klick_preis * 1.25), border=True)

    with b:
        st.metric("Preis Klick-Upgrade:", st.session_state.preis_klicker, round(st.session_state.preis_klicker * 1.25), border=True)

    with c:
        st.metric("Preis Baum:", st.session_state.preis_baum, round(st.session_state.preis_baum * 1.25), border=True)


def debug():

    a, b, c = st.columns(3)

    with a:
        st.metric("Blätter:", st.session_state.blatt, st.session_state.BPS, border=True)

        st.metric("Kritischer Klick Preis:", st.session_state.kritischer_klick_preis, round(st.session_state.kritischer_klick_preis * 1.25), border=True)

    with b:
        st.metric("Preis Klick-Upgrade:", st.session_state.preis_klicker, round(st.session_state.preis_klicker * 1.25), border=True)

        st.metric("Achievements:", st.session_state.achievements_zähler, "6", border=True)

    with c:
        st.metric("Preis Baum:", st.session_state.preis_baum, round(st.session_state.preis_baum * 1.25), border=True)

        st.metric("Kritischer Klick Prozent:", st.session_state.kritischer_klick, st.session_state.kritischer_klick + 1, border=True)



     




# ==========================================================
# Upgrade-System
# ==========================================================


def upgrades(preis, name, upgrade_anzahl, variable, operation, help, multiplier):
    """
    Kauft ein Upgrade.

    Parameter
    ---------
    preis:
        Kosten des Upgrades

    name:
        Text des Buttons

    upgrade_anzahl:
        Stärke des Upgrades

    variable:
        "klick" oder "baum"

    operation:
        "+" = addieren
        "*" = multiplizieren
    """

    # Nur kaufen, wenn genügend Blätter vorhanden sind
    if st.session_state.blatt >= preis*multiplier:
        if st.button(name, key=name, help=help):
            # -------------------------
            # Klick-Upgrade
            # -------------------------
            if variable == "klick":

                if name == "Kritischer Klick":
                    st.session_state.kritischer_klick += 1

                else:
                    # Upgrade anwenden
                    if operation == "*":
                        st.session_state.klick *= upgrade_anzahl*multiplier

                    if operation == "+":
                        st.session_state.klick += upgrade_anzahl*multiplier

                # Preis bezahlen
                st.session_state.blatt -= preis*multiplier

                # Neues Upgrade wird teurer
                if name == "+2 BPK 🖱":
                    st.session_state.preis_klicker *= 1.25*multiplier

                if name == "Kritischer Klick":
                    st.session_state.kritischer_klick_preis *= 1.25*multiplier


                # Preis runden
                st.session_state.preis_klicker = round(st.session_state.preis_klicker)

                st.session_state.kritischer_klick_preis = round(st.session_state.kritischer_klick_preis)
                
            # -------------------------
            # Baum-Upgrade
            # -------------------------
            if variable == "baum":

                if operation == "*":
                    st.session_state.BPS *= upgrade_anzahl*multiplier

                if operation == "+":
                    st.session_state.BPS += upgrade_anzahl*multiplier

                # Kosten bezahlen
                st.session_state.blatt -= preis*multiplier

                # Baumpreis erhöhen
                if name == "Baum 🌳":
                    st.session_state.preis_baum *= 1.25*multiplier

                st.session_state.preis_baum = round(st.session_state.preis_baum)

            # Seite aktualisieren
            st.rerun()
    else:
        st.error("zu teuer")    

def achievement_helper(nummer):
    st.session_state.achievements_zähler += 1

    # Kleine Meldung anzeigen
    st.toast("+1 Achievement")

    # Achievement dauerhaft freischalten
    st.session_state.achievement_toggle[nummer] = True

# ==========================================================
# Achievement-System
# ==========================================================

def achievement(name, erklärung, icon, nummer, anzahl_blätter):

    if st.session_state.achievement_toggle[nummer] == False:

        # Genügend Blätter gesammelt?

        if st.session_state.prestige == 1:
            achievement_helper(nummer)

        if anzahl_blätter != -1:
            if st.session_state.blatt >= anzahl_blätter:
                achievement_helper(nummer)

    else:

        # Freigeschaltete Achievements anzeigen
        with st.popover(name, icon=icon, key=name):
            st.write(erklärung)

def prestige():
    if st.session_state.blatt >= st.session_state.prestige_preis:
        if st.button("Prestige"):
            if st.session_state.prestige_toggle[0] == False:
                st.session_state.prestige_toggle[0] = True

                st.session_state.prestige_preis *= 10
                
                st.session_state.blatt = 0
                st.session_state.BPS = 1
                st.session_state.preis_klicker = 5
                st.session_state.preis_baum = 10
                st.session_state.kritischer_klick = 0
                st.session_state.kritischer_klick_preis = 10
                st.session_state.krit = 0
                st.session_state.prestige += 1

                if st.session_state.prestige >= 0:

                    st.session_state.preis_klicker *= 0.9
                    st.session_state.preis_klicker = int(round(st.session_state.preis_klicker))

                    st.session_state.preis_baum *= 0.9
                    st.session_state.preis_baum = int(round(st.session_state.preis_baum))

                    st.session_state.kritischer_klick_preis *= 0.9
                    st.session_state.kritischer_klick_preis = int(round(st.session_state.kritischer_klick_preis))

                    st.session_state.BPS *= 2
    else:
        st.error(f"Tipp: du brauchst {st.session_state.prestige_preis} Blätter für prestige")


def achievements():
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        achievement("🌱 Der Anfang", "Dein allererstes Blatt!", "🍃", 0, 1)

        achievement("prestige", "jhvdjhsdhv", "🍃", 6, -1)

    with col2:
        achievement("🌿 Blatt-Sammler", "100 Blätter gesammelt", "🍃", 1, 100)
    with col3:
        achievement("🌳 Wald-Entdecker", "1000 Blätter erreicht", "🍃", 2, 1000)
    with col4:
        achievement("🌲 König des Waldes", "1 Million Blätter!", "🍃", 3, 1000000)
    with col5:
        achievement("🏆 Legende", "1 Milliarde Blätter!", "🍃", 4, 1000000000)
    with col6:
        achievement("👑 Unendlich", "wie...", "🍃", 5, 1000000000000)


# ==========================================================
# Buttons
# ==========================================================

def knopfe():

    options = ["x1", "x10", "x100", "x1000"]
    mult = st.segmented_control("Multiplier:", options, selection_mode="single", width="stretch", default = "x1")

    if mult == "x10":
        mult = 10
    elif mult == "x100":
        mult = 100
    elif mult == "x1000":
        mult = 1000
    else:
        mult = 1

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        if st.button("Blatt 🍃", help="BPK: " + str(st.session_state.klick)):
            

            if st.session_state.klick != 0:
                garantiert = int(st.session_state.kritischer_klick // 100)
                rest = st.session_state.kritischer_klick % 100
                krits = garantiert 
                if random() < rest / 100:
                    krits += 1    
                if krits >= 1:
                    st.toast(f"Krit {krits}")
                krits += 1
                #st.session_state.klick *= krits
            

                st.session_state.blatt += st.session_state.klick * krits
            else:
                st.session_state.blatt += 1

            


    with col3:
        upgrades(st.session_state.preis_baum, "Baum 🌳", 1, "baum", "+", f"x{mult}", mult)

    with col2:
        upgrades(st.session_state.preis_klicker, "+2 BPk 🖱", 2, "klick", "+", f"Blatt Pro klick. x{mult}", mult)

        upgrades(st.session_state.kritischer_klick_preis, "Kritischer Klick", 1, "klick", "+", f"x{mult}", mult)

    with col4:
        heute = datetime.today()

        # Jahr wird ignoriert
        heute_datum = datetime(2000, heute.month, heute.day)

        if st.session_state.blatt >= 1:

            # Nur am 25. Dezember
            if str(heute_datum) == wn:

                if st.button("🎄", help = f"x{mult}"):

                    # Ein Blatt bezahlen
                    st.session_state.blatt -= 1

                    # Zwei zusätzliche Bäume erhalten
                    st.session_state.BPS += 2*mult
        else:
            st.error("zu teuer")

def save_load():
    def spiel_speichern():
        with open("save.json", "w", encoding="utf-8") as f:
            json.dump(dict(st.session_state), f, indent=4)

    def spiel_laden():
        try:
            with open("save.json", "r", encoding="utf-8") as f:
                daten = json.load(f)

            # Only load game state variables, not widget state
            game_state_keys = ['blatt', 'upgrade', 'preis', 'preis_klicker', 'preis_baum', 
                              'klick', 'achievements_zähler', 'achievement_toggle', 
                              'kritischer_klick', 'kritischer_klick_preis']
            
            for key in game_state_keys:
                if key in daten:
                    st.session_state[key] = daten[key]

        except FileNotFoundError:
            st.error("Kein Spielstand gefunden.")


    if st.button("💾 Speichern", type="primary"):
        spiel_speichern()
        st.success("Spiel gespeichert!")


    if st.button("📂 Laden", type="primary"):
        spiel_laden()

# ==========================================================
# Spielschleife
# ==========================================================

# Diese Funktion wird jede Sekunde automatisch ausgeführt
@st.fragment(run_every="1s")
def loop():

    # Spielwerte anzeigen
    ui()

    # Buttons anzeigen
    knopfe()

    # Jeder Baum produziert ein Blatt pro Sekunde
    st.session_state.blatt += st.session_state.BPS

    prestige()

    # Debug-Menü
    with st.expander("Debug", False):
        debug()

    # Achievement-Menü
    with st.expander("Achievements", False):
        achievements()

    save_load()

loop()

# ==========================================================
# Animation
# ==========================================================

# Blätter fallen dauerhaft vom Himmel
def sads():
    rain(
        emoji="🍃",
        font_size=45,
        falling_speed=5,
        animation_length="infinite",
    )

# Cheat-Button für Testzwecke
if st.button("CHEAT"):
    st.session_state.blatt = 999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999*999



#Prestige-System BPS 1%

#nur ein prestige geht