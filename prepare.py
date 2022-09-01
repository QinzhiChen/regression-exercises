import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer
from scipy import stats
import sklearn.preprocessing
from env import user, password, host
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import os
import csv
import wrangle_zillow

def scale(scaler,zillow_train,zillow_validate,zillow_test,cols=['bedroom','bathroom','sqtft','taxvalue'],return_scaler=True):
    zillow_train,zillow_validate,zillow_test=wrangle_zillow.wrangle_zillow(1.5)
    zillow_train.transactiondate=pd.DatetimeIndex(zillow_train.transactiondate)
    zillow_validate.transactiondate=pd.DatetimeIndex(zillow_validate.transactiondate)
    zillow_test.transactiondate=pd.DatetimeIndex(zillow_test.transactiondate)
    zillow_train_scaled=zillow_train.copy()
    zillow_validate_scaled=zillow_validate.copy()
    zillow_test_scaled=zillow_test.copy()
    scaler=scaler
    zillow_train_scaled[cols] = scaler.fit_transform(zillow_train[cols])
    zillow_validate_scaled[cols] = scaler.fit_transform(zillow_validate[cols])
    zillow_test_scaled[cols] = scaler.fit_transform(zillow_test[cols])
    return scaler, zillow_train_scaled,zillow_validate_scaled, zillow_test_scaled
    

def visualize_scaler(scaler, df, cols, bins):
    fig, axs = plt.subplots(len(cols), 2, figsize=(16,9))
    df_scaled = df.copy()
    df_scaled[cols] = scaler.fit_transform(df[cols])
    for (ax1, ax2), col in zip(axs, cols):
        ax1.hist(df[col], bins=bins)
        ax1.set(title=f'{col} before scaling', xlabel=col, ylabel='count')
        ax2.hist(df_scaled[col], bins=bins)
        ax2.set(title=f'{col} after scaling with {scaler.__class__.__name__}', xlabel=col, ylabel='count')
    plt.tight_layout()