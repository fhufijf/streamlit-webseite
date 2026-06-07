import streamlit as st
from streamlit_extras.three_viewer import *


# Using a public GLB model from the Khronos glTF sample models
Ente = (
    "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb"
)

Maus = (
    "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb"
)

model = st.segmented_control("", [Ente, Maus])

three_viewer(model, height=400, key="basic_demo")