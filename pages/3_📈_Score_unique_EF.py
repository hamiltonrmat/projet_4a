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

st.set_page_config(page_title="Score unique EF", initial_sidebar_state='auto', layout="wide")
data = pd.read_csv('Agribalyse_Synthese (2).csv')
cols = list(data.columns)
data = data.rename(columns={cols[18]: "effets_toxico_non_cancer", cols[19]: "effets_toxico_cancer"})
st.title('Projet 4A - Traitement de données alimentaires')
st.header("Le score unique EF")
st.write("Le score unique EF est la valeur préconisée par la Commission Européenne. Le Score Unique EF regroupe et représente les différents indicateurs ayant une influence environnementale. On peut notamment voir la pondération des différents facteurs qui forme ce score sur le tableau ci-dessous.")
st.image("https://doc.agribalyse.fr/~gitbook/image?url=https%3A%2F%2F2407839794-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LpO7Agg1DbhEBNAvmHP%252F-MLmGl1xWNUdFGoOBo9f%252F-MLmGoORnso9M46c0PtM%252Fjrc.png%3Falt%3Dmedia%26token%3D9da03594-5db3-433b-9461-c24e23ee5e1c&width=768&dpr=2&quality=100&sign=4fe1c17ceedc8702a665f9d5c511f618313f5439678e76fc2ef954da1cd9c621")
expander = st.expander("Cliquez ici pour plus d'informations sur les 16 indicateurs.")
expander.write(""" 

Notre base de données est basée sur 16 indicateurs environnementaux qui sont fournis pour chaque produit :  

- **Le changement climatique**, ce dernier indicateur permet d’avoir une vision globale des impacts d’un produits sur son environnement et plus particulièrement sur le changement climatique, reflet de l’incidence de l’homme sur son environnement.
- **Les particules fines** car ces dernières participent au réchauffement de la planète en piégeant les rayons du soleil, mais elles ont aussi de fortes conséquences sur la santé humaine. 
- **L’épuisement des ressources en eau** qui est calculé en fonction de la consommation d’eau nécessaire au produit par rapport à sa rareté dans la région de production. L’épuisement des ressources en eau est responsable du stress hydrique pour les écosystèmes et peut modifier le cycle de l’eau de certaines régions. 
- **L’épuisement des ressources énergétiques** qui correspond à l’utilisation de ressources non renouvelables, grandement responsables des émissions de gaz à effets de serre.  
- **L’usage des terres** : Les terres utilisées pour l’agricultures ne sont plus à leur état naturel et représente des ressources en moins pour les milieux naturels (exemple : forêt).
- **L’épuisement des ressources en minéraux** : Les ressources minérales sont non renouvelables. De plus leur extraction nécessite beaucoup d’énergies et libèrent de grandes quantités de gaz à effets de serre dans l’atmosphère. Par ailleurs leur extraction dégrade également l’environnement par la création de mines et carrières pour les extraire.
- **L’appauvrissement de la couche d’ozone** induit une augmentation de l’exposition des individus aux rayonnements ultraviolets issus du soleil. Ces radiations sont nocives pour la santé et peuvent causer des cancers.
- **L’acidification** peut avoir lieu par exemple dans les océans lorsque du CO2 est dissout dans l’eau, d’autres écosystèmes peuvent également être acidifiés à cause des pluies acides.
- **L’effet des radiations ionisantes sur la santé** est issu de la rpudction d’électricité par la voie du nucléaire. Cette dernière est responsable de la production de déchets radioactifs néfaste pour les écosystèmes et la santé humaine. 
- **La formation photochimique d’ozone** qui a des conséquences sur la santé, est issus de la réaction entre des oxydes d’azote et des composés volatils lorsque ces derniers sont exposés à la lumière du soleil.
- **L’eutrophisation terrestre** déséquilibre voire appauvrit les sols (principalement agricoles) lorsqu’un excès de nutriments est apporté.
- **L’eutrophisation marine** : ce phénomène dû à un excès de nutriments (principalement de l’azote) dans le sol ce qui engendre une prolifération d’algues, asphyxiant le milieu naturel. 
- **L’eutrophisation d’eau douce**  tout comme pour l’eutrophisation marine, cette dernière mène à une asphyxie des milieux naturels par la prolifération d’algues. 
- **L’écotoxicité d’eau douce** cet indicateur n’est pas très bien assimilé, mais il correspond à la contamination de l’environnement.
- **Effet toxicologique sur la santé humaine (substances cancérogènes et non cancérogènes) :**ces deux indicateurs mesurent l’exposition des populations à des contaminants tels que des métaux lourds ou des pesticides.  
 

Ces 16 indicateurs influencent le dérèglement climatique/ changement climatique auquel nous faisons face aujourd’hui.  
""")
expander.image("https://agribalyse.ademe.fr/static/media/logo.e3e348f6.png")
st.write("On observe notamment que le changement climatique, les particules fines, l'épuisement des ressources en eau, l'épuisement des ressources énergétiques et l'utilisation du sol sont les 5 facteurs les plus importants qui représentent le score unique EF.")
st.caption("À eux 5, ils pondèrent pour 54,79 % du Score Unique EF. À noter que le changement climatique pondère à lui seul 21,06 % du Score Unique EF.")

st.subheader('Comment est distribué le Score Unique EF ?')

fig = px.histogram(data, x="Score unique EF", title="Histogramme de la répartition du Score Unique EF")
st.plotly_chart(fig)
st.write("Cet histogramme montre la distribution des valeurs du Score Unique EF est clairement concentrée vers un score ne dépassant pas la valeur unique de 0,5.")

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
len(variables)
df = data[data["DQR"]<3]
variables_EF = res = [*['Score unique EF'], *variables]
df = df[variables_EF]
st.header("Analyse de la corrélation entre les 16 indicateurs de l'ACV et le score unique EF")
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(10, 7))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, vmin=-1, vmax=1)
st.pyplot(f)

corr = df.corr()['Score unique EF']
st.write("Tableau décroissant des variables les plus corrélées avec le Score unique EF")
top_variables = pd.DataFrame(df.corr()['Score unique EF'].sort_values(ascending=False))
top_variables = top_variables.reset_index()
top_variables = top_variables.iloc[1:, :]
st.dataframe(top_variables)
st.write("On a pu observer précédemment que les 5 variables qui pondéraient le plus le Score unique EF étaient le changement climatique, les particules fines, l'épuisement des ressources en eau, l'épuisement des ressources énergétiques et l'utilisation du sol. En revanche, on remarque que les 5 variables les plus corrélées sont : Les particules fines, l'acidification terrestre et eaux douces, le changement climatique, l'eutrophisation terrestre et les effets toxicologiques cancérigènes.")
st.caption("Pour la suite de notre projet, nous avons fait le choix de travailler sur les 5 variables les plus corrélées avec le score unique EF malgré le fait que ce ne soit pas les variables qui possèdent le plus de pondération dans le calcul de ce dernier.")

df.corr()['Score unique EF'].sort_values(ascending=False)[1:6]
cols_importantes = ["Score unique EF",
                    "Particules fines",
                    "Acidification terrestre et eaux douces",
                    "Changement climatique",
                    "Eutrophisation terrestre",
                    "effets_toxico_cancer"]
top_5_var = ["Particules fines",
                    "Acidification terrestre et eaux douces",
                    "Changement climatique",
                    "Eutrophisation terrestre",
                    "effets_toxico_cancer"]
df_selection = df[cols_importantes]
st.divider()
st.write("**Nous vous laissons poursuivre avec la page 4 sur la comparaison de couples de produits issus de la base de donnée ou revenir à la page d'accueil avec les liens ci-dessous.**")
st.page_link("Homepage.py", label="Page d'accueil", icon="🏠")
st.page_link("pages/4_🍽️_Comparaison_des_produits.py", label="Comparaison des produits 🍽️", icon="4️⃣")

st.sidebar.title('À propos')
st.sidebar.info('Cette application a été développée par Margaux BOYER, Marion DE CACQUERAY, Jules LEFORT et Laure WATERHOUSE.')
