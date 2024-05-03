import pandas as pd
import numpy as np
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

st.title('Projettt 4A - Traitement de données alimentaires')

#ajouter une image
st.image('Agribalyse-image1.png')
st.caption('Petite description')

st.header('La base de données AgriBalyse')
st.write("Quelques mots sur la base de données")

expander = st.expander("Cliquez ici pour plus d'informations")
expander.write("rtrtrttrtrtrtrtr")
expander.image("https://static.streamlit.io/examples/dice.jpg")

st.divider() # diviseur

st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule

st.write("This text is between the horizontal rules.")
st.caption('Mini text pour expliquer quelque chose')
st.divider() 
################

st.header("l'ACV")
st.caption('Mini text pour expliquer quelque chose')
st.divider()

### du code qui vient de notre notebook, ne fait pas partie de l'affichage
data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})

## ici oui on l'affiche le dataset avec st
st.header("Les données AgriBalyse brutes")
st.dataframe(data)
st.write(data.shape)
cols_data, lignes_data = st.columns(2)
cols_data.metric("Produits", str(data.shape[0]))
lignes_data.metric("Paramètres", str(data.shape[1]))
st.divider()


st.header('Qualité de la donnée:')
dqr_value = st.select_slider('Qualité de la donné',
    options=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
st.write('Donnés avec DQR plus petit que:', dqr_value)


df = data[data["DQR"]<dqr_value]
st.dataframe(df)
st.write(df.shape)
lignes_df, cols_df= st.columns(2)
lignes_df.metric("Produits", str(df.shape[0]))
cols_df.metric("Paramètres", str(df.shape[1]))
a = np.round(df.shape[0] / data.shape[0],3)*100
st.write("Porcentage de produits gardés (par rapport au total) :", a, " %")
st.divider()

variables = ['Changement climatique',
       "Appauvrissement de la couche d'ozone", "Rayonnements ionisants",
       "Formation photochimique d'ozone", "Particules fines",
       'effets_toxico_non_cancer', 'effets_toxico_cancer',
       'Acidification terrestre et eaux douces', 'Eutrophisation eaux douces',
       'Eutrophisation marine', 'Eutrophisation terrestre',
       "Écotoxicité pour écosystèmes aquatiques d'eau douce",
       'Utilisation du sol', 'Épuisement des ressources eau',
       'Épuisement des ressources énergétiques',
       'Épuisement des ressources minéraux']



st.header('Les variables')
variable_select = st.selectbox('Choisisez une variable', (i for i in variables))

confirm = st.checkbox('Afficher détails')

if confirm:
    st.write(variable_select)
    st.line_chart(df[variable_select])
    min_variable, max_variable, mean_variable = st.columns(3)
    min_variable.metric("Min", df[variable_select].min())
    max_variable.metric("Max", df[variable_select].max())
    mean_variable.metric("Moyenne", df[variable_select].mean())

st.header('Le score unique EF')


st.line_chart(df['Score unique EF'])
min_EF, max_EF, mean_EF = st.columns(3)
min_EF.metric("Min", df['Score unique EF'].min())
max_EF.metric("Max", df['Score unique EF'].max())
mean_EF.metric("Moyenne", df['Score unique EF'].mean())

fig = px.scatter_ternary(df, a='Changement climatique', b="Particules fines", c='effets_toxico_cancer')
st.plotly_chart(fig,theme="streamlit", use_container_width=True)
