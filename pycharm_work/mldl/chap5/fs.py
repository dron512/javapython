import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

train_df = pd.read_excel('fs.xlsx', sheet_name='train')
test_df = pd.read_excel('fs.xlsx', sheet_name='test')

print(train_df.head())
print(test_df.head())

train_input = train_df[['Father']].to_numpy()
train_target = train_df['Son'].to_numpy()

test_input = test_df[['Father']].to_numpy()
test_target = test_df['Son'].to_numpy()

lr = LinearRegression()
lr.fit(train_input,train_target)

훈련점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)

print(훈련점수)
print(테스트점수)

pred = lr.predict([[160]])
print('예측키 = ',pred)

lr = DecisionTreeRegressor()
lr.fit(train_input,train_target)

훈련점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)

print(훈련점수)
print(테스트점수)

pred = lr.predict([[160]])
print('예측키 = ',pred)

lr = RandomForestRegressor()
lr.fit(train_input,train_target)

훈련점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)

print(훈련점수)
print(테스트점수)

pred = lr.predict([[170]])
print('예측키 = ',pred)

prediction = lr.predict(train_input[:30])

plt.scatter(train_input,train_target)
plt.plot(train_input[:30],prediction,c='#ff0000')
plt.xlabel('father')
plt.ylabel('son')
plt.show()