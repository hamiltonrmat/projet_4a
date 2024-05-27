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
from sklearn import preprocessing
import plotly.graph_objects as go
from sklearn.cluster import KMeans

st.set_page_config(page_title="Introduction", initial_sidebar_state='auto', layout="wide")
st.title('Introduction')
st.write("La base de données Agribalyse")

#ajouter une image
st.image('Agribalyse-image1.png')
st.caption('Petite description')

st.header('La base de données AgriBalyse')
st.write("Quelques mots sur la base de données")

expander = st.expander("Cliquez ici pour plus d'informations")
expander.write("rtrtrttrtrtrtrtr")
expander.image("https://agribalyse.ademe.fr/static/media/logo.e3e348f6.png")

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


