import streamlit as st   # Streamlit wird importiert, um eine Web-App zu erstellen

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

# Breite und Höhe des Rechners (für Layout)
rechner_width = 250
rechner_height = 125

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

# Container = Rahmen um den Rechner (für schönes Layout)
with st.container(border=True, width=rechner_width + 30):
    st.title("Rechner")  # Titel der App

    # Innerer Container für die Buttons
    with st.container(border=True, width=rechner_width + 10):
        
        # 4 Spalten für die Buttons
        col0, col1, col2, col3 = st.columns(4, width=rechner_width)

        # ------------------- SPALTE 0 (Operatoren) -------------------
        with col0:
            if st.button(":heavy_plus_sign:", type=p, key="plus"):
                st.session_state.txt += "+"   # "+" wird angehängt

            if st.button(":heavy_minus_sign:", type=p, key="minus"):
                st.session_state.txt += "-"   # "-" wird angehängt

            if st.button(":heavy_division_sign:", type=p, key="geteilt"):
                st.session_state.txt += "/"   # "/" wird angehängt

            if st.button(":heavy_multiplication_x:", type=p, key="mal"):
                st.session_state.txt += "*"   # "*" wird angehängt

        # ------------------- SPALTE 1 -------------------
        with col1:
            if st.button("0️⃣"):
                st.session_state.txt += "0"

            if st.button("3️⃣"):
                st.session_state.txt += "3"

            if st.button("6️⃣"):
                st.session_state.txt += "6"

            if st.button("⚫"):
                st.session_state.txt += "."   # Punkt für Kommazahlen

        # ------------------- SPALTE 2 -------------------
        with col2:
            if st.button("1️⃣"):
                st.session_state.txt += "1"

            if st.button("4️⃣"):
                st.session_state.txt += "4"

            if st.button("7️⃣"):
                st.session_state.txt += "7"

            if st.button("9️⃣"):
                st.session_state.txt += "9"

        # ------------------- SPALTE 3 -------------------
        with col3:
            if st.button("2️⃣"):
                st.session_state.txt += "2"

            if st.button("5️⃣"):
                st.session_state.txt += "5"

            if st.button("8️⃣"):
                st.session_state.txt += "8"

            # Wenn "=" gedrückt wird → rechnen()-Funktion wird ausgeführt
            if st.button("=", width=47, type=p):
                rechnen()

        # ------------------- LÖSCHEN BUTTON -------------------
        # Löscht den kompletten Text
        if st.button(":wastebasket:", type=p, key="del", width=rechner_width):
            st.session_state.txt = ""

#-------------------------------------------------------------------------------------------
        # AUSGABEFELD
        # Zeigt den aktuellen Text oder das Ergebnis an
        txt = st.text_area(
            label="test",
            height=rechner_height,
            width=rechner_width,
            disabled=True,                # Benutzer kann nicht direkt reinschreiben
            label_visibility="collapsed", # Label wird versteckt
            value=st.session_state.txt    # Inhalt kommt aus dem Speicher
        )