import streamlit as st

# Layout: Linke "Sidebar", Hauptbereich, Rechte "Sidebar"
col_left, col_main, col_right = st.columns([1, 2, 1])

# Linke Sidebar (simuliert)
with col_left:
    st.markdown("### Linke Sidebar")
    st.button("Knopf A")
    st.checkbox("Option 1")

# Hauptinhalt
with col_main:
    st.markdown("## Hauptbereich")
    st.write("Hier ist dein Hauptinhalt.")

# Rechte Sidebar (simuliert)
with col_right:
    st.markdown("### Rechte Sidebar")
    st.selectbox("Wähle was:", ["X", "Y", "Z"])
    st.slider("Wert", 0, 10, 5)
