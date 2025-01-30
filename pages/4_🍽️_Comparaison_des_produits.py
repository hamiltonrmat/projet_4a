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

st.title('Projet 4A - Traitement de données alimentaires')
st.title("Comparaison des couples de produits")

st.write("Nous avons décidé de former des couples de produits pour répondre à notre problématique d'origine :")
st.write("- Est-ce que l'impact environnemental est le même lorsque l'on compare des produits similaires (appartenants au même groupe d'aliment)  ?")
data = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/743dfdb2-73c4-4312-8256-0bb2d9bbdd13')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})
df2 = data[data["DQR"]<3]
df2 = df2.drop(['Code AGB', 'Code CIQUAL', 'LCI Name', 'code saison', 'code avion',
       'Livraison', "Matériau d'emballage", 'Préparation', 'DQR'],axis=1)

groupes = (df2["Groupe d'aliment"].unique())
sous_groupes = (df2["Sous-groupe d'aliment"].unique())
st.header("Articulation des groupes et sous groupes d'aliments dans la base de donnée Agribalyse")
st.caption("Ci-dessous les 10 groupes qui composent la base de donnée.")
st.write(groupes)
st.caption("Ci-dessous les 54 sous-groupes qui composent la base de donnée.")
st.write(sous_groupes)
st.divider()
st.header("Choix des couples")
st.write("Le choix des couples s'est fait de manière manuelle. Nous avons délibéremment choisi des produits du quotidien sur lesquels nous pouvions avoir des doutes sur le produit ayant plus grand impact environnemental.")

st.write ("Vous pouvez retrouvez ci-dessous la liste des couples que nous avons pu choisir.")
produits = []
produit_1 = 'Comté'
produit_2 = 'Yaourt, lait fermenté ou spécialité laitière, nature'
produits.append(produit_1)
produits.append(produit_2)
couple_1 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_1['Couple'] = ['Couple_1', 'Couple_1']
produit_1 = 'Merguez, boeuf et mouton, cuite'
produit_2 = 'Chipolata, cuite'
produits.append(produit_1)
produits.append(produit_2)
couple_2 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_2["Couple"]=["Couple_2","Couple_2"]
produit_1 = 'Cola, sucré'
produit_2 = "Jus d'orange, à base de concentré"
produits.append(produit_1)
produits.append(produit_2)
couple_3 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_3["Couple"]=["Couple_3","Couple_3"]
produit_1 = 'Matière grasse végétale (type margarine) à 80% MG, salé'
produit_2 = "Beurre à 80% MG, salé"
produits.append(produit_1)
produits.append(produit_2)
couple_4 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_4["Couple"]=["Couple_4","Couple_4"]
produit_1 = 'Boeuf, entrecôte, partie maigre, grillée/poêlée'
produit_2 = "Homard, bouilli/cuit à l'eau"
produits.append(produit_1)
produits.append(produit_2)
couple_5 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_5["Couple"]=["Couple_5","Couple_5"]
produit_1 = 'Ketchup'
produit_2 = 'Mayonnaise (70% MG min.)'
produits.append(produit_1)
produits.append(produit_2)
couple_6 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_6["Couple"]=["Couple_6","Couple_6"]
produit_1 = 'Café au lait ou cappuccino, poudre soluble'
produit_2 = 'Thé infusé, non sucré'
produits.append(produit_1)
produits.append(produit_2)
couple_7 = df2[(df2['Nom du Produit en Français'] == produit_1) | (df2['Nom du Produit en Français'] == produit_2)]
couple_7["Couple"]=["Couple_7","Couple_7"]
produits_cibles = pd.concat([couple_1, couple_2, couple_3, couple_4, couple_5,couple_6 ,couple_7])
colonnes = ['Couple'] + [col for col in produits_cibles.columns if col != 'Couple']
produits_cibles = produits_cibles[colonnes]
st.write(produits_cibles)
top_5_var = ['Particules fines', 'Acidification terrestre et eaux douces', 'Changement climatique', 'Eutrophisation terrestre', 'effets_toxico_cancer']
scaler = preprocessing.MinMaxScaler()
d = scaler.fit_transform(df2[top_5_var])
scaled_df2 = pd.DataFrame(d, columns=df2[top_5_var].columns)
scaled_df2.index = df2[top_5_var].index
test_triangle = scaled_df2.loc[produits_cibles.index]



fig = px.line_polar(d, r=test_triangle.iloc[0,:].values, theta=top_5_var, line_close=True)


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[0,:].values,
      theta=top_5_var,
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[1,:].values,
      theta=top_5_var,
      fill='toself',
      name='Product B'
))

st.divider()
st.write("Voici la figure présentant tous les produits de tous les couples selon les 5 variables préconisées.")


fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[0,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[0]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[1,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[1]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[2,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[2]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[3,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[3]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[4,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[4]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[5,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[5]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[6,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[6]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[7,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[7]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[8,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[8]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[9,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[9]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[10,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[10]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[11,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[11]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[12,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[12]
))
fig.add_trace(go.Scatterpolar(
      r=test_triangle.iloc[13,:].values,
      theta=top_5_var,
      fill='toself',
      name=produits_cibles['Nom du Produit en Français'].iloc[13]
))


st.plotly_chart(fig)

st.write("Enfin, nous vous proposons de faire vos propres choix à travers les différents couples pour les comparer entre eux.")

fig = go.Figure()

for i in range(14):  # Assuming you have 14 products
    fig.add_trace(go.Scatterpolar(
        r=test_triangle.iloc[i, :].values,
        theta=top_5_var,
        fill='toself',
        name=produits_cibles['Nom du Produit en Français'].iloc[i],
        visible='legendonly'  # Ensure traces are not selected when the figure is displayed
    ))
st.plotly_chart(fig)

variables = ['Changement climatique',
 "Appauvrissement de la couche d'ozone",
 'Rayonnements ionisants',
 "Formation photochimique d'ozone",
 'Particules fines',
 'effets_toxico_non_cancer',
 'effets_toxico_cancer',
 'Acidification terrestre et eaux douces',
 'Eutrophisation eaux douces',
 'Eutrophisation marine',
 'Eutrophisation terrestre',
 "Écotoxicité pour écosystèmes aquatiques d'eau douce",
 'Utilisation du sol',
 'Épuisement des ressources eau',
 'Épuisement des ressources énergétiques',
 'Épuisement des ressources minéraux']

ds = df2[variables]




st.divider()
st.write("**Nous vous laissons poursuivre avec la page 5 sur l'intégration de cluster avec l'aide d'une IA ou revenir à la page d'accueil avec les liens ci-dessous.**")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")
st.page_link("pages/5_🤖_IA Clustering.py", label="IA Clustering 🤖", icon="5️⃣")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')


