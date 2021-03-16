## Data Preprocessing
## 1-- İmport Library And Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##import seaborn as sbn

FordData=pd.read_csv("ford.csv")
print(FordData.head())

## Data missing

print(FordData.isnull().sum())

## data Cleaning

print(FordData.corr()["price"].sort_values())

plt.figure(figsize=(7,5))
plt.hist(FordData["price"])
#plt.show()
print(len(FordData))
print(len(FordData)*0.01)

x=FordData.sort_values("price",ascending=False).iloc[180:]
plt.figure(figsize=(7,5))
plt.hist(x["price"])
#plt.show()
print(FordData.groupby("year").mean()["price"])

FordData=x
FordData=FordData[FordData.year != 2060]

print((FordData.groupby("year").mean()["price"]))

FordData=FordData.drop("model",axis=1)

## One Hot Encoding of Categorical Variables

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
onehotencoder = preprocessing.OneHotEncoder()
FordData['transmission'] = pd.Categorical(FordData['transmission'])
dfDummies = pd.get_dummies(FordData['transmission'], prefix = 'Trans')
print(dfDummies)
FordData=pd.concat([FordData, dfDummies], axis=1)
print(FordData)
FordData=FordData.drop("transmission",axis=1)
onehotencoder2 = preprocessing.OneHotEncoder()
FordData['fuelType'] = pd.Categorical(FordData['fuelType'])
dfDummies2 = pd.get_dummies(FordData['fuelType'], prefix = 'Ftype')
dfDummies2
FordData=pd.concat([FordData, dfDummies2], axis=1)
FordData=FordData.drop("fuelType",axis=1)
print(FordData)

## Spliting Data İnto Training and Testing Data

y=FordData["price"].values
x=FordData.drop("price",axis=1).values

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

model.fit(x=x_train,y=y_train,validation_data=(x_test,y_test),batch_size=250,epochs=250)

LostData=pd.DataFrame(model.history.history)

LostData.head()

LostData.plot()

from sklearn.metrics import mean_absolute_error, mean_squared_error

tahmindizisi=model.predict(x_test)
print(tahmindizisi)
mean_absolute_error(y_test,tahmindizisi)
plt.scatter(y_test,tahmindizisi)

model.save("FordModel.h5")


