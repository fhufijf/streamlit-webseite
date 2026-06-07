import streamlit as st

def theme_editor():
    st.sidebar.header("🎨 Theme Editor")

    # Store values in session state so they persist
    defaults = {
        "primary": "#4CAF50",
        "background": "#FFFFFF",
        "secondary_bg": "#F0F2F6",
        "text": "#000000",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    # Color pickers
    st.session_state.primary = st.sidebar.color_picker(
        "Primary color", st.session_state.primary
    )
    st.session_state.background = st.sidebar.color_picker(
        "Background color", st.session_state.background
    )
    st.session_state.secondary_bg = st.sidebar.color_picker(
        "Secondary background", st.session_state.secondary_bg
    )
    st.session_state.text = st.sidebar.color_picker(
        "Text color", st.session_state.text
    )

    # Apply styles
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {st.session_state.background};
            color: {st.session_state.text};
        }}

        section[data-testid="stSidebar"] {{
            background-color: {st.session_state.secondary_bg};
        }}

        button[kind="primary"] {{
            background-color: {st.session_state.primary};
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    return {
        "primary": st.session_state.primary,
        "background": st.session_state.background,
        "secondary_bg": st.session_state.secondary_bg,
        "text": st.session_state.text,
    }

st.set_page_config(layout="wide")

theme = theme_editor()

st.title("Live Theme Preview")
st.write("Your current theme:", theme)
st.button("Primary Button", type = "primary")
st.button("Secondary Button", type = "secondary")
st.sidebar.write("Sidebar preview")