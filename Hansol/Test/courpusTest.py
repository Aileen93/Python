# ----------- createCorpus before w2v, d2v ---------
# http://blog.theeluwin.kr/post/146591096133/%ED%95%9C%EA%B5%AD%EC%96%B4-word2vec
# --------------------------------------------------
# -*- coding: utf-8 -*-
import codecs
from konlpy.tag import Okt; okt = Okt()
import re

PROJECT_PATH = '/Users/atec/Desktop/hansol_crawling/'
READ_FILE = 'ranking_news_title.txt'
CLEAN_TITLE_FILE = 'ranking_news_new.txt'
CORPUS_FILE = 'corpus.txt'


def main():
    str = ''

    rawDataFile = open(PROJECT_PATH + READ_FILE, 'r') # read file

    lines = rawDataFile.readlines()
    for line in lines:
        str = re.sub('[^가-힝0-9a-zA-Z\\s]', '', line.strip()) # 문장 특수문자 제거 전처리
        print(okt.pos(str))

    rawDataFile.close()

main()
