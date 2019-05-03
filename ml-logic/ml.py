from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def handleData(data):
      df = pd.DataFrame(data)

      # x = df.drop(labels="tmin", axis=1)
      x = df.drop(labels=["tmax", "date", "tmoy", "tmin"], axis=1)
      y = df.drop(labels=["dayInYear", "date"], axis=1)
      y = y.astype('int')

      X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

      X_train.head()

      model = LinearRegression()

      model.fit(X_train, y_train)
      score = model.score(x, y)
      print("Score = ", score)
      coef = model.coef_
      print("Coef = ", coef)
      intercept = model.intercept_
      print("Intercept = ", intercept)

      predict = model.predict(np.array([[166], [270]]))

      print("-----------------------------------")
      print("Result")
      print("-----------------------------------")
      # r2 = r2_score(y_train, predict)
      print("                   TEMPMAX     / TEMPMIN  / TEMPMOY")
      print("Predict day 166 = ", predict[0])
      print("                   TEMPMAX     / TEMPMIN  / TEMPMOY")
      print("Predict day 270 = ", predict[1])