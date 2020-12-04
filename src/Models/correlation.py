import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Correlation : 

    def matrix_correlation(self,df) : 

        
        #remove the column index 
        df_no_index = df.iloc[:,1:] 

        f, ax = plt.subplots(figsize=(20, 10))

        corr = df_no_index.corr()

        sns.heatmap(corr, annot=True, xticklabels=1, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
                    square=False, ax=ax)

        #adjust the figure margin
        plt.subplots_adjust(left=0.1, bottom=0.2, right=1, top=0.9, wspace=0, hspace=0)
        
        #display the graph
        plt.show()

