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


st.title("Comparatif")


data = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/743dfdb2-73c4-4312-8256-0bb2d9bbdd13')
df2 = data[data["DQR"]<3]
df2 = df2.drop(['Code AGB', 'Code CIQUAL', 'LCI Name', 'code saison', 'code avion',
       'Livraison', "Matériau d'emballage", 'Préparation', 'DQR'],axis=1)

groupes = list(df2["Groupe d'aliment"].unique())
(groupes, len(groupes))

sous_groupes = list(df2["Sous-groupe d'aliment"].unique())
(sous_groupes, len(sous_groupes))

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

st.dataframe(produits_cibles)

