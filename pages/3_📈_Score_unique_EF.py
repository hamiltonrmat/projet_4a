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

data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})
st.header('Qualité de la donnée:')
dqr_value = st.select_slider('Qualité de la donné',
    options=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
st.write('Donnés avec DQR plus petit que:', dqr_value)
df = data[data["DQR"]<dqr_value]

st.header('Le score unique EF')

st.line_chart(df['Score unique EF'])
min_EF, max_EF, mean_EF = st.columns(3)
min_EF.metric("Min", df['Score unique EF'].min())
max_EF.metric("Max", df['Score unique EF'].max())
mean_EF.metric("Moyenne", df['Score unique EF'].mean())

fig = px.scatter_ternary(df, a='Changement climatique', b="Particules fines", c='effets_toxico_cancer')
st.plotly_chart(fig,theme="streamlit", use_container_width=True)