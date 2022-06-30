from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit([[0,1],[1,2],[3,4]],[1,2,3])

predict = lr.predict([[2,3]])
print('predict',predict)