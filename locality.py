import pandas as pd
import numpy as np
from main import *

def getDf():
   immo = pd.read_csv('immoweb_scrapped.csv',encoding='utf-8-sig')
   localite = pd.read_csv('liste-des-codes-postaux-belges-fr.csv',sep=';',encoding='utf-8-sig')
   del localite['Sous-commune']
   #remove the column type_of_sale

   df = filtring(immo)


   #append both data frame with match postal code 
   merged_left = pd.merge(left=df,right=localite ,how ='left', left_on='locality', right_on='Code postal')
   del merged_left['Code postal']
   return addRegion(merged_left)

def addRegion(df):
    flandre = ['Flandre-Occidentale','Flandre-Orientale','Brabant Flamand','Anvers','Limbourg']
    wallonie =['Liège','Hainaut','Namur','Brabant Wallon', 'Luxembourg']
    bruxelles = ['Bruxelles (19 communes)']
    df['Region'] = np.select([df['Province'].isin(flandre),df['Province'].isin(wallonie),df['Province'].isin(bruxelles)],
                           ['Flandre','Wallonie','Bruxelles'])
    ######## I Normalize value in col as there is accents ################################
    df['Province'] = df['Province'].str.normalize('NFKD')\
       .str.encode('ascii', errors='ignore')\
       .str.decode('utf-8')
    df['Localité'] = df['Localité'].str.normalize('NFKD')\
       .str.encode('ascii', errors='ignore')\
       .str.decode('utf-8')
    df['Commune principale']= df['Commune principale'].str.normalize('NFKD')\
       .str.encode('ascii', errors='ignore')\
       .str.decode('utf-8')
    ######## I set type to str #################################
    df["Region"] = df["Region"].astype("|S")
    df["Province"] = df["Province"].astype("|S")
    df["Localité"] = df["Localité"].astype("|S")
    df["Commune principale"] = df["Commune principale"].astype("|S")
    return df


## Try make graoph on belgium map by region , province