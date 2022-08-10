from turtle import down
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://hong-yp-ml-records.tistory.com/88
plt.style.use("seaborn")
data = pd.read_excel('20220809/carprice.xlsx')

ta = data.groupby('년식').mean()
print(ta)
print(type(ta))
print(ta.columns)
print(ta.index.to_numpy())
# print(ta[ta.iloc(0)])
# x = np.array(data.groupby('년식'))
# print(x)
plt.bar(ta.index.to_numpy()-0.1,ta['가격'].to_numpy(),width=0.1,alpha=0.5 ,label='price')
plt.bar(ta.index.to_numpy(),ta['배기량'].to_numpy(),width=0.1,alpha=0.5,label='cc')
plt.bar(ta.index.to_numpy()+0.1,ta['중량'].to_numpy(),width=0.1,alpha=0.5,label='kg')
plt.xticks(rotation=30)
plt.yticks(rotation=30)
plt.grid()
plt.legend()
plt.show()

yon = ta['연비'].to_numpy()
ma = ta['마력'].to_numpy()
tok = ta['토크'].to_numpy()

plt.bar(ta.index.to_numpy(),yon,width=0.1,alpha=0.8 ,label='yon')
plt.bar(ta.index.to_numpy(),ma,width=0.2,alpha=0.5,label='mar',bottom=yon)
plt.bar(ta.index.to_numpy(),tok,width=0.2,alpha=0.5,label='to',bottom=yon+ma)
plt.grid()
plt.legend()
plt.show()


# x_data = data[['년식', '종류', '연비', '마력', '토크',
#                '연료', '하이브리드', '배기량', '중량', '변속기']].to_numpy()
# print(x_data[:5])
# y_data = data['가격'].to_numpy()
# print(y_data[:5])

# np.savez('carprice.npz', x_data=x_data, y_data=y_data)
