import streamlit as st


st.set_page_config(page_title="AgriBalyse UniLaSalle", initial_sidebar_state='auto', layout="wide")
st.title('Projet 4A - Traitement de données alimentaires')

st.image("https://www.actalia.eu/wp-content/uploads/2020/07/Agribalyse.jpg")

col1, col2 = st.columns(2)
with col1:
    st.page_link("Homepage.py", label="Homepage", icon="🏠")
    st.page_link("pages/1_📚_Introduction.py", label="Introduction", icon="1️⃣")
    st.page_link("pages/2_📊_Vision_génerale.py", label="Vision génerale", icon="2️⃣")
    st.page_link("pages/3_📈_Score_unique_EF.py", label="Score_unique_EF", icon="3️⃣")
    st.page_link("https://agribalyse.ademe.fr/", label="Page offitielle Ademe", icon="🌎")

with col2:
   st.image("https://lh7-us.googleusercontent.com/4N1kPTj6oyb9SPqfcYLXvUfD7a_i3ZB0phoR497KS1--SqioVUkx7riN3LYApywPh4cu_pnw4K1fTdu4f3J1-pRVG2zNYUmGauu5GG2cBWeFUK0gMhVVVw1Uu0WUKT4GxbPpuolMM0a13QGWmaIshbLEqg=s2048",
           width=0.5)
