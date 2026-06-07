import streamlit as st
from streamlit_extras.three_viewer import *

st.title("3D Viewer")
st.subheader("Hier kanst du 3D Objekte anschauen")

st.divider()

with st.echo(code_location="below"):
    # Using a public GLB model from the Khronos glTF sample models
    Ente = (
        "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb"
    )

    model = Ente

    Maus = (
        "https://raw.githubusercontent.com/fhufijf/streamlit-webseite/main/pages/maus.glb"
    )

    if st.button("Ente", type="primary", width = "stretch"):
        model = Ente

    if st.button("Maus", type="primary", width = "stretch"):
        model = Maus

    st.divider()

    three_viewer(model, height=400, key="basic_demo")

    st.divider()