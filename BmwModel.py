## Data Preprocessing
## 1-- İmport Library And Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##import seaborn as sbn

BmwData=pd.read_csv("bmw.csv")
print(BmwData.head())

## Data missing

print(BmwData.isnull().sum())

## data Cleaning

print(BmwData.corr()["price"].sort_values())

plt.figure(figsize=(7,5))
plt.hist(BmwData["price"])
#plt.show()
print(len(BmwData))
print(len(BmwData)*0.01)

x=BmwData.sort_values("price",ascending=False).iloc[107:]
plt.figure(figsize=(7,5))
plt.hist(x["price"])
#plt.show()

## One Hot Encoding of Categorical Variables

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
onehotencoder = preprocessing.OneHotEncoder()
BmwData['transmission'] = pd.Categorical(BmwData['transmission'])
dfDummies = pd.get_dummies(BmwData['transmission'], prefix = 'Trans')
print(dfDummies)
BmwData=pd.concat([BmwData, dfDummies], axis=1)
print(BmwData)
BmwData=BmwData.drop("transmission",axis=1)

onehotencoder2 = preprocessing.OneHotEncoder()
BmwData['fuelType'] = pd.Categorical(BmwData['fuelType'])
dfDummies2 = pd.get_dummies(BmwData['fuelType'], prefix = 'Ftype')
print(dfDummies2)
BmwData=pd.concat([BmwData, dfDummies2], axis=1)
BmwData=BmwData.drop("fuelType",axis=1)
print(BmwData)

onehotencoder3 = preprocessing.OneHotEncoder()
BmwData['model'] = pd.Categorical(BmwData['model'])
dfDummies3 = pd.get_dummies(BmwData['model'], prefix = 'Model')
print(dfDummies3)
BmwData=pd.concat([BmwData, dfDummies3], axis=1)
BmwData=BmwData.drop("model",axis=1)
print(BmwData)

## Spliting Data İnto Training and Testing Data

y=BmwData["price"].values
x=BmwData.drop("price",axis=1).values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.3,random_state=10)

## Data Scaling
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)
print(x_train.shape)

## Deep Learning Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model=Sequential()

model.add(Dense(20,activation="relu"))
model.add(Dense(20,activation="relu"))
model.add(Dense(20,activation="relu"))
model.add(Dense(20,activation="relu"))

model.add(Dense(1))

model.compile(optimizer="adam",loss="mse")

model.fit(x=x_train,y=y_train,validation_data=(x_test,y_test),batch_size=200,epochs=250)

LostData=pd.DataFrame(model.history.history)

LostData.head()

LostData.plot()

from sklearn.metrics import mean_absolute_error, mean_squared_error

tahmindizisi=model.predict(x_test)
print(tahmindizisi)
mean_absolute_error(y_test,tahmindizisi)
plt.scatter(y_test,tahmindizisi)
plt.show()
model.save("BmwModel.h5")
import joblib
joblib.dump(scaler, 'Bmwscaler.save')
