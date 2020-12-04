import pandas as pd
import numpy as np
from main import *


immo = pd.read_csv('immoweb_scrapped.csv')
localite = pd.read_csv('liste-des-codes-postaux-belges-fr.csv',sep=';')
del localite['Sous-commune']
df = filtring(immo)


#append both data frame with matche postal code 
merged_left = pd.merge(left=df,right=localite ,how ='left', left_on='locality', right_on='Code postal')
del merged_left['Code postal']

def addRegion(df):
    flandre = ['Flandre-Occidentale','Flandre-Orientale','Brabant Flamand','Anvers','Limbourg']
    wallonie =['Liège','Hainaut','Namur','Brabant Wallon', 'Luxembourg']
    bruxelles = ['Bruxelles (19 communes)']
    df['Region'] = np.select([df['Province'].isin(flandre),df['Province'].isin(wallonie),df['Province'].isin(bruxelles)],
                           ['Flandre','Wallonie','Bruxelles'])
    print(df.Region.value_counts())
addRegion(merged_left)


## Graph correlation
## Try make graoph on belgium map by region , province