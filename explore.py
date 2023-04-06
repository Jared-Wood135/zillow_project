# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. plot_variable_pairs
4. plot_categorical_and_continuous_vars
5. vis3_catandcont
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to create functions for exploratory and visualization purposes
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from scipy import stats
from sklearn.model_selection import train_test_split
import os
import wrangle

# =======================================================================================================
# Imports END
# Imports TO plot_variable_pairs
# plot_variable_pairs START
# =======================================================================================================

def plot_variable_pairs(df):
    '''
    Takes in a dataframe and gets all of the float and int dtype columns then 
    returns a histogram, boxplot, and a .describe for each column
    '''
    quantitative_col = df.select_dtypes(include=['float', 'int'])
    for col in quantitative_col:
        sns.histplot(quantitative_col[col])
        plt.title(f'Distribution of {col}')
        plt.show()
        sns.boxplot(quantitative_col[col])
        plt.title(f'Distribution of {col}')
        plt.show()
        print(quantitative_col[col].describe().to_markdown())
        print('\n=======================================================\n')

# =======================================================================================================
# plot_variable_pairs END
# plot_variable_pairs TO plot_categorical_and_continuous_vars
# plot_categorical_and_continuous_vars START
# =======================================================================================================

def plot_categorical_and_continuous_vars(df):
    '''
    Takes in a dataframe and separates all of the columns into category or values then
    returns a bargraph of each unique combination of category and value columns
    '''
    val_col = []
    cat_col = []
    for col in df:
        if df[col].dtype == 'O':
            cat_col.append(col)
        elif (df[col].dtype == 'float64') | (df[col].dtype == 'int'):
            val_col.append(col)
    combo_col = list(itertools.product(cat_col, val_col))
    for x, y in combo_col:
        sns.barplot(x=df[x], y=df[y])
        plt.title(f'Relationship of {x} and {y}')
        plt.axhline(y=df[y].mean(), color='r', label=f'Mean: {round(df[y].mean(), 2)}')
        plt.legend()
        plt.show()
        print(df.groupby(x)[y].describe().T.to_markdown())
        print('\n=======================================================\n')

# =======================================================================================================
# plot_categorical_and_continuous_vars END
# plot_categorical_and_continuous_vars TO vis3_catandcont
# vis3_catandcont START
# =======================================================================================================

def vis3_catandcont(data, figsize1, figsize2, unique_cutoff):
    '''
    Takes in a dataframe and separates columns into continuous or categorical based on the percentage
    of unique values within each column, then creates 3 visuals for each combination of columns.

    INPUT:
    data = pandas dataframe
    figsize1 = Size of visuals
    figsize2 = Size of visuals
    unique_cutoff = Percentage of uniques that if the column is higher than, it will be deemed continuous

    OUTPUT:
    - Subplot with 3 visuals for each combination of columns
    '''
    categorical_cols = []
    continuous_cols = []
    for col in data:
        if (data[col].nunique() / data.shape[0]) < unique_cutoff:
            categorical_cols.append(col)
        else:
            continuous_cols.append(col)
    combo_list = list(itertools.product(categorical_cols, continuous_cols))
    fig, axs = plt.subplots(len(combo_list), 3, figsize=(figsize1, figsize2))
    for (ax1, ax2, ax3), combo in zip(axs, combo_list):
        sns.violinplot(data=data, x=combo[0], y=combo[1], ax=ax1)
        ax1.set(title=f'{combo[0]} vs. {combo[1]}',
                xlabel=f'{combo[0]}',
                ylabel=f'{combo[1]}')
        sns.regplot(data=data, x=combo[0], y=combo[1], color='red', ax=ax2)
        ax2.set(title=f'{combo[0]} vs. {combo[1]}',
                xlabel=f'{combo[0]}',
                ylabel=f'{combo[1]}')
        sns.swarmplot(data=data, x=combo[0], y=combo[1], ax=ax3)
        ax3.set(title=f'{combo[0]} vs. {combo[1]}',
                xlabel=f'{combo[0]}',
                ylabel=f'{combo[1]}')
    plt.tight_layout()
    plt.show()

# =======================================================================================================
# vis3_catandcont END
# =======================================================================================================