from konlpy.corpus import kobill    # Docs from pokr.kr/bill
files_ko = kobill.fileids()         # Get file ids
doc_ko = kobill.open('news.txt').read()

from konlpy.tag import Twitter; t = Twitter()
tokens_ko = t.morphs(doc_ko)

import nltk
ko = nltk.Text(tokens_ko, name='뉴스')   # 이름

print(len(ko.tokens))       # returns number of tokens (document length)
print(len(set(ko.tokens)))  # returns number of unique tokens
ko.vocab()                  # returns frequency distribution

print(ko.count(str('메르스')))

ko.similar('메르스') #유사어 찾기

#10.1 형태소 분석기(POS tagging)
from konlpy.tag import Twitter; t = Twitter()
tags_ko = t.pos('작고 노란 강아지가 고양이에게 짖었다')
print(tags_ko)