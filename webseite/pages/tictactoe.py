import streamlit as st 

#-----------------------------------------------------------------------------
if 'txt' not in st.session_state:
    st.session_state.txt = [":large_blue_circle:"] * 9
#-----------------------------------------------------------------------------  
p = "primary"
s = "secondary"
t = "tertiary"

leer = ":large_blue_circle:"
#-----------------------------------------------------------------------------

def leer(kwargs):
    leer = ""
    st.session_state.txt[kwargs] = ":o:"
    st.rerun()

with st.container(border=True, width=225):
    st.title("Tictactoe")

    col1, col2, col3 = st.columns(3, width=200)


    with col1:
        if st.button(st.session_state.txt[0], key = 1):
            leer(0)
            leer = ":o:"

        if st.button(st.session_state.txt[1], key = 2):
            leer(1)
            leer = ":o:"

        if st.button(st.session_state.txt[2], key = 3):
            leer(2)
            leer = ":o:"


    with col2:
        if st.button(st.session_state.txt[3], key = 4):
            leer(3)
            leer = ":o:"

        if st.button(st.session_state.txt[4], key = 5):
            leer(4)
            leer = ":o:"

        if st.button(st.session_state.txt[5], key = 6):
            leer(5)
            leer = ":o:"


    with col3:
        if st.button(st.session_state.txt[6], key = 7):
            leer(6)
            leer = ":o:"

        if st.button(st.session_state.txt[7], key = 8):
            leer(7)
            leer = ":o:"

        if st.button(st.session_state.txt[8], key = 9):
            leer(8)
            leer = ":o:"

    #    :o: :x: