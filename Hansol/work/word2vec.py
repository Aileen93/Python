# ----------- word2vec ---------
# http://blog.theeluwin.kr/post/146591096133/%ED%95%9C%EA%B5%AD%EC%96%B4-word2vec
# ------------------------------
# -*- coding: utf-8 -*-
import codecs
import gensim
import multiprocessing
#
# config = {
#     'min_count': 1,  # 등장 횟수가 5 이하인 단어는 무시
#     'size': 300,  # 300차원짜리 벡터스페이스에 embedding
#     'sg': 1,  # 0이면 CBOW, 1이면 skip-gram을 사용한다
#     'batch_words': 10000,  # 사전을 구축할때 한번에 읽을 단어 수
#     'iter': 10,  # 보통 딥러닝에서 말하는 epoch과 비슷한, 반복 횟수
#     'workers': multiprocessing.cpu_count(),
# }
# model = gensim.models.Word2Vec(**config)
import self

PROJECT_PATH = '/Users/atec/Desktop/hansol_crawling/'
CLEAN_TITLE_FILE = 'ranking_news_new.txt'
CORPUS_FILE = 'corpus.txt'

class SentenceReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        for line in codecs.open(self.filepath, encoding='utf-8'):
            yield line.split(' ')


def main():

    try:
        cleanData = open(PROJECT_PATH + CLEAN_TITLE_FILE, 'r')  # read file
        sentenceArray = []
        for sent in cleanData :
            # clean_title = [i.replace("\'", '').replace(' ', '') for i in sent if i != ""]
            sentenceArray.append(sent.split())

        corpusData = open(PROJECT_PATH + CORPUS_FILE, 'r')  # read file
        corpusArry = []
        for cor in corpusData:
            corpusArry.append(cor.split())

        sentences_vocab = SentenceReader(PROJECT_PATH+CORPUS_FILE)
        sentences_train = SentenceReader(PROJECT_PATH+CLEAN_TITLE_FILE)

        # print(sentenceArray[0])
        # print(len(sentenceArray))
        # print(corpusArry[0])

        # model 만들기 -----------------------------------------------------
        model = gensim.models.Word2Vec()
        model.build_vocab(sentences=sentenceArray)
        model.train(corpusArry, epochs=model.epochs, total_examples=model.corpus_count, total_words=model.corpus_total_words)
        model.save('model')

        # word2vec 실행 -----------------------------------------------------
        model = gensim.models.Word2Vec.load('model')
        print(model.most_similar(positive=["날씨"], topn=20))

    except KeyError:
        print("not in vocabulary")

main()