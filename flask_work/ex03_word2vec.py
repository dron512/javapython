import gensim
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
#Window 의 한글 폰트 설정
#plt.rc('font', family='Malgun Gothic')
#Mac 의 한글 폰트 설정
plt.rc('font', family='AppleGothic')
import seaborn as sns
import numpy as np

##########모델 로드

model = gensim.models.Word2Vec.load('/Users/mac/Downloads/ko/ko.bin')
#print(model.wv.vectors.shape) #(30185, 200)

##########모델 예측

words = np.array(['사과', '배', '복숭아', '집', '아파트', '컴퓨터', '책', '마우스',
        '책상', '의자', '지하철'])

vectors = []
for i, word in enumerate(words):
    if word in model:
        vectors.append(model[word])
    else:
        del words[i]

similarity = cosine_similarity(vectors, vectors)
print(similarity.shape) #(11, 11)

sns.heatmap(similarity, xticklabels=words, yticklabels=words, cmap='viridis')
plt.show()