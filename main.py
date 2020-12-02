import pandas as pd
import numpy as np
import matplotlib

# Read csv file 
df = pd.read_csv('immoweb_scrapped.csv')
#remove Nan in column price
df = df[df['price'].notna()]
#Check if there is duplicate data
x = df[df.duplicated(['id'])]
#remove white space in case there is 
df.columns = df.columns.str.strip()
#check if there is no strange property type
df.type_of_property.value_counts()
#check if there is no strange subtype of property
df.subtype_of_property.value_counts()
print(df.columns)
#print first 10 items
print(df.head(10))