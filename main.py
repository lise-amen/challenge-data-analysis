import pandas as pd
import numpy as np
import matplotlib

# Read csv file 
df = pd.read_csv('immoweb_scrapped.csv')

#remove Nan in column price, area
df = df[df['price'].notna() & df['area'].notna()& df['building_condition'].notna()]
#remove Nan in column price, area and total_land_area if we need later for a different graph
#df = df[df['price'].notna() & df['area'].notna()& df['total_land_area'].notna()]

#Check if there is duplicate data
x = df[df.duplicated(['id'])]
#remove white space in case there is 
df.columns = df.columns.str.strip()
#check if there is no strange property type
df.type_of_property.value_counts()
#check if there is no strange subtype of property
df.subtype_of_property.value_counts()
# df.loc[df['column name'] condition, 'new column name'] = 'value if condition is met'

############## set the number of room to one if it's equal to 0 (WE NEED A PLACE TO SLEEP CMON) #############
df.loc[df['nr_of_rooms'] == 0, 'nr_of_rooms'] = 1
df.loc[df['nr_of_facades'] == 0, 'nr_of_facades'] = 1
df.loc[df['nr_of_facades'] == 10, 'nr_of_facades'] = 1
df.loc[df['garden_area'].isna(), 'garden_area'] = 0
df.loc[df['terrace_area'].isna(), 'terrace_area'] = 0
df.loc[df['type_of_sale'].isna(), 'type_of_sale'] = 0

############## Set total_land_area to area if NaN #############
df.loc[df['total_land_area'].isna(), 'total_land_area'] = df.area

##############set furnished to NOT_SPECIFIED if it's NaN #############
df.loc[df['furnished'].isna(), 'furnished'] = False
df.loc[df['open_fire'].isna(), 'open_fire'] = False
df.loc[df['terrace'].isna(), 'terrace'] = False
df.loc[df['garden'].isna(), 'garden'] = False
df.loc[df['swimming_pool'].isna(), 'swimming_pool'] = False

#############Define type of object type##################
df['swimming_pool'] = df['swimming_pool'].astype('bool')
df['furnished'] = df['furnished'].astype('bool')
df['terrace'] = df['terrace'].astype('bool')
df['garden'] = df['garden'].astype('bool')

############# Set to int all object type ##########
# NEED TO SET ALL BOOL BEFORE DOING THIS (even if actually it's not really a problem, 0 1)
for col in df.select_dtypes(['object']):
    x = df[col].unique()
    x_dict = dict(zip(x, range(len(x))))
    df[col] = [x_dict[type] for type in df[col]]


#Number of rows and cols
print(df.shape)

#Correlation between all col
price = df['price']
cols = df.loc[:,df.columns != 'price']
#print(df[df.columns[1:]].corr()['price'][:])

#Correlation between target (price) and other cols
corr_matrix = df.corrwith(df['price'])
print(corr_matrix.sort_values(ascending=False))
#Get max of correlation
print(corr_matrix.drop(['price']).idxmax())
# Get Min of correlation
print(corr_matrix.idxmin())
print(df.type_of_sale.head())
print(df)

