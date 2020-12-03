import pandas as pd 

zip = pd.read_csv('liste-des-codes-postaux-belges-fr.csv', sep=';')

zip = pd.DataFrame(data=zip) #define column

print(zip.head())

print(zip['Province'].value_counts())

if zip['Province'] == Namur : 
    zip['Région'] = Wallonie

if zip['Province'] == Liège : 
    zip['Région'] = Wallonie

if zip['Province'] == Flandre-Orientale : 
    zip['Région'] = Wallonie

if zip['Province'] == Flandre-Occidentale : 
    zip['Région'] = Flandre

if zip['Province'] == Brabant Flamand : 
    zip['Région'] = Flandre

if zip['Province'] == Luxembourg : 

if zip['Province'] == Anvers : 
    zip['Région'] = Flandre

if zip['Province'] == Braband Wallon : 
    zip['Région'] = Wallonie

if zip['Province'] == Bruxelles : 
    zip['Région'] == Bruxelles 




































































































































































