# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. visual
4. model_scores
5. stats
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to create functions for expediting the presentation of the 
'final_report'.ipynb.
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
from scipy import stats
import wrangle

# =======================================================================================================
# Imports END
# Imports TO visual
# visual START
# =======================================================================================================

def visual():
    '''
    Function that returns 5 key visuals to help reinforce feature selection decision.
    '''
    train, validate, test = wrangle.wrangle_zillow_mvp()
    key_features = [
        'bedrooms',
        'home_sqft',
        'full_bathrooms',
        'home_lot_ratio',
        'home_age'
    ]
    for key in key_features:
        sns.regplot(data=train, x=train[key], y='value', line_kws={'color': 'red'})
        plt.title(f'{key} vs. value')
        plt.show()

# =======================================================================================================
# visual END
# visual TO model_scores
# model_scores START
# =======================================================================================================

def model_scores():
    '''
    Function that returns a table of baseline and top model scores to help reinforce model selection.
    '''
    model_dict = {
    'model' : ['baseline', 'poly', 'lr', 'tdr_pow0_a1'],
    'type' : ['baseline(mean)', 'Polynomial Regression', 'Linear Regression', 'TweedieRegressor'],
    'rmse' : [685403.82, 491313.79, 670163.46, 726863.46],
    'r2' : [0.00, 0.49, 0.38, 0.27]
    }
    return pd.DataFrame(model_dict)

# =======================================================================================================
# model_scores END
# model_scores TO stats
# stats START
# =======================================================================================================

def stat_testing(df):
    '''
    Function that returns a list of stats testing on features to determine whether or not the feature
    can reject the null hypothesis.
    '''
    stat_list = df.drop(columns='value').columns.to_list()
    alpha = 0.05
    for col in stat_list:
        r, p = stats.spearmanr(df['value'], df[col])
        if p < alpha:
            print(f'\033[32m===== REJECT NULL HYPOTHESIS! =====\033[0m')
            print(f'\033[35mFeature:\033[0m {col}')
            print(f'\033[35mCorrelation Value:\033[0m {r:.2f}')
            print(f'\033[35mP-Value:\033[0m {p:.2f}\n\n')
        else:
            print(f'\033[31m===== ACCEPT NULL HYPOTHESIS! =====\033[0m')
            print(f'\033[35mFeature:\033[0m {col}')
            print(f'\033[35mCorrelation Value:\033[0m {r:.2f}')
            print(f'\033[35mP-Value:\033[0m {p:.2f}\n\n')
    

# =======================================================================================================
# stats END
# =======================================================================================================