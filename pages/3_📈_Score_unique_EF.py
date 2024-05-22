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

st.set_page_config(page_title="Score unique EF", initial_sidebar_state='auto', layout="wide")
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
min_EF.metric("Min", np.round(df['Score unique EF'].min(), 3))
max_EF.metric("Max", np.round(df['Score unique EF'].max(), 3))
mean_EF.metric("Moyenne", np.round(df['Score unique EF'].mean(), 3))
