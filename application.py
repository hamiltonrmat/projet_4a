import pandas as pd
import numpy as np
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Projet 4A - Traitement de données alimentaires')

#ajouter une image
st.image('Agribalyse-image1.png')
st.caption('Petite description')

st.header('La base de données AgriBalyse')
st.write("This is some text.")
st.divider() # diviseur

st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule

st.write("This text is between the horizontal rules.")
st.caption('Mini text pour expliquer quelque chose')
st.divider() 
################

st.title("l'ACV")
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
col1, col2 = st.columns(2)
col1.metric("Produits", str(data.shape[0]))
col2.metric("Paramètres", str(data.shape[1]))
st.divider()


st.header('Qualité de la donnée:')
dqr_value = st.select_slider('Qualité de la donné',
    options=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], 1.5)
st.write('Donnés avec DQR plus petit que:', dqr_value)


df = data[data["DQR"]<dqr_value]
st.dataframe(df)
st.write(df.shape)
col1, col2 = st.columns(2)
col1.metric("Produits", str(df.shape[0]))
col2.metric("Paramètres", str(df.shape[1]))
a = np.round(df.shape[0] / data.shape[0],3)*100
st.write("Porcentage de produits gardés (par rapport au total :", a, " %")
st.divider()