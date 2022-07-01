import pandas
from sklearn.linear_model import LogisticRegression

inputdata= [[1,2],[1,3],[3,5],[3,6]]
inputvalue = ['A','A','B','B']

lr = LogisticRegression()
lr.fit(inputdata,inputvalue)

prevalue = lr.predict([[1,1.5]])

print(prevalue)

prevalue = lr.predict([[3,3.5]])

print(prevalue)

