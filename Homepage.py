import streamlit as st


st.set_page_config(page_title="AgriBalyse UniLaSalle", initial_sidebar_state='auto')
st.title('Projet 4A - Traitement de données alimentaires')

col1, col2 = st.columns(2)

with col1:
    st.page_link("Homepage.py", label="Homepage", icon="🏠")
    st.page_link("pages/page_1.py", label="Introduction", icon="1️⃣")
    st.page_link("pages/Vision_génerale.py", label="Vision génerale", icon="2️⃣")
    st.page_link("pages/Score_unique_EF.py", label="Score_unique_EF", icon="2️⃣")
    st.page_link("https://agribalyse.ademe.fr/", label="Page offitielle Ademe", icon="🌎")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")