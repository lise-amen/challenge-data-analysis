import pandas as pd
import numpy as np

df = pd.read_csv('immoweb_scrapped.csv')

# print(df.head())
# print(df['swimming_pool'])
# print(df['swimming_pool'].isnull())

print(df.total_land_area.min())
