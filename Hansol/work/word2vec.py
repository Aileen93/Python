# ----------- word2vec ---------
# http://blog.theeluwin.kr/post/146591096133/%ED%95%9C%EA%B5%AD%EC%96%B4-word2vec
# ------------------------------
# -*- coding: utf-8 -*-
import gensim
from konlpy.tag import Okt; okt = Okt()
# config = {
#     'min_count': 1,  # 등장 횟수가 5 이하인 단어는 무시
#     'size': 300,  # 300차원짜리 벡터스페이스에 embedding
#     'sg': 1,  # 0이면 CBOW, 1이면 skip-gram을 사용한다
#     'batch_words': 10000,  # 사전을 구축할때 한번에 읽을 단어 수
#     'iter': 10,  # 보통 딥러닝에서 말하는 epoch과 비슷한, 반복 횟수
#     'workers': multiprocessing.cpu_count(),
# }
# model = gensim.models.Word2Vec(**config)

PROJECT_PATH = '/Users/atec/Desktop/hansol_crawling/'
CLEAN_TITLE_FILE = 'cleanRankingNews_merge.txt'
# CORPUS_FILE = 'corpus.txt'

def main():
    try:
        cleanData = open(PROJECT_PATH + CLEAN_TITLE_FILE, 'r')  # read file
        sentenceArray = []
        for sent in cleanData:
            #['불법', '차로', '안전', '센터', '마비', '새해', '첫날', '양심', '불량']
            tokens_sent = okt.nouns(sent.replace('\n',''))  #명사만 가지고 실행한 결과
            for x in tokens_sent:
                if len(x) > 1:
                    sentenceArray.append(tokens_sent)

        # corpusData = open(PROJECT_PATH + CORPUS_FILE, 'r')  # read file
        # corpusArry = []
        # for cor in corpusData:
        #     corpusArry.append(cor.split())

        # model 만들기 -----------------------------------------------------
        model = gensim.models.Word2Vec(sentenceArray, iter=10, min_count=1, size=300)
        # model.build_vocab(sentences=sentenceArray)
        # model.train(sentenceArray, epochs=model.epochs, total_examples=model.corpus_count, total_words=model.corpus_total_words)
        model.save(PROJECT_PATH+'word2vec.model')

        # word2vec 실행 -----------------------------------------------------
        # train.py로 이동

    except KeyError:
        print("not in vocabulary")

main()