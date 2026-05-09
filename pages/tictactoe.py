import streamlit as st 

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


with st.container(border=True, width=225):
    st.title("Tictactoe")
    st.badge(st.session_state.winspeicher, color="green")

    col1, col2, col3 = st.columns(3, width=200)


    with col1:
        if st.button(st.session_state.brett[0], key = 1, disabled = st.session_state.buttondisabled):
            spielzug(0)


        if st.button(st.session_state.brett[1], key = 2, disabled = st.session_state.buttondisabled):
            spielzug(1)


        if st.button(st.session_state.brett[2], key = 3, disabled = st.session_state.buttondisabled):
            spielzug(2)


    with col2:
        if st.button(st.session_state.brett[3], key = 4, disabled = st.session_state.buttondisabled):
            spielzug(3)


        if st.button(st.session_state.brett[4], key = 5, disabled = st.session_state.buttondisabled):
            spielzug(4)


        if st.button(st.session_state.brett[5], key = 6, disabled = st.session_state.buttondisabled):
            spielzug(5)


    with col3:
        if st.button(st.session_state.brett[6], key = 7, disabled = st.session_state.buttondisabled):
            spielzug(6)


        if st.button(st.session_state.brett[7], key = 8, disabled = st.session_state.buttondisabled):
            spielzug(7)


        if st.button(st.session_state.brett[8], key = 9, disabled = st.session_state.buttondisabled):
            spielzug(8)

    def reset():
        if st.button(label = "Reset", type = "primary", key = 34235):
            st.session_state.brett = [":large_blue_circle:"] * 9
            st.session_state.buttondisabled = False
            st.session_state.spieler = ":o:"
            st.session_state.winspeicher = ""
            st.rerun()
    reset()