import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

data = pd.read_csv('chap3.csv')

length = data['length'].to_numpy()
weight = data['weight'].to_numpy()

train_input, test_input, train_target, test_target = \
    train_test_split(length, weight, random_state=42)

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(train_input, train_target)

prevalue = knr.predict([[50]])
print(prevalue)
prevalue = knr.predict([[100]])
print(prevalue)

dis, inx = knr.kneighbors([[50]])
print(inx)

trainvalues = train_input[inx], train_target[inx]
print(trainvalues)

plt.scatter(train_input, train_target)
plt.scatter(50, 1033, marker='^')
plt.scatter(100, 1033, marker='D')
plt.scatter(train_input[inx],train_target[inx],marker='*')
plt.show()
