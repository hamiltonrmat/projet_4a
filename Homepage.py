import streamlit as st


st.set_page_config(page_title="AgriBalyse UniLaSalle", initial_sidebar_state='auto', layout="wide")
st.title('Projet 4A - Traitement de données alimentaires')

st.page_link("Homepage.py", label="Homepage", icon="🏠")
st.page_link("pages/1_📚_Introduction.py", label="Introduction", icon="1️⃣")
st.page_link("pages/2_📊_Vision_génerale.py", label="Vision génerale", icon="2️⃣")
st.page_link("pages/3_📈_Score_unique_EF.py", label="Score_unique_EF", icon="3️⃣")
st.page_link("https://agribalyse.ademe.fr/", label="Page offitielle Ademe", icon="🌎")

col1, col2 = st.columns(2)
with col1:
    st.image("https://www.actalia.eu/wp-content/uploads/2020/07/Agribalyse.jpg")
with col2:
   st.image("https://lh7-us.googleusercontent.com/0CTFmliTC1Zl4Om49kH2ss7rt8We7gkkDxXyh1a1bViltFIu3xN8kKrs55A8_ACL2XFLmNdXvzQAom7Ts8LrXHVLabMhRPA0K6_SPJcftwoURd38HQ77nCMU-BkySOCp4dv932tV5MZlHwqfO5nckzcM5g=s2048")
