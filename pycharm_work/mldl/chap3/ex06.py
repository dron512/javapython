import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

perch_full = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = perch_full.to_numpy()

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

print(perch_full.shape)
print(perch_weight.shape)

train_input,test_input,train_target,test_target = \
 train_test_split(perch_full,perch_weight,random_state=42)

print(train_input.shape)
print(test_input.shape)
print(train_target.shape)
print(test_target.shape)

print(train_input[0])
print(train_target[0])

lr = LinearRegression()
lr.fit(train_input,train_target)

훈련점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)

print(f'훈련점수 = {훈련점수} 테스트점수 = {테스트점수}')

예측할데이터 = [[19.6,5.14,3.04],[20.4,6.08,3.05]]
예측실제값 = [85,120]
예측값 = lr.predict(예측할데이터)
print(f"예측값 = {예측값}")

예측점수 = lr.score(예측할데이터,예측실제값)
print(f"예측점수 = {예측점수}")

poly = PolynomialFeatures()
poly.fit([[2,3]])
train이삼 = poly.transform([[2,3]])
print(train이삼)
print(poly.get_feature_names())

 














