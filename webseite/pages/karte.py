import streamlit as st
import pandas as pan
import pydeck
from pathlib import Path

script_path = Path(__file__).resolve()
repo_root = script_path.parents[1]
csv_path = repo_root / "country-capital-lat-long-population.csv"

hauptstädte = pan.read_csv(csv_path)

hauptstädte["size"] = hauptstädte.Population / 10

point_layer = pydeck.Layer(
    "ColumnLayer",
    data=hauptstädte,
    id="capital-cities",
    get_position=["longitude", "latitude"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    radius=50000,
    get_elevation="size"
)
hexagonlayer = pydeck.Layer(
    "HexagonLayer",
    data=hauptstädte,
    get_position=["longitude", "latitude"],
    radius=100,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=False
)

chart = pydeck.Deck(
    initial_view_state = pydeck.ViewState(pitch=50, latitude=20, longitude=0, zoom=1),
    layers = [point_layer, hexagonlayer],
    tooltip={"text": "{Capital City}, {Country}\nPopulation: {Population}"},
)

with st.container(border = True):
    st.text("Die Hauptstädte von Ländern")
    event = st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")
