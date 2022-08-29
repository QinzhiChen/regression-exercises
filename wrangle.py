#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import os
import csv


# In[ ]:


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[ ]:


def wrangle_zillow():
    file='zillow2017_df.csv'
    if os.path.isfile(file):
        return pd.read_csv(file)
    else:
        zillow2017 = pd.read_sql(('SELECT bedroomcnt,bathroomcnt,calculatedfinishedsquarefeet,taxvaluedollarcnt,yearbuilt,taxamount,fips FROM properties_2017'), get_connection('zillow'))
        zillow2017.to_csv(file,index=False)
        zillow2017 = zillow2017.replace(r'^\s*$', np.NaN, regex=True)
        zillow2017_df = zillow2017.dropna()
        zillow2017_df = zillow2017_df.astype('int')
    return zillow2017_df

