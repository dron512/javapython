# import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt', delimiter='\t', keep_default_na=False)

# df.to_csv('traing.csv')

import pandas as pd 
import re

trainData=pd.read_csv("traing.csv")
print(trainData[:5])

# 결측값 제거 
# 데이터가 많고 null값 있는 행은 적기 때문에 null 값이 있는 행 전체 제거 
trainData=trainData.dropna()

trainData['document'] = trainData['document'].str.replace("[^가-힣ㄱ-하-ㅣ ]","")
print(trainData[:20])

stopwords = ["하다","한","에","와","자","과","걍","잘","좀","는","의","가","이","은","들"]

# 단어 토큰화 
from konlpy.tag import Okt 
import matplotlib.pyplot as plt 


okt = Okt()
tokenizedData = []

for sent in trainData['document']:
    t = okt.morphs(sent, stem=True) 
    # stem: 어근 추출
    # norm(표준화): 그래욬ㅋㅋ => 그래요
    [w for w in t if w not in stopwords] # for문부터 해석 => if문 => 조건문에 해당하는 w 순서로 해석
    tokenizedData.append(t)