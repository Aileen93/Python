# ----------- createCorpus before w2v, d2v ---------
# http://blog.theeluwin.kr/post/146591096133/%ED%95%9C%EA%B5%AD%EC%96%B4-word2vec
# --------------------------------------------------
# -*- coding: utf-8 -*-
from konlpy.tag import Okt; okt = Okt()
import re

PROJECT_PATH = '/Users/atec/Desktop/hansol_crawling/trainData/'
target_year = '2018'

def flat(content):
    return ["{}/{}".format(word, tag) for word, tag in okt.pos(content)]

def main():
    str = ''

    rawDataFile = open(PROJECT_PATH + 'rankingNews_org'+target_year+'.txt', 'r', encoding='utf-8') # read file
    newDateFile = open(PROJECT_PATH + 'rankingNews_clean'+target_year+'.txt', 'w', encoding='utf-8')
    # corpusFile  = open(PROJECT_PATH + 'corpus'+target_year+'.txt', 'w', encoding='utf-8')

    lines = rawDataFile.readlines()
    for line in lines:
        str = re.sub('[^가-힝0-9a-zA-Z\\s]', '', line.strip()) # 문장 특수문자 제거 전처리
        newDateFile.write(str+'\n') #정제된 데이타 새로 만들기
        # corpusFile.write(' '.join(flat(str)) + '\n') #Corpus File 만들기

    newDateFile.close()
    # corpusFile.close()

main()