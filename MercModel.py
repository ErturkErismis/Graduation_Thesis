## Data Preprocessing
## 1-- İmport Library And Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##import seaborn as sbn

MercData=pd.read_csv("Merc.csv")
print(MercData.head())

## Data missing

print(MercData.isnull().sum())

## data Cleaning

print(MercData.corr()["price"].sort_values())

plt.figure(figsize=(7,5))
plt.hist(MercData["price"])
#plt.show()
print(len(MercData))
print(len(MercData)*0.01)

x=MercData.sort_values("price",ascending=False).iloc[130:]
plt.figure(figsize=(7,5))
plt.hist(x["price"])
#plt.show()
print(MercData.groupby("year").mean()["price"])

MercData=x
MercData=MercData[MercData.year != 1970]

print((MercData.groupby("year").mean()["price"]))

MercData=MercData.drop("model",axis=1)

## One Hot Encoding of Categorical Variables

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing
onehotencoder = preprocessing.OneHotEncoder()
MercData['transmission'] = pd.Categorical(MercData['transmission'])
dfDummies = pd.get_dummies(MercData['transmission'], prefix = 'Trans')
print(dfDummies)
MercData=pd.concat([MercData, dfDummies], axis=1)
print(MercData)
MercData=MercData.drop("transmission",axis=1)
onehotencoder2 = preprocessing.OneHotEncoder()
MercData['fuelType'] = pd.Categorical(MercData['fuelType'])
dfDummies2 = pd.get_dummies(MercData['fuelType'], prefix = 'Ftype')
print(dfDummies2)
MercData=pd.concat([MercData, dfDummies2], axis=1)
MercData=MercData.drop("fuelType",axis=1)
print(MercData)

## Spliting Data İnto Training and Testing Data

y=MercData["price"].values
x=MercData.drop("price",axis=1).values

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

model.add(Dense(15,activation="relu"))
model.add(Dense(15,activation="relu"))
model.add(Dense(15,activation="relu"))
model.add(Dense(15,activation="relu"))

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
model.save("FordModel.h5")
import joblib
joblib.dump(scaler, 'Mercscaler.save')
