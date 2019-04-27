import gensim
import self
from konlpy.tag import Okt; okt = Okt()

PROJECT_PATH = '/Users/atec/Desktop/hansol_crawling/'

# --------------------------------------------
#           word2vec
# --------------------------------------------
model = gensim.models.Word2Vec.load(PROJECT_PATH + 'word2vec.model')
print(model.most_similar(positive=['출력']))
print(model.most_similar(positive=['제지','종이'], topn=10))

# --------------------------------------------
#           doc2vec
# --------------------------------------------
