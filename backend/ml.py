# 1. ---Create your machine learning model---#

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


df = pd.read_csv("integration.csv")
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
x = cdf.iloc[:, :3]
y = cdf.iloc[:, -1]
regressor = LinearRegression()
regressor.fit(x,y)
pickle.dump(regressor, open('model.pkl','wb'))
# model = pickle.load(open('model.pkl','rb'))
# print(model.predict([[2.6, 8, 10.1]]))
