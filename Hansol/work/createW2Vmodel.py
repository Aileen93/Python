# -*- coding: utf-8 -*-
import csv
import re
import gensim
from nltk.tokenize import word_tokenize
from nltk import pos_tag

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()

def main():
    i = 0
    try:
        resrultSent = []
        # thermalPaperList(688)
        # 1970s 1980s 1990s 2000s 2010s
        # F_2000_2004s F_2005_2009s F_2010_2014s F_2015_2017s F_2014_2017s
        # 특허카테고리별_원본데이터/A24 A45 A47 A61 A62 A63 All_p
        # 파일 읽기 -----------------------------------------------------

        with open('/Users/atec/Desktop/hansol_crawling/trainData/thermalPaperList(688).csv', encoding='utf-8-sig',
                  newline='') \
                as \
                csvfile:
            reader = csv.reader(csvfile) # DictReader
            for line in reader:
                # doc = row['APPLN_ABSTRACT'] #컬럼 이름으로 가져오기 -- ThermalPaperList(688) 파일만

                # 전처리 1)================
                # 특수문자 제거 전처리
                # =======================
                clean_doc = re.sub('[^0-9a-zA-Z-\\s]', '', line[0])
                clean_doc = clean_doc.replace('<P>','')

                # 전처리 2)================
                # 어간 어미 추출하여 정규화
                # =======================
                clean_doc = lemmatize_sentence(clean_doc)

                # 전처리 3)================
                # 품사 tagging
                # =======================
                # NN: Noun, singular or mass
                # NNS: Noun, plural
                # NNP: Proper noun, singular Phrase
                # NNPS: Proper noun, plural

                # JJ: Adjective
                # JJR: Adjective, comparative
                # JJS: Adjective, superlative

                # VB : VERb, Basic
                # VP : Verb Phrase
                # VBD: Verb, past tense
                # VBG: Verb, gerund or present participle
                # VBN: Verb, past participle
                tokenized_doc = word_tokenize(clean_doc.lower())   # tokenized_doc : ['an', 'image', 'forming']
                tagged_doc = pos_tag(tokenized_doc) # tagged_doc : [('an','DT'), ('image','NN'), ('forming','VBG')]
                sentenceArray = []
                for word in tagged_doc:
                    if word[1] in ('NN', 'NNS', 'NNP', 'NNPS',
                                   'JJ', 'JJR', 'JJS',
                                   'VB', 'VP', 'VBD', 'VBG', 'VBN'):
                        sentenceArray.append(word[0]+'/'+word[1])
                resrultSent.append(sentenceArray)
                i +=1
                print(i)

            # model 만들기 -----------------------------------------------------
            print(resrultSent)
            print('====== word2vec 모델 만들기 시작 ======')
            model = gensim.models.Word2Vec(resrultSent, iter=10, min_count=5, size=300)
            model.init_sims(replace=True) #학습 완료 후, 필요없는 메모리 unload
            model.save('/Users/atec/Desktop/hansol_crawling/model/w2v_thermalPaperList(688).model')
            print('====== word2vec 모델 생성 완료 ======')

            # word2vec 실행 -----------------------------------------------------
            # train.py로 이동

    except KeyError:
        print("not in vocabulary")



def nltk2wn_tag(nltk_tag):
  if nltk_tag.startswith('J'):
    return wordnet.ADJ
  elif nltk_tag.startswith('V'):
    return wordnet.VERB
  elif nltk_tag.startswith('N'):
    return wordnet.NOUN
  elif nltk_tag.startswith('R'):
    return wordnet.ADV
  else:
    return None

def lemmatize_sentence(sentence):
  nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
  wn_tagged = map(lambda x: (x[0], nltk2wn_tag(x[1])), nltk_tagged)
  res_words = []
  for word, tag in wn_tagged:
    if tag is None:
      res_words.append(word)
    else:
      res_words.append(lemmatizer.lemmatize(word, tag))
  return " ".join(res_words)

main()