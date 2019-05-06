
# uncomment if gensim is installed
# !pip install gensim
import gensim
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
# --------------------------------------------
#           word2vec
# --------------------------------------------
# model = gensim.models.Word2Vec.load('/Users/atec/Desktop/hansol_crawling/model/word2vec.model')
# print(model.most_similar(positive=['학생']))

# --------------------------------------------
# "Thermal Paper" word2vec
# --------------------------------------------
model = gensim.models.Word2Vec.load('/Users/atec/Desktop/hansol_crawling/model/word2vec_20190503.model')
# print(model.most_similar('paper'))
print(model.most_similar(positive=['thermal', 'paper'], topn=500)) #단어와 가장 가까운 단어
print('=========================1')
#
vocab = list(model.wv.vocab)
X = model[vocab]
print('=========================2')

# 2차원
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)
print('=========================3')

# 100개의 단어에 대해서만 시각화 ------------
X_tsne = tsne.fit_transform(X[:500,:])
df = pd.DataFrame(X_tsne, index=vocab[:500], columns=['x', 'y'])
df.shape
print('=========================4')

# ----------------- 그림 그리기
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df['x'], df['y'])

for word, pos in df.iterrows():
    ax.annotate(word, pos, fontsize=8)
plt.show()
print('=========================5')

# --------------------------------------------
#           doc2vec
# --------------------------------------------
