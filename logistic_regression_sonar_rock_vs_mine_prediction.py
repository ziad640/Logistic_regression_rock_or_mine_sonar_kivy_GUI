# -*- coding: utf-8 -*-
"""logistic_regression_sonar rock_vs_mine_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17EbPfPFgrBVryUBVkHr5JBPlD51N2U9k
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header=None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

#60 is the number of columns
sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

print(X_train)
print(Y_train)

model = LogisticRegression()

model.fit(X_train, Y_train)

#accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)

#Predictive System
input_data = (0.0299,0.0688,0.0992,0.1021,0.0800,0.0629,0.0130,0.0813,0.1761,0.0998,0.0523,0.0904,0.2655,0.3099,0.3520,0.3892,0.3962,0.2449,0.2355,0.3045,0.3112,0.4698,0.5534,0.4532,0.4464,0.4670,0.4621,0.6988,0.7626,0.7025,0.7382,0.7446,0.7927,0.5227,0.3967,0.3042,0.1309,0.2408,0.1780,0.1598,0.5657,0.6443,0.4241,0.4567,0.5760,0.5293,0.3287,0.1283,0.0698,0.0334,0.0342,0.0459,0.0277,0.0172,0.0087,0.0046,0.0203,0.0130,0.0115,0.0015)

# changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a mine')