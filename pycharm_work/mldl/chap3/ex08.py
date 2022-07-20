import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from scipy.special import expit
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv('https://bit.ly/fish_csv_data')
# data.to_excel('fish_data.xlsx')
print(data.head())

fish_data = data[['Weight','Length','Diagonal','Height','Width']].to_numpy()
print(fish_data[:5])
fish_target = data['Species'].to_numpy()
print(fish_target[:5])

train_input,test_input,train_target,test_target \
    = train_test_split(fish_data,fish_target,random_state=42)

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

print(train_scaled[:5])
print(train_target[:5])
print(test_scaled[:5])
print(test_target[:5])

knclf = KNeighborsClassifier(n_neighbors=3)
knclf.fit(train_scaled,train_target)

예측값 = knclf.predict(test_scaled)
print(예측값[:5])
print(test_target[:5])

pre = [[242.,25.4, 30., 11.52, 4.02],[ 363., 29., 33.5, 12.73, 4.4555]]
pre_scaled = ss.transform(pre)

print(pre_scaled)
pre_value = knclf.predict(pre_scaled)
print(pre_value)

score = knclf.score(test_scaled,test_target)
print(score)

z = np.arange(-5,5,0.1)
phi = 1 / (1+np.exp(-z))
print(z)
print(phi)

plt.plot(z,phi)
plt.show()

indexs = (train_target=='Bream')|(train_target=='Smelt')
print(indexs)
도미빙어데이터=train_scaled[indexs]
도미빙어타겟=train_target[indexs]

print(도미빙어데이터.shape)
print(도미빙어타겟.shape)

lr = LogisticRegression()
lr.fit(도미빙어데이터,도미빙어타겟)

score = lr.score(도미빙어데이터,도미빙어타겟)
print(score)

indexs = (test_target=='Bream')|(test_target=='Smelt')
도미빙어데이터=test_scaled[indexs]
도미빙어타겟=test_target[indexs]

score = lr.score(도미빙어데이터,도미빙어타겟)
print(score)

pre = [[242.,25.4, 30., 11.52, 4.02],[ 363., 29., 33.5, 12.73, 4.4555]]
pre_scaled = ss.transform(pre)

pre_value = lr.predict(pre_scaled)
print(pre_value)

z = lr.decision_function(도미빙어데이터)
print(z)

phi = 1/(1+np.exp(-z))
print(phi)

phi = expit(z)
print(phi)

훈련데이터점수리스트 = []
테스트데이터점수리스트 = []

for i in range(1,100):
    lr = LogisticRegression(C=i,max_iter=1000)
    lr.fit(train_scaled,train_target)

    훈련데이터점수 = lr.score(train_scaled,train_target)
    테스트데이터점수 = lr.score(test_scaled,test_target)

    훈련데이터점수리스트.append(훈련데이터점수)
    테스트데이터점수리스트.append(테스트데이터점수)

print(훈련데이터점수리스트)
print(테스트데이터점수리스트)
print(np.argmax(훈련데이터점수리스트))
print(np.argmax(테스트데이터점수리스트))

plt.plot(range(1,100),훈련데이터점수리스트)
plt.plot(range(1,100),테스트데이터점수리스트)
plt.show()

# Whitefish,
pre = [[242.,25.4, 30., 11.52, 4.02],
       [ 363., 29., 33.5, 12.73, 4.4555],
       [1000,40,43.5,12.354,6.525]]
pre_scaled = ss.transform(pre)

pre_value = lr.predict(pre_scaled)
print(pre_value)


lgb = RandomForestClassifier()
lgb.fit(train_scaled,train_target)

훈련데이터점수 = lgb.score(train_scaled,train_target)
테스트데이터점수 = lgb.score(test_scaled,test_target)

print(훈련데이터점수)
print(테스트데이터점수)

pre = [[242.,25.4, 30., 11.52, 4.02],
       [ 363., 29., 33.5, 12.73, 4.4555],
       [1000,40,43.5,12.354,6.525]]
pre_scaled = ss.transform(pre)

pre_value = lgb.predict(pre_scaled)
print(pre_value)




