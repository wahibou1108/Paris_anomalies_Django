import pandas
import csv
import numpy
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import kde
import seaborn as sns
import json
from datetime import datetime

# Lecture du fichier csv
def f_lecture_fichier(chemin_vers_le_fichier) :
    
#df = pandas.read_csv(r"C:\Users\shuai\Documents\FromationPython\anomalie-signalees\dans_ma_rue_ok.csv",sep = ';', encoding = 'unicode_escape', header = 0)
    try:
        df = pandas.read_csv(chemin_vers_le_fichier, sep = ';', encoding = 'unicode_escape', header = 0)
                # supprimer les colonnes qui servent à  rien
        df = df.drop(['ADRESSE','DATE DECLARATION','geo_shape','ID DECLARATION',
                'CONSEIL DE QUARTIER','OUTIL SOURCE','INTERVENANT','ID_DMR','SOUS TYPE DECLARATION'], axis=1)
         #Transformer tous les noms de colunnes en miniscule
        df.columns = df.columns.str.lower()
         #Remplacer les espaces de noms de colonnes par '_'
        df.columns = df.columns.str.replace(" ", "_")
    except:
        df = "Erreur sur le fichier"       
    return df

 #le df
df = f_lecture_fichier("./static/csv/dans_ma_rue.csv")

# generer la dataframe 1 et 3
def f_data_frame(dataFrame) :
    # Ajouter les colonnes min et max de chaque ligne new_df
    dataFrame['min_idxmin'] = dataFrame.idxmin(axis=1)
    dataFrame['max_idxmax'] = dataFrame.idxmax(axis=1)
    # on cree des copie de colonnes min_idxmin et max_idxmax  que l'on nomme min et max
    dataFrame['min'] = dataFrame['min_idxmin'].tolist()
    dataFrame['max'] = dataFrame['max_idxmax'].tolist()
    # Suppression de colonnes min_idxmax et max_idx
    # car elles nous servent Ã  rien (on les a copiÃ©)
    dataFrame = dataFrame.drop(['min_idxmin', 'max_idxmax'],axis=1)
    # la dataframe finale
    return dataFrame.reset_index()

df_1 = f_data_frame(pandas.crosstab([df['arrondissement']], df['annee_declaration']))


# permet de generer le df que je souhaite 
def table_type_anomalie_par_mois(annee) :
    dta = pandas.crosstab([df['type_declaration'], df['annee_declaration']], df['mois_declaration'])
    # pour recuperer type_declaration et année_declaration en colonne
    dt = dta.reset_index()
    dt_frame = dt.groupby('annee_declaration').get_group(annee)
    # Supprimer les colonnes nulles
    # exemple: en 2020 aucune anomalie n'a été signalée entre janvier et aout
    # on suprime donc ces colonnes de la df
    colonne_a_supprimee = []
    for colonne in range(1, 13) :
        somme = 0
        for j in dt_frame[colonne] :
            somme += j
        if somme == 0 :
            colonne_a_supprimee.append(colonne)
    # La data qu'on va retourner
    dt_final = dt_frame.drop(colonne_a_supprimee, axis = 1)
    
    # supprimer egalement les annee_declaration et type_de_declaration
    # pour eviter de fausser les resultat de min et max
    data = dt_final.drop(['annee_declaration', 'type_declaration'], axis=1)
    
    # la valeur de min
    data['min'] = data.min(axis=1)
    # le mois sur lequel on a le min
    data['min_mois'] = data.idxmin(axis=1)

    # le mois sur lequel on a le ax
    data['max_mois'] = data.idxmax(axis=1)
    # la valeur de max
    data['max'] = data.max(axis=1)
    # min_mois correspond au mois sur lequel on le moins d'anomalie signalÃ©e
    dt_final['min_mois'] = data['min_mois']
    # valeur_min correspond au nb d'anomalie signalee de l'annee
    dt_final['valeur_min'] = data['min']

    dt_final['max_mois'] = data['max_mois']
    dt_final['valeur_max'] = data['max']
    #  renomer les index de 1 à 10
    dt_final.index = list(range(1, 11))
    
    return dt_final


# 
class C_dataFrame() :
    def __init__(self, dataframe):
        self.df_1 = dataframe
    # transforme les dicto
    def m_df_dicto(self) :
        return self.df_1.to_dict('index')
    def m_df_ligne(self, ligne) :
        dframe = self.df_1.iloc[ligne : ligne+1]
        return dframe.to_dict('index')
    
data = C_dataFrame(df_1)
# les 2 df qu'ontilisera
df_2020 = C_dataFrame(table_type_anomalie_par_mois(2020))
df_2021 = C_dataFrame(table_type_anomalie_par_mois(2021))

DICT_MOIS = {
    1  : 'Janvier',
    2  : 'Fevrier',
    3  : 'Mars',
    4  : 'Avril',
    5  : 'Mai',
    6  : 'Juin',
    7  : 'Juillet' ,
    8  : 'Aout',
    9  : 'Septembre',
    10 : 'Octobre',
    11 : 'Novembre',
    12 : 'Decembre'
}

df_3 = C_dataFrame(f_data_frame(pandas.crosstab([df['type_declaration']], df['arrondissement'])))
