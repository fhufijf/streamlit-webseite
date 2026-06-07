import streamlit as st

st.set_page_config(
    page_title="TicTacToe",
    layout="centered"
)

st.title("Tictactoe")
st.subheader("Spiel mit deinen Freunden.")

# --- CSS NUR FÜR DAS SPIELFELD (ÜBER EINE KLASSE) ---
st.html(
    """
    <style>
    /* Wir targeten nur den Container mit der Klasse "tictactoe-container" */
    .tictactoe-container [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: center !important;
        width: 100% !important;
    }
    
    .tictactoe-container [data-testid="column"] {
        width: 5rem !important;
        flex: 0 0 5rem !important;
        min-width: 5rem !important;
        margin: 0 0.3rem !important;
    }
    
    @media (max-width: 640px) {
        .tictactoe-container [data-testid="stHorizontalBlock"] {
            flex-direction: row !important;
        }
        .tictactoe-container [data-testid="column"] {
            width: 5rem !important;
            flex: 0 0 5rem !important;
            min-width: 5rem !important;
        }
    }

    /* Macht die Spielfeld-Buttons perfekt quadratisch */
    .tictactoe-container div.stButton > button {
        width: 5rem !important;
        height: 5rem !important;
        font-size: 1.5rem !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    </style>
    """
)

st.divider()

# Session State initialisieren
if 'brett' not in st.session_state:
    st.session_state.brett = [":large_blue_circle:"] * 9 
if 'spieler' not in st.session_state:
    st.session_state.spieler = ":o:"
if 'winspeicher' not in st.session_state:
    st.session_state.winspeicher = ""
if 'buttondisabled' not in st.session_state:
    st.session_state.buttondisabled = False

def win():
    gwp = [
        [0, 4, 8], [6, 4, 2], # Diagonalen
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Zeilen
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Spalten
    ]
    for a in gwp:
        eins = st.session_state.brett[a[0]]
        zwei = st.session_state.brett[a[1]]
        drei = st.session_state.brett[a[2]]
        if eins != ":large_blue_circle:" and eins == zwei and zwei == drei:
            st.session_state.winspeicher = f"{eins} hat gewonnen!!!"
            st.session_state.buttondisabled = True
            return True
    return False

def spielzug(index):
    if st.session_state.brett[index] == ":large_blue_circle:":
        st.session_state.brett[index] = st.session_state.spieler
        if not win():
            if st.session_state.spieler == ":o:":
                st.session_state.spieler = ":x:"
            else:
                st.session_state.spieler = ":o:"
        st.rerun()

# Statusmeldung (Außerhalb des Custom-CSS-Containers, damit sie volle Breite hat)
if st.session_state.winspeicher:
    st.success(st.session_state.winspeicher)
else:
    st.info(f"Spieler {st.session_state.spieler} ist an der Reihe.")

# --- SPIELFELD CONTAINER MIT HTML-KLASSE ---
# st.container(border=True) kriegt hier ein umschließendes div mit unserer Klasse
st.markdown('<div class="tictactoe-container">', unsafe_allow_html=True)
with st.container(border=True):
    # Reihe 1
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(st.session_state.brett[0], key="b0", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(0)
    with c2:
        if st.button(st.session_state.brett[1], key="b1", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(1)
    with c3:
        if st.button(st.session_state.brett[2], key="b2", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(2)

    # Reihe 2
    c4, c5, c6 = st.columns(3)
    with c4:
        if st.button(st.session_state.brett[3], key="b3", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(3)
    with c5:
        if st.button(st.session_state.brett[4], key="b4", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(4)
    with c6:
        if st.button(st.session_state.brett[5], key="b5", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(5)

    # Reihe 3
    c7, c8, c9 = st.columns(3)
    with c7:
        if st.button(st.session_state.brett[6], key="b6", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(6)
    with c8:
        if st.button(st.session_state.brett[7], key="b7", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(7)
    with c9:
        if st.button(st.session_state.brett[8], key="b8", disabled=st.session_state.buttondisabled, use_container_width=True): spielzug(8)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Reset-Button (Außerhalb des Containers, damit er normal groß angezeigt wird)
if st.button(label="Reset", type="primary", key="reset_btn", use_container_width=True):
    st.session_state.brett = [":large_blue_circle:"] * 9
    st.session_state.buttondisabled = False
    st.session_state.spieler = ":o:"
    st.session_state.winspeicher = ""
    st.rerun()


def sda():

    st.set_page_config(
        page_title="TicTacToe",
        layout="wide"
    )

    st.title("Tictactoe")
    st.subheader("Spiel mit deinen Freunden.")

    st.divider()

    with st.echo(code_location="below"):
        #-----------------------------------------------------------------------------
        #wenn brett nicht in st.session_state, wird st.session_state.brett neun blaue kreise
        if 'brett' not in st.session_state:
            st.session_state.brett = [":large_blue_circle:"] * 9 #liste mit neun sachen
        #spieler ist o
        if 'spieler' not in st.session_state:
            st.session_state.spieler = ":o:"
        if 'winspeicher' not in st.session_state:
            st.session_state.winspeicher = ""
        if 'buttondisabled' not in st.session_state:
            st.session_state.buttondisabled = False
        #----------------------------------------------------------------------------- 

        def win():
            gwp = [
                [0, 4, 8], #diag 1
                [6, 4, 2], #diag 2
                [0, 3, 6], #zeile 1
                [1, 4, 7], #zeile 2
                [2, 5, 8], #zeile 3
                [0, 1, 2], #spalte 1
                [3, 4, 5], #spalte 2
                [6, 7, 8], #spalte 3   
            ]
            for a in gwp:
                eins = st.session_state.brett[a[0]]
                zwei = st.session_state.brett[a[1]]
                drei = st.session_state.brett[a[2]]
                if eins != ":large_blue_circle:" and eins == zwei and zwei == drei:
                    if st.session_state.spieler == ":x:" or st.session_state.spieler == ":o:" :
                        st.session_state.spieler == "X" or st.session_state.spieler == "O"
                        st.session_state.winspeicher = f"{st.session_state.spieler} hat gewonnen!!!"
                        if st.session_state.winspeicher != st.session_state.buttondisabled:
                            st.session_state.buttondisabled = True

        #st.session_state.spieler wird zu st.session_state.brett[] mit ein liste
        def spielzug(kwargs):
            if st.session_state.brett[kwargs] == ":large_blue_circle:":
                st.session_state.brett[kwargs] = st.session_state.spieler
                win()
                #wenn spieler o ist wird spieler x
                if st.session_state.spieler == ":o:":
                    st.session_state.spieler = ":x:"
                #wenn spieler etwas anderes ist wird es ein o
                else:
                    st.session_state.spieler = ":o:"
                st.rerun()


        with st.container(border=True):
            if st.session_state.winspeicher:
                st.success(st.session_state.winspeicher)
            else:
                st.info(f"Spieler {st.session_state.spieler} ist am Reihe.")

            # REIHE 1
            row1_col1, row1_col2, row1_col3 = st.columns(3)
            with row1_col1:
                if st.button(st.session_state.brett[0], key=1, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(0)
            with row1_col2:
                if st.button(st.session_state.brett[1], key=2, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(1)
            with row1_col3:
                if st.button(st.session_state.brett[2], key=3, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(2)

            # REIHE 2
            row2_col1, row2_col2, row2_col3 = st.columns(3)
            with row2_col1:
                if st.button(st.session_state.brett[3], key=4, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(3)
            with row2_col2:
                if st.button(st.session_state.brett[4], key=5, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(4)
            with row2_col3:
                if st.button(st.session_state.brett[5], key=6, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(5)

            # REIHE 3
            row3_col1, row3_col2, row3_col3 = st.columns(3)
            with row3_col1:
                if st.button(st.session_state.brett[6], key=7, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(6)
            with row3_col2:
                if st.button(st.session_state.brett[7], key=8, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(7)
            with row3_col3:
                if st.button(st.session_state.brett[8], key=9, disabled=st.session_state.buttondisabled, use_container_width=True):
                    spielzug(8)

            st.divider()

            # Reset Funktion & Button außerhalb der Spalten
            if st.button(label="Reset", type="primary", key=34235, use_container_width=True):
                st.session_state.brett = [":large_blue_circle:"] * 9
                st.session_state.buttondisabled = False
                st.session_state.spieler = ":o:"
                st.session_state.winspeicher = ""
                st.rerun()

            def reset():
                if st.button(label = "Reset", type = "primary", key = 34235):
                    st.session_state.brett = [":large_blue_circle:"] * 9
                    st.session_state.buttondisabled = False
                    st.session_state.spieler = ":o:"
                    st.session_state.winspeicher = ""
                    st.rerun()
            reset()
        st.divider()