# -*- coding: utf-8 -*-
"""Car Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O59oV8MejtTgOFFDThMKjQtVTKJIKWvH

#Importing the dependencies
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import metrics

"""#Data collection and Processing"""

#loadiing the data from CSV file to pandas data frame
car_dataset= pd.read_csv('/content/car data.csv')

#inspecting the first 5 rows of the data frame
car_dataset.head()

#checking the number of rows and columns
car_dataset.shape

#getting some information about dataset
car_dataset.info()

#checking the number of missing values
car_dataset.isnull().sum()

#checking the distribution of categorical data
print(car_dataset.Fuel_Type.value_counts())
print(car_dataset.Seller_Type.value_counts())
print(car_dataset.Transmission.value_counts())

"""#Encoding the categorical Data"""

#encoding Fuel_Type column
car_dataset.replace({'Fuel_Type':{'Petrol':0, 'Diesel':1, 'CNG':2}}, inplace=True)

#encoding Seller_Type column
car_dataset.replace({'Seller_Type':{'Dealer':0, 'Individual':1}}, inplace=True)

#encoding Transmission column
car_dataset.replace({'Transmission':{'Manual':0, 'Automatic':1}}, inplace=True)

car_dataset.head()

"""#Splitting the data into training and target"""

x= car_dataset.drop(['Car_Name', 'Selling_Price'], axis=1)

y= car_dataset['Selling_Price']

print(x)

print(y)

#Splitting the data into Training And Test data
x_train, x_test, y_train, y_test= train_test_split(x,y, test_size =0.2, random_state=2)

"""#Model  Training
1: LinearRegression
"""

#Loading the linearRegression Model
lin_reg_model = LinearRegression()
lin_reg_model.fit(x_train, y_train)

"""#Evaluating the model"""

#prediction on traing data
training_data_prediction= lin_reg_model.predict(x_train)

#R Square Error
error_score= metrics.r2_score(y_train, training_data_prediction)
print("R Square Error: ",error_score)

"""#Visualizing the actual prices and Predicted prices"""

plt.scatter(y_train, training_data_prediction)
plt.xlabel("Actual Price", color= "Red")
plt.ylabel("Predicted Price", color="Blue")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

#prediction on test data
test_data_prediction= lin_reg_model.predict(x_test)

#R Square Error
error_score= metrics.r2_score(y_test, test_data_prediction)
print("R Square Error: ",error_score)

"""#Visualizing the actual prices and Predicted prices"""

plt.scatter(y_test, test_data_prediction)
plt.xlabel("Actual Price", color= "Red")
plt.ylabel("Predicted Price", color="Blue")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""#2: Lasso Model"""

#Loading the linearRegression Model
las_model = Lasso()
las_model.fit(x_train, y_train)

#prediction on traing data
training_data_prediction= las_model.predict(x_train)

#R Square Error
error_score= metrics.r2_score(y_train, training_data_prediction)
print("R Square Error: ",error_score)

plt.scatter(y_train, training_data_prediction)
plt.xlabel("Actual Price", color= "Red")
plt.ylabel("Predicted Price", color="Blue")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

#prediction on test data
test_data_prediction= las_model.predict(x_test)

#R Square Error
error_score= metrics.r2_score(y_test, test_data_prediction)
print("R Square Error: ",error_score)

plt.scatter(y_test, test_data_prediction)
plt.xlabel("Actual Price", color= "Red")
plt.ylabel("Predicted Price", color="Blue")
plt.title("Actual Prices vs Predicted Prices")
plt.plot(y_test,'r',test_data_prediction,'b' )
plt.show()

