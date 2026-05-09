import streamlit as st

def dasds():

    options = ["North", "East", "South", "West"]
    selection = st.segmented_control(
        "Directions", options, selection_mode="multi"
    )
    st.markdown(f"Your selected options: {selection}.")



    option_map = {
        0: ":material/add:",
        1: ":material/zoom_in:",
        2: ":material/zoom_out:",
        3: ":material/zoom_out_map:",
    }
    selection = st.segmented_control(
        "Tool",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        selection_mode="single",
    )
    st.write(
        "Your selected option: "
        f"{None if selection is None else option_map[selection]}"
    )
dasds()