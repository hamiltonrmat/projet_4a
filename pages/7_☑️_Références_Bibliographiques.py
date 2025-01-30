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

st.set_page_config(page_title="Références Bibligraphiques", initial_sidebar_state='auto', layout="wide")
st.title('Projet 4A - Traitement de données alimentaires')
st.title('Références Bibliographiques')

st.write("""
Accès aux données | Documentation AGRIBALYSE®, 2024. [en ligne]. Date de consultation : 04/06/2024. Disponible sur : <https://doc.agribalyse.fr/documentation/utiliser-agribalyse/acces-donnees>
Analyse du Cycle de Vie ACV, In eco-conception.fr [en ligne]. Date de consultation : 04/06/2024. Disponible sur : <https://www.eco-conception.fr/static/analyse-du-cycle-de-vie-acv.html>
Google Colab, [en ligne]. Date de consultation : 04/06/2024. Disponible sur : <https://colab.research.google.com/drive/1r5EBrZhbMDmGd651fpRODIATcYk4KucG?usp=sharing#scrollTo=I5Uvn0ubelFi>
Graphique: Marché de l’alimentation : quels produits génèrent le plus de revenus ? | Statista, [en ligne]. Date de consultation : 04/06/2024. Disponible sur : <https://fr.statista.com/infographie/24237/segments-alimentaires-qui-generent-le-plus-de-revenus-part-du-chiffre-affaires-mondial/>
Infographie: Marché de l’alimentation : quels produits génèrent le plus de revenus ?, 2024. In Statista Daily Data [en ligne]. Date de consultation : 04/06/2024. Disponible sur : <https://fr.statista.com/infographie/24237/segments-alimentaires-qui-generent-le-plus-de-revenus-part-du-chiffre-affaires-mondial>
Jules76810, 2024. Jules76810/projet_4a. Date de consultation : 04/06/2024. Disponible sur : <https://github.com/Jules76810/projet_4a>.
Schwab, P.-N., 2017. Étude de marché : les évolutions du marché de l’alimentation. Conseils en marketingDate de consultation : 04/06/2024. Disponible sur : <https://www.intotheminds.com/blog/etude-de-marche-france-evolutions-marche-de-alimentation/>.
Streamlit, [en ligne]. Date de consultation : 04/06/2024. Disponible sur : <https://projetagribalyse4a.streamlit.app/R%C3%A9f%C3%A9rences_Bibliographiques>
""")



st.divider()
st.write("**Nous vous laissons revenir à la page d'accueil avec le lien ci-dessous.**")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')
