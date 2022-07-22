import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv')
data.to_csv('wine.csv')

print(data.head())
print(data.describe())
print(data.info())

wine_data = data[['alcohol', 'sugar', 'pH']].to_numpy()
wine_class = data['class'].to_numpy()

print(wine_data.shape)
print(wine_class.shape)

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target \
    = train_test_split(wine_data, wine_class, test_size=0.2, random_state=42)

print(train_input.shape)
print(test_input.shape)

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

print(train_scaled[:5])
print(train_target[:5])

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_scaled, train_target)

훈련점수 = lr.score(train_scaled, train_target)
테스트점수 = lr.score(test_scaled, test_target)

print(훈련점수)
print(테스트점수)

'''
10.2,2.0,3.57,0.0
11.0,3.6,3.39,0.0
8.8,20.7,3.0,1.0
9.5,1.6,3.3,1.0



'''

mydata = [[10.2, 2.0, 3.57], [11.0, 3.6, 3.39], [8.8, 20.7, 3.0], [9.5, 1.6, 3.3]]
mydata_target = [0, 0, 1, 1]

mydata = ss.transform(mydata)

예측값 = lr.predict(mydata)
print(예측값)
print(mydata_target)

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(max_depth=40, random_state=42)

dt.fit(train_scaled,train_target)

훈련점수 = dt.score(train_scaled,train_target)
테스트점수 = dt.score(test_scaled,test_target)

print(훈련점수)
print(테스트점수)

mydata = [[10.2, 2.0, 3.57], [11.0, 3.6, 3.39], [8.8, 20.7, 3.0], [9.5, 1.6, 3.3]]
mydata_target = [0, 0, 1, 1]

mydata = ss.transform(mydata)

예측값 = dt.predict(mydata)
print(예측값)
print(mydata_target)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10,7))
# plot_tree(dt, max_depth=2, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()







