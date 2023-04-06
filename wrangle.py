# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. acquire
4. prepare_mvp
5. wrangle_zillow_mvp
6. split
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to create functions for both the acquire & preparation phase of the data
science pipeline or also known as 'wrangle' data...
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
from sklearn.model_selection import train_test_split
import os
import env

# =======================================================================================================
# Imports END
# Imports TO acquire
# acquire START
# =======================================================================================================

def acquire():
    '''
    Obtains the vanilla version of zillow dataframe
    '''
    query = '''
            SELECT
                *
            FROM
                (SELECT 
                    parcelid, 
                    logerror, 
                    transactiondate 
                FROM 
                    predictions_2017 
                WHERE 
                    transactiondate LIKE %s) AS A
            LEFT JOIN 
                (SELECT 
                    * 
                FROM 
                    properties_2017 
                WHERE 
                    propertylandusetypeid = 261 
                    OR propertylandusetypeid = 279) AS B USING(parcelid)
            LEFT JOIN airconditioningtype USING(airconditioningtypeid)
            LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
            LEFT JOIN buildingclasstype USING(buildingclasstypeid)
            LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
            LEFT JOIN propertylandusetype USING(propertylandusetypeid)
            LEFT JOIN storytype USING(storytypeid)
            LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)'''
    params = ('2017%', )
    url = env.get_db_url('zillow')
    zillow = pd.read_sql(query, url, params=params)
    return zillow

# =======================================================================================================
# acquire END
# acquire TO prepare_mvp
# prepare_mvp START
# =======================================================================================================

def prepare_mvp():
    '''
    Takes in the vanilla zillow dataframe and returns a cleaned version that is ready for exploration
    and further analysis
    '''
    zillow = acquire()
    zillow = zillow.drop(columns=[ 
        'typeconstructiontypeid',
        'storytypeid',
        'propertylandusetypeid',
        'heatingorsystemtypeid',
        'buildingclasstypeid',
        'architecturalstyletypeid',
        'airconditioningtypeid',
        'parcelid',
        'logerror',
        'transactiondate',
        'id',
        'basementsqft',
        'bathroomcnt',
        'buildingqualitytypeid',
        'calculatedbathnbr',
        'decktypeid',
        'finishedfloor1squarefeet',
        'finishedsquarefeet12',
        'finishedsquarefeet13',
        'finishedsquarefeet15',
        'finishedsquarefeet50',
        'finishedsquarefeet6',
        'fireplacecnt',
        'garagecarcnt',
        'garagetotalsqft',
        'hashottuborspa',
        'latitude',
        'longitude',
        'poolcnt',
        'poolsizesum',
        'pooltypeid10',
        'pooltypeid2',
        'pooltypeid7',
        'propertycountylandusecode',
        'propertyzoningdesc',
        'rawcensustractandblock',
        'regionidcity',
        'regionidcounty',
        'regionidneighborhood',
        'regionidzip',
        'roomcnt',
        'threequarterbathnbr',
        'unitcnt',
        'yardbuildingsqft17',
        'yardbuildingsqft26',
        'numberofstories',
        'fireplaceflag',
        'structuretaxvaluedollarcnt',
        'assessmentyear',
        'landtaxvaluedollarcnt',
        'taxamount',
        'taxdelinquencyflag',
        'taxdelinquencyyear',
        'censustractandblock',
        'airconditioningdesc',
        'architecturalstyledesc',
        'buildingclassdesc',
        'heatingorsystemdesc',
        'propertylandusedesc',
        'storydesc',
        'typeconstructiondesc'])
    zillow.bedroomcnt = zillow.bedroomcnt.fillna(3.0).astype(int)
    zillow.calculatedfinishedsquarefeet = zillow.calculatedfinishedsquarefeet.fillna(1922.89)
    zillow.fips = zillow.fips.fillna(6037).astype(int)
    zillow.fullbathcnt = zillow.fullbathcnt.fillna(2.0).astype(int)
    zillow.lotsizesquarefeet = zillow.lotsizesquarefeet.fillna(11339.62)
    zillow.yearbuilt = zillow.yearbuilt.fillna(1955).astype(int)
    zillow.taxvaluedollarcnt = zillow.taxvaluedollarcnt.fillna(529688.16)
    conditions = [
        zillow.fips == 6037,
        zillow.fips == 6059,
        zillow.fips == 6111
        ]

    choices = [
        'Los Angeles',
        'Orange',
        'Ventura'
        ]
    zillow.fips = np.select(conditions, choices)
    zillow.yearbuilt = 2017 - zillow.yearbuilt
    zillow = zillow.rename(columns={
    'bedroomcnt' : 'bedrooms',
    'calculatedfinishedsquarefeet' : 'home_sqft',
    'fips' : 'county',
    'fullbathcnt' : 'full_bathrooms',
    'lotsizesquarefeet' : 'lotsize_sqft',
    'yearbuilt' : 'home_age',
    'taxvaluedollarcnt' : 'value'
    })
    zillow['home_lot_ratio'] = round(zillow.home_sqft / zillow.lotsize_sqft, 2)
    dummies = pd.get_dummies(zillow.select_dtypes(include='object'))
    zillow = pd.concat([zillow, dummies], axis=1)
    zillow = zillow.drop(columns='county')
    return zillow

# =======================================================================================================
# prepare_mvp END
# prepare_mvp TO wrangle_zillow_mvp
# wrangle_zillow_mvp START
# =======================================================================================================

def wrangle_zillow_mvp():
    '''
    Function that acquires, prepares, and splits the zillow dataframe for use as well as 
    creating a csv.
    '''
    if os.path.exists('zillow.csv'):
        zillow = pd.read_csv('zillow.csv', index_col=0)
        train, validate, test = split(zillow)
        return train, validate, test
    else:
        zillow = prepare_mvp()
        zillow.to_csv('zillow.csv')
        train, validate, test = split(zillow)
        return train, validate, test
    
# =======================================================================================================
# wrangle_zillow END
# wrangle_zillow TO split
# split START
# =======================================================================================================

def split(df):
    '''
    Takes a dataframe and splits the data into a train, validate and test datasets
    '''
    train_val, test = train_test_split(df, train_size=0.8, random_state=1349)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=1349)
    print(f"train.shape:{train.shape}\nvalidate.shape:{validate.shape}\ntest.shape:{test.shape}")
    return train, validate, test


# =======================================================================================================
# split END
# =======================================================================================================