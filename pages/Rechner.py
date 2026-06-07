import streamlit as st   # Streamlit wird importiert, um eine Web-App zu erstellen

st.title("Rechner")
st.subheader("Nichts mehr dazu einfach ein Rechner.")

st.divider()

with st.echo(code_location="below"):
    #-----------------------------------------------------------------------------
    # SPEICHER (Session State)
    # Prüft, ob es bereits einen Eintrag "txt" im Session-Speicher gibt.
    # Wenn nicht, wird er angelegt und als leerer Text gespeichert.
    if 'txt' not in st.session_state:
        st.session_state.txt = ""
    #-----------------------------------------------------------------------------  

    # Button-Typen (Farben in Streamlit)
    p = "primary"
    s = "secondary"
    t = "tertiary"

    #-----------------------------------------------------------------------------
    # FUNKTION ZUM RECHNEN
    def rechnen():
        # try = "versuchen"
        # Wenn die Rechnung funktioniert → Ergebnis anzeigen
        # Wenn nicht → Fehlermeldung anzeigen
        try:
            ergebnis = eval(st.session_state.txt)  # Rechnet den eingegebenen Text aus
            st.session_state.txt = str(ergebnis)   # Ergebnis wird wieder als Text gespeichert
        except:
            st.session_state.txt = "Geht nicht"    # Falls Fehler (z.B. 5++), dann Fehlermeldung
    #-----------------------------------------------------------------------------
    # Innerer Container für die Buttons
    with st.container(border=True, width="stretch"):
        
        # 4 Spalten für die Buttons
        col0, col1, col2, col3 = st.columns(4, width="stretch")

        # ------------------- SPALTE 0 (Operatoren) -------------------
        with col0:
            if st.button(":heavy_plus_sign:", type=p, key="plus", width = "stretch"):
                st.session_state.txt += "+"   # "+" wird angehängt

            if st.button(":heavy_minus_sign:", type=p, key="minus", width = "stretch"):
                st.session_state.txt += "-"   # "-" wird angehängt

            if st.button(":heavy_division_sign:", type=p, key="geteilt", width = "stretch"):
                st.session_state.txt += "/"   # "/" wird angehängt

            if st.button(":heavy_multiplication_x:", type=p, key="mal", width = "stretch"):
                st.session_state.txt += "*"   # "*" wird angehängt

        # ------------------- SPALTE 1 -------------------
        with col1:
            if st.button("0️⃣", width = "stretch"):
                st.session_state.txt += "0"

            if st.button("3️⃣", width = "stretch"):
                st.session_state.txt += "3"

            if st.button("6️⃣", width = "stretch"):
                st.session_state.txt += "6"

            if st.button("⚫", width = "stretch"):
                st.session_state.txt += "."   # Punkt für Kommazahlen

        # ------------------- SPALTE 2 -------------------
        with col2:
            if st.button("1️⃣", width = "stretch"):
                st.session_state.txt += "1"

            if st.button("4️⃣", width = "stretch"):
                st.session_state.txt += "4"

            if st.button("7️⃣", width = "stretch"):
                st.session_state.txt += "7"

            if st.button("9️⃣", width = "stretch"):
                st.session_state.txt += "9"

        # ------------------- SPALTE 3 -------------------
        with col3:
            if st.button("2️⃣", width = "stretch"):
                st.session_state.txt += "2"

            if st.button("5️⃣", width = "stretch"):
                st.session_state.txt += "5"

            if st.button("8️⃣", width = "stretch"):
                st.session_state.txt += "8"

            # Wenn "=" gedrückt wird → rechnen()-Funktion wird ausgeführt
            if st.button("=", width="stretch", type=p):
                rechnen()

        # ------------------- LÖSCHEN BUTTON -------------------
        # Löscht den kompletten Text
        if st.button(":wastebasket:", type=p, key="del", width="stretch"):
            st.session_state.txt = ""

#-------------------------------------------------------------------------------------------
        # AUSGABEFELD
        # Zeigt den aktuellen Text oder das Ergebnis an
        txt = st.text_area(
            label="test",
            width="stretch",
            disabled=True,                # Benutzer kann nicht direkt reinschreiben
            label_visibility="collapsed", # Label wird versteckt
            value=st.session_state.txt    # Inhalt kommt aus dem Speicher
        )
    st.divider()