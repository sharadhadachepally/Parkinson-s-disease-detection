# -*- coding: utf-8 -*-
"""Parkinson's disease detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gbcPOqU8L7gaE_hCqhucXulEyjpXIhhc
"""

import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=pd.read_csv("/content/pd_speech_features.csv")
data

features=data.loc[:,data.columns!='gender'].values[:,1:]
labels=data.loc[:,'gender'].values

scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels

x_t,x_test,y_t,y_test=train_test_split(x, y, test_size=0.3, random_state=8)

model=XGBClassifier()
model.fit(x_t,y_t)

y_pred=model.predict(x_test)
print(accuracy_score(y_test, y_pred)*100)