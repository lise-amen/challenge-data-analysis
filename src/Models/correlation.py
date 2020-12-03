import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Correlation : 

    def matrix_correlation(self,df) : 

        #remove the column index 
        df_no_index = df.iloc[:,1:] 

        f, ax = plt.subplots(figsize=(10, 10))

        corr = df_no_index.corr()

        sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
                    square=True, ax=ax)
        
        #display the graph
        plt.show()

