from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def test_all_regressor(x_train, y_train, x_test, y_test):

    if x_train == None:
        raise Exception("x_train value missing")
    if y_train == None:
        raise Exception("y_train value missing")
    if x_test == None:
        raise Exception("x_test value missing")
    if y_test == None:
        raise Exception("y_test value missing")

    sc_x = StandardScaler()
    sc_y = StandardScaler()
    x_train_fs = sc_x.fit_transform(x_train)
    y_train_fs = sc_y.fit_transform(y_train)

    # multiple linear regression
    mlr = LinearRegression()
    mlr.fit(x_train, y_train)
    y_pred_multi = mlr.predict(x_test)

    # polynomial linear regression
    pf = PolynomialFeatures(degree=4)
    x_poly = pf.fit_transform(x_train)
    x_poly_test = pf.transform(x_test)
    plr = LinearRegression()
    plr.fit(x_poly, y_train)
    y_pred_poly = plr.predict(x_poly_test)

    # support vector linear regression
    regressor = SVR(kernel='rbf')
    regressor.fit(x_train_fs, y_train_fs)
    y_pred_sr = sc_y.inverse_transform(
        regressor.predict(sc_x.transform(x_test)))

    # decision tree regression
    dt = DecisionTreeRegressor(random_state=0)
    dt.fit(x_train, y_train)
    y_pred_dt = dt.predict(x_test)

    # random forest regression
    rf = RandomForestRegressor(n_estimators=10, random_state=0)
    rf.fit(x_train, y_train)
    y_pred_rf = rf.predict(x_test)

    # r2 score
    print("multi :"+str(r2_score(y_test, y_pred_multi)))
    print("poly :"+str(r2_score(y_test, y_pred_poly)))
    print("support vector :"+str(r2_score(y_test, y_pred_sr)))
    print("decision tree :"+str(r2_score(y_test, y_pred_dt)))
    print("random forest :"+str(r2_score(y_test, y_pred_rf)))


def test_all_classifires():
    print()
