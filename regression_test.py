from sklearn import linear_model
import pandas as pd
df=pd.read_csv('~/Documents/Econometrics/SLEEP100.csv', delimiter=',')
print df.head(n=5)
reg=linear_model.LinearRegression()
#reg.fit(feature_train, target_train)
#print reg.coef_
#print reg.intercept_
#print reg.score(feature_test, target_test)