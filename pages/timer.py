#countdaum zu einem datum
#todo stopuhr
import streamlit as st
from datetime import datetime, time, date
from time import sleep

# 1. Aktuellen Zeitpunkt bestimmen
jetzt = datetime.now()

# 2. Mitternacht für den heutigen Tag festlegen
#mitternacht = datetime.combine(jetzt.date(), time.min)
mitternacht = jetzt.replace(hour = 0, minute=0, second=0, microsecond=0)

# 3. Differenz berechnen und in Sekunden umwandeln
sekunden_heute = (jetzt - mitternacht).total_seconds()

#Speicher.-----------------------------------------------
if "totalen_zeit" not in st.session_state:
    st.session_state.totale_zeit = 5

if 'zeit' not in st.session_state:
    st.session_state.zeit = st.session_state.totale_zeit

if "running" not in st.session_state:
    st.session_state.running = False

if "pausierte_zeit" not in st.session_state:
    st.session_state.pausierte_zeit = 0

if "title" not in st.session_state:
    st.session_state.title = "Timer"

if "toggle_label" not in st.session_state:
    st.session_state.toggle_label = "zu Alarm wechseln"
#UI.-----------------------------------------------------

def debug():
    st.write("pausierte_zeit", st.session_state.pausierte_zeit)
    st.write("running", st.session_state.running)
    st.write("zeit", st.session_state.zeit)
    st.write("totalen_zeit", st.session_state.totale_zeit)
    st.write("----------------------------------------------------")

st.title(st.session_state.title)


toggle = st.toggle(st.session_state.toggle_label, key = "dtcfzvguhbijn")

if toggle:
    # Sekunden = (Stunden * 3600) + (Minuten * 60) + Sekunden
    t = st.time_input("Set an alarm for", time(8, 45))
    sek = (t.hour * 3600) + (t.minute * 60) + t.second
    sek = round(abs(sek - sekunden_heute))

    a = "Alarm"
    
    if st.session_state.title == "Timer":
        st.session_state.title = "Alarm"
        st.session_state.toggle_label = "zu Timer wechseln"
        st.rerun()
else:
    sek = st.number_input(label = "Sekunden: ", value = st.session_state.totale_zeit, min_value = 0)

    a = "Timer"

    if st.session_state.title == "Alarm":
        st.session_state.title = "Timer"
        st.session_state.toggle_label = "zu Alarm wechseln"
        st.rerun()

if sek != st.session_state.totale_zeit:
    st.session_state.totale_zeit = sek
    st.session_state.zeit = st.session_state.totale_zeit 

placeholder = st.empty()
my_bar = st.empty()

col1, col2 = st.columns(2)

with col1:
    start = st.button("Start", width = "stretch")

    if toggle != True:
        eine_sek = st.button("+1 sek", width = "stretch")

with col2:
    stop = st.button("Stop", width = "stretch")
    if toggle != True:
        fünf_sek = st.button("+5 sek", width = "stretch")
#Logik.----------------------------------------------------
if start:
    st.session_state.zeit = st.session_state.totale_zeit
    st.session_state.running = True
    st.session_state.pausierte_zeit = 0

if toggle != True:
    if eine_sek:
        st.session_state.totale_zeit += 1
        st.session_state.zeit += 1 
        st.rerun()
else:
    st.space()

if stop:
    st.session_state.running = False

if toggle != True:
    if fünf_sek:
        st.session_state.totale_zeit += 5
        st.session_state.zeit += 5
        st.rerun()
else:
    st.space()

if st.session_state.running and st.session_state.zeit > 0:
    st.success("Der "+ a +" läuft: " + str(st.session_state.zeit))
else:
    my_bar.progress(st.session_state.pausierte_zeit, text = "")
    st.info("Der "+ a +" läuft nicht")
#----------------------------------------------------------
my_bar.progress(st.session_state.pausierte_zeit, text = "")
#Timer Logik.----------------------------------------------
if st.session_state.running and st.session_state.zeit > 0:
    for i in range(st.session_state.zeit):
        st.session_state.zeit -= 1
        sleep(1)
        st.session_state.pausierte_zeit = ( st.session_state.totale_zeit -  st.session_state.zeit) / st.session_state.totale_zeit
        my_bar.progress(st.session_state.pausierte_zeit, text = "")
    st.rerun()
    if st.session_state.zeit == 0:
        st.balloons()

#---------------------------------------------------------
st.title("Countdown to a date")

nielsgt = st.date_input(" ", date(2026, 6, 28))
heute = datetime.today()
nielsgtdatum = datetime(nielsgt.year, nielsgt.month, nielsgt.day)
days = nielsgtdatum - heute

st.metric("Days to the date:", days.days + 1)
if days.days == -1:
    st.balloons()