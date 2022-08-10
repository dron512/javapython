import gensim
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns

##########모델 로드

model = gensim.models.KeyedVectors.load_word2vec_format('/Users/mac/Downloads/GoogleNews-vectors-negative300.bin', binary=True) 
#print(model.vectors.shape) #(3000000, 300) 

##########모델 예측

words = np.array(['coffee', 'tea', 'beer', 'wine', 'brandy', 'rum', 'champagne', 'water'])

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