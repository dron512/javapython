import pandas as pd
import matplotlib.pyplot as plt

kisa = pd.read_csv('kisa.csv',encoding="euc-kr")
print(kisa.head())

#print(kisa['종목명'].unique())

x = []
y = []
data = kisa[kisa['종목명']=='전기공사']
x.append('전기공사')
y.append(data.iloc[0,-1])
#print(data)
print('전기 공사 누적 취득자수',data.iloc[0,-1])
data = kisa[kisa['종목명']=='가스']
x.append('가스')
y.append(data.iloc[0,-1])
#print(data)
print('가스 누적 취득자수',data.iloc[0,-1])
data = kisa[kisa['종목명']=='전자계산기']
x.append('전자계산기')
y.append(data.iloc[0,-1])
#print(data)
print('전자계산기 누적 취득자수',data.iloc[0,-1])
data = kisa[kisa['종목명']=='신재생에너지발전설비(태양광)']
#print(data)
x.append('신재생에너지발전설비(태양광)')
y.append(data.iloc[0,-1])
print('신재생에너지발전설비(태양광) 누적 취득자수',data.iloc[0,-1])

data = kisa[kisa['종목명']=='빅데이터분석']
print(data)
print('빅데이터분석 누적 취득자수',data.iloc[0,-1])
x.append('빅데이터분석')
y.append(data.iloc[0,-1])

plt.bar(x,y)
plt.show()