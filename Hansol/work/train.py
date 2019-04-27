
import gensim
from konlpy.tag import Okt; okt = Okt()

PROJECT_PATH = '/Users/atec/Desktop/hansol_crawling/'


# --------------------------------------------
#           word2vec
# --------------------------------------------
model = gensim.models.Word2Vec.load(PROJECT_PATH + 'word2vec.model')
print(model.most_similar(negative=['재활용']))
print(model.most_similar(positive=['재활용']))
# print(model.most_similar(positive=['필기','인쇄'], topn=10))

# --------------------------------------------
#           doc2vec
# --------------------------------------------
