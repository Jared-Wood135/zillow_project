# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. visual
4. model_scores
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
import wrangle

# =======================================================================================================
# Imports END
# Imports TO visual
# visual START
# =======================================================================================================

def visual():
    '''
    Function that returns 4 key visuals to help reinforce feature selection decision.
    '''
    train, validate, test = wrangle.wrangle_zillow_mvp()
    key_features = [
        'bedrooms',
        'home_sqft',
        'full_bathrooms',
        'home_lot_ratio'
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
    'model' : ['baseline', 'poly'],
    'type' : ['baseline(mean)', 'Polynomial Regression'],
    'rmse' : [685403.82, 491313.79],
    'r2' : [0.00, 0.49]
    }
    return pd.DataFrame(model_dict)

# =======================================================================================================
# model_scores END
# =======================================================================================================