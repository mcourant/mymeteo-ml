from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
def handleData(data):
    df = pd.DataFrame(data)
    
    x = df.drop(labels=["tmax", "date", "tmoy"], axis=1)
    y = df["tmin"]
    y = y.astype('int')
    
    print(x)

    print(y)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)

    from sklearn.linear_model import LinearRegression

    reg = LinearRegression()

    reg.fit(x, y)
    
    score = reg.score(x, y)
    print("Score = ", score)
    coef = reg.coef_
    print("Coef = ", coef)
    intercept = reg.intercept_
    print("Intercept = ", intercept)

    predict = reg.predict(np.array([[269,0], [270, 5]]))
    print("Predict = ", predict)
