import streamlit as st


st.set_page_config(page_title="AgriBalyse UniLaSalle", initial_sidebar_state='auto', layout="wide")
st.title('Projet 4A - Traitement de données alimentaires')

st.write("Bienvenue sur notre application permettant de mieux comprendre notre projet sur le traitement des données alimentaires de la base de données Agribalyse.")

st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")
st.page_link("pages/1_📚_Introduction.py", label="Introduction 📚", icon="1️⃣")
st.page_link("pages/2_📊_Vision_génerale.py", label="Vision génerale 📊", icon="2️⃣")
st.page_link("pages/3_📈_Score_unique_EF.py", label="Score Unique EF 📈", icon="3️⃣")
st.page_link("pages/4_🍽️_Comparaison_des_produits.py", label="Comparaison des produits 🍽️", icon="4️⃣")
st.page_link("pages/5_🤖_IA Clustering.py", label="IA Clustering 🤖", icon="5️⃣")
st.page_link("pages/6_⌛️_Conclusion.py", label="Conclusion ⌛️", icon="6️⃣")
st.page_link("pages/7_☑️_Références_Bibliographiques.py", label="Références Bibliographiques ☑️", icon="7️⃣")

st.write("Pour vous familiariser ou en apprendre plus par vous même, vous pouvez notamment retrouvez la base de données Agribalyse en ligne en cliquant sur le lien de la page officielle de l'ADEME ci-dessous.")
st.page_link("https://agribalyse.ademe.fr/", label="Page officielle Ademe", icon="🌎")

col1, col2 = st.columns(2)
with col1:
    st.image("https://www.actalia.eu/wp-content/uploads/2020/07/Agribalyse.jpg")
with col2:
   st.image("https://lh7-us.googleusercontent.com/0CTFmliTC1Zl4Om49kH2ss7rt8We7gkkDxXyh1a1bViltFIu3xN8kKrs55A8_ACL2XFLmNdXvzQAom7Ts8LrXHVLabMhRPA0K6_SPJcftwoURd38HQ77nCMU-BkySOCp4dv932tV5MZlHwqfO5nckzcM5g=s2048")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')
