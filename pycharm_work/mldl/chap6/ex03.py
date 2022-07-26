from sklearn import datasets
import pandas as pd

data = datasets.fetch_california_housing()

print(data.data)
print(data.target)

print(data.data[:5])
print(data.target[:5])
df = pd.DataFrame(data.data, columns=data.feature_names)

print(df.head())
'''
MedInc median income in block 중위 소득
HouseAge median house age in block 평균 주택 연령
AveRooms average number of rooms 평균 객실 수
AveBedrms average number of bedrooms 평균 침실 수
Population block population 인구
AveOccup average house occupancy 평균 주택 점유율
Latitude house block latitude 위도
Longitude house block longitude 경도

'''