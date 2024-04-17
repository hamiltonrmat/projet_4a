import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import streamlit as st

st.title('Projet 4A - AgriBalyse')

st.header('Exemples pour écrire du text')

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider() # diviseur

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule

st.caption('Mini text pour expliquer quelque chose')

st.divider() 
################

st.header('Aficher nos datasets traités (ou bruts)')


### du code qui vient de notre notebook, ne fait pas partie de l'affichage
data = pd.read_csv('Agribalyse_Synthese (2).csv')

## ici oui on l'affiche avec st
st.write("Les données AgriBalyse brutes")
st.dataframe(data)