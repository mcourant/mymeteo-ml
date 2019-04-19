from sklearn.model_selection import train_test_split
import pandas as pd

def handleData(data):
    df = pd.DataFrame(data)
    
    # x = df.drop(labels="tmin", axis=1)
    x = df.drop(labels=["tmax", "date", "tmoy"], axis=1)
    y = df["tmin"]
    y = y.astype('int')

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    X_train.head()

    from sklearn.ensemble import RandomForestRegressor
    from sklearn.linear_model import LogisticRegression


    model = LogisticRegression(random_state=0, solver='lbfgs')

    # y_train = y_train.astype('int')

    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)

    model.predict_proba(X_test)

    print(model.score(x, y))