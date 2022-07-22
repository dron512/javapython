import numpy as np

x = np.array([i for i in range(30, 50, 2)])
y = np.array(x ** 2 + x * 1.5 + 5)

x = x.reshape(-1,1)
print(x)
print(y)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x,y)

print('가중치',lr.coef_)
print('절편', lr.intercept_)

예측값 = lr.predict([[49]])
print(예측값)

import matplotlib.pyplot as plt
plt.plot(x[:,0],y)
plt.scatter(49,예측값)
plt.show()
