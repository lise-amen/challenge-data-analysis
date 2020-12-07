import matplotlib
import seaborn as sns
import numpy as np
import pandas as pd
from locality import *

df = getDf()


### GRAPH BELGIUM municipalities => AVG price , median price , price per sqaure meter

## commune , surface , price


## localité + price
df['Province'] = df['Province'].str.decode('utf-8') 
# ax = sns.barplot(x="Province", y="price", data=df)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
# plt.tight_layout()
# plt.show()


# create bins interval using numpy
# min = df['area'].min()
# max =df['area'].max()
# binsVal = np.arange(min,max,50)
m2 = df['price']/df['area']
avg = len(df.index)/ df['price'].mean()
median = df['price'].median()


print(m2,'m2')
print(avg,'avg')
print(median,'median')
# ax = sns.lmplot(x='area',y='price', data=df, hue='Province',height=10)
# plt.xlabel("area")
# plt.ylabel("price")
# plt.tight_layout()
# plt.show()

"""
##REGION MOYENNE + BAR by REGION barplot
Region = df.groupby('Region').mean().reset_index
plt.figure(figsize=(10,6)) 
avg = len(df.index)/ df['price'].mean()
max = df['area'].max()
min = df['area'].min()
binsVal = np.arange(min,max,50)
ax = sns.barplot(x = 'area', y= 'price', data=df, hue='Region', estimator=np.median)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right",fontsize=7)
plt.tight_layout()
plt.show()"""


##REGION MOYENNE Price PER AREA by Region
Region_price = df.groupby('Region')['price'].mean()
Region_area = df.groupby('Region')['area'].mean()
print('Average price by Region \n', Region_price)
price_per_area = (Region_price/Region_area)
print('Average price per area by Region\n', price_per_area)

list_region = price_per_area.index.tolist()
list_price_per_area = price_per_area.tolist()

fig, ax = plt.subplots()
plt.bar(list_region, list_price_per_area)
plt.title("Average price per area by Region") 
plt.ylabel("€/m²") 
plt.show()



