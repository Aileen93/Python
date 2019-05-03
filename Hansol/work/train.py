import gensim
from konlpy.tag import Okt; okt = Okt()

# --------------------------------------------
#           word2vec
# --------------------------------------------
# model = gensim.models.Word2Vec.load('/Users/atec/Desktop/hansol_crawling/model/word2vec.model')
# print(model.most_similar(positive=['학생']))


# --------------------------------------------
# "Thermal Paper" word2vec
# --------------------------------------------
model = gensim.models.Word2Vec.load('/Users/atec/Desktop/hansol_crawling/model/word2vec20190503.model')
print(model.most_similar('paper'))
print(model.most_similar(positive=['student'], topn=20))


# --------------------------------------------
#           doc2vec
# --------------------------------------------
