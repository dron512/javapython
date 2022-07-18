import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('chap3.csv')

length = data['length'].to_numpy()
weight = data['weight'].to_numpy()

train_input, test_input, train_target, test_target = \
    train_test_split(length, weight, random_state=42)

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

lr = LinearRegression()
lr.fit(train_input,train_target)

prevalue = lr.predict([[50]])
print(prevalue)
prevalue = lr.predict([[15]])
print(prevalue)

plt.scatter(train_input,train_target)
plt.plot([15,50],[lr.predict([[15]]),lr.predict([[50]])] )
# plt.show()

훈련점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)
print(f"훈련 점수 = {훈련점수}, 테스트 점수 = {테스트점수}")

train_input = np.column_stack((train_input**2,train_input))
print(train_input.shape)
print(train_input[:5])

test_input = np.column_stack((test_input**2,test_input))
lr.fit(train_input,train_target)

훈련점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)
print(f"훈련 점수 = {훈련점수}, 테스트 점수 = {테스트점수}")

x1 = np.arange(15,50)
# print(x1)

x1 = np.column_stack((x1**2,x1))
# print(x1)

predition = lr.predict(x1)
print(x1[:5],predition[:5])

가중치 = lr.coef_

bias = lr.intercept_
print(f'wegiht = {가중치} bias= {bias}')



plt.plot(np.arange(15,50),predition)
plt.show()









