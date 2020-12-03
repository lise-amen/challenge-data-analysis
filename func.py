
import pandas as pd
import numpy as np
import matplotlib

# Read csv file 
df = pd.read_csv('immoweb_scrapped.csv')
corr_matrix = df.corrwith(df['price'])


############## Percentage of missing values per columns #############
def percentMissing(df):
    percent_missing = df.isnull().sum()*100 /len(df)
    missing_value_df = pd.DataFrame({'column_name': df.columns, 'percent_missing':percent_missing})
    return round(missing_value_df)

############# Set to int all object type ##########
# NEED TO SET ALL BOOL BEFORE DOING THIS (even if actually it's not really a problem, 0 1)
def setObjToInt(df):
    for col in df.select_dtypes(['object']):
        x = df[col].unique()
        x_dict = dict(zip(x, range(len(x))))
        df[col] = [x_dict[type] for type in df[col]]
    return df

#Number of rows and cols
def getShape(df):
    return(df.shape)

#Correlation between all col
def corrAll(df):
    price = df['price']
    cols = df.loc[:,df.columns != 'price']
    return df[df.columns[1:]].corr()['price'][:]

#Correlation between target (price) and other cols
def corrPrice():
    return corr_matrix.sort_values(ascending=False)

#Get max of correlation
def corrMax():
    return corr_matrix.drop(['price']).idxmax()

# Get Min of correlation
def corrMin():
    return corr_matrix.idxmin()