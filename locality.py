import pandas as pd
from main import *


immo = pd.read_csv('immoweb_scrapped.csv')
localite = pd.read_csv('liste-des-codes-postaux-belges-fr.csv',sep=';')
del localite['Sous-commune']
df = filtring(immo)


#append both data frame with matche postal code 
merged_left = pd.merge(left=df,right=localite ,how ='left', left_on='locality', right_on='Code postal')
print(merged_left)