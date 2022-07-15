import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('chap3.csv')
print(data.head())

length = data['length'].to_numpy()
weight = data['weight'].to_numpy()

train_input, test_input, train_target, test_target = train_test_split(length, weight, random_state=42)
print(train_input.shape)
print(test_input.shape)

train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

print(train_input.shape)
print(test_input.shape)

maelist = []
for i in range(1,20):
    knr = KNeighborsRegressor(n_neighbors=i)
    knr.fit(train_input, train_target)

#    score = knr.score(test_input, test_target)
    predict_target = knr.predict(test_input)

    mae = mean_absolute_error(test_target, predict_target)
    maelist.append((i,mae))

print(maelist)
'''
    학습을 진행할껀데 이웃되는 좌표를 3일때와 좌표가 5일때 
    스코어 값이랑 오차값을 확인을 해보도록겠습니다
'''

knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(train_input,train_target)
훈련점수 = knr.score(train_input,train_target)
테스트점수 = knr.score(test_input,test_target)
prediction = knr.predict(test_input)
mae = mean_absolute_error(test_target,prediction)
print('-----------3-----------')
print('훈련점수',훈련점수)
print('테스트점수',테스트점수)
print('오차',mae)

knr = KNeighborsRegressor(n_neighbors=5)
knr.fit(train_input,train_target)
훈련점수 = knr.score(train_input,train_target)
테스트점수 = knr.score(test_input,test_target)
prediction = knr.predict(test_input)
mae = mean_absolute_error(test_target,prediction)
print('-----------5-----------')
print('훈련점수',훈련점수)
print('테스트점수',테스트점수)
print('오차',mae)

x = np.arange(4,50).reshape(-1,1)

for i in [1,5,10]:
    knr = KNeighborsRegressor(n_neighbors=i)
    knr.fit(train_input,train_target)
    prediction = knr.predict(x)

    plt.scatter(length, weight)
    plt.plot(x,prediction,c="#555500")
    plt.title(f"이웃되는점 {i}개일때 그래프")
    plt.xlabel('길이')
    plt.ylabel('무게')
    plt.show()
