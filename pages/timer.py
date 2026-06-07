import streamlit as st
from datetime import datetime, time, date
from time import sleep

st.title("Timer")
st.subheader("Du kannst von Timer zu Alarm und Alarm zu Timer wechseln.")

def timer_tab():
    with st.echo(code_location="below"):

        if "totale_zeit" not in st.session_state:
            st.session_state.totale_zeit = 5
        if "zeit" not in st.session_state:
            st.session_state.zeit = st.session_state.totale_zeit
        if "running" not in st.session_state:
            st.session_state.running = False
        if "pausierte_zeit" not in st.session_state:
            st.session_state.pausierte_zeit = 0

        st.subheader("Timer")

        sek = st.number_input(
            "Sekunden:",
            value=st.session_state.totale_zeit,
            min_value=0,
        )

        if sek != st.session_state.totale_zeit:
            st.session_state.totale_zeit = sek
            st.session_state.zeit = st.session_state.totale_zeit

        my_bar = st.empty()
        col1, col2 = st.columns(2)

        with col1:
            start = st.button("Start", width="stretch")
            plus_one = st.button("+1 sek", width="stretch")

        with col2:
            stop = st.button("Stop", width="stretch")
            plus_five = st.button("+5 sek", width="stretch")

        if start:
            st.session_state.zeit = st.session_state.totale_zeit
            st.session_state.running = True
            st.session_state.pausierte_zeit = 0

        if plus_one:
            st.session_state.totale_zeit += 1
            st.session_state.zeit += 1
            st.rerun()

        if stop:
            st.session_state.running = False

        if plus_five:
            st.session_state.totale_zeit += 5
            st.session_state.zeit += 5
            st.rerun()

        if st.session_state.running and st.session_state.zeit > 0:
            st.success("Der Timer läuft: " + str(st.session_state.zeit))
        else:
            my_bar.progress(st.session_state.pausierte_zeit, text="")
            st.info("Der Timer läuft nicht")

        my_bar.progress(st.session_state.pausierte_zeit, text="")

        if st.session_state.running and st.session_state.zeit > 0:
            for _ in range(st.session_state.zeit):
                st.session_state.zeit -= 1
                sleep(1)

                if st.session_state.totale_zeit > 0:
                    st.session_state.pausierte_zeit = (
                        st.session_state.totale_zeit - st.session_state.zeit
                    ) / st.session_state.totale_zeit

                my_bar.progress(st.session_state.pausierte_zeit, text="")

            st.rerun()

            if st.session_state.zeit == 0:
                st.balloons()

        st.divider()

def alarm_tab():
    with st.echo(code_location="below"):
        st.subheader("Alarm")

        jetzt = datetime.now()
        mitternacht = jetzt.replace(hour=0, minute=0, second=0, microsecond=0)
        sekunden_heute = (jetzt - mitternacht).total_seconds()

        alarm_time = st.time_input("Set an alarm for", time(8, 45))
        sek = (alarm_time.hour * 3600) + (alarm_time.minute * 60) + alarm_time.second
        sek = round(abs(sek - sekunden_heute))

        st.info(f"Alarm in {sek} Sekunden")

        st.divider()

def countdown_tab():
    with st.echo(code_location="below"):

        st.title("Countdown to a date")

        nielsgt = st.date_input(" ", date(2026, 6, 28))
        heute = datetime.today()
        nielsgtdatum = datetime(nielsgt.year, nielsgt.month, nielsgt.day)
        days = nielsgtdatum - heute

        st.metric("Days to the date:", days.days + 1)

        if days.days == -1:
            st.balloons()

        st.divider()


tab_timer, tab_alarm, tab_countdown = st.tabs(["Timer", "Alarm", "Countdown"])

with tab_timer:
    timer_tab()

with tab_alarm:
    alarm_tab()

with tab_countdown:
    countdown_tab()