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

CLEAN_TITLE_FILE = 'cleanRankingNews_merge.txt'

# CORPUS_FILE = 'corpus.txt'

def main():
    try:
        cleanData = open('/Users/atec/Desktop/hansol_crawling/trainData/' + CLEAN_TITLE_FILE, 'r')  # read file
        sentenceArray = []
        for sent in cleanData:
            tokens_sent = okt.nouns(sent)
            # sent :국민 10명 중 23명 1년간 여행 한번 못했다
            # tokens_sent :['국민', '명', '중', '명', '여행', '한번']
            for x in tokens_sent:
                if len(x) > 1:
                    # ['국민', '명', '중', '명', '여행', '한번']
                    sentenceArray.append(tokens_sent)
                    print('=============================')
                    print(sentenceArray)


        # model 만들기 -----------------------------------------------------
        model = gensim.models.Word2Vec(sentenceArray, iter=10, min_count=1, size=300)
        # model.build_vocab(sentences=sentenceArray)
        # model.train(sentenceArray, epochs=model.epochs, total_examples=model.corpus_count, total_words=model.corpus_total_words)
        model.save('/Users/atec/Desktop/hansol_crawling/model/word2vec.model')

        # word2vec 실행 -----------------------------------------------------
        # train.py로 이동
        print('word2vec model 생성 완료')

    except KeyError:
        print("not in vocabulary")

main()