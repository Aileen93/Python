# -*- coding: utf-8 -*-
import csv
import re
import gensim
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from datetime import datetime

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
        # ThermalPaperList(688)
        # 1970s 1980s 1990s 2000s 2010s
        # 파일 읽기 -----------------------------------------------------

        with open('/Users/atec/Desktop/hansol_crawling/trainData/2010s.csv', encoding='utf-8-sig', newline='') as csvfile:
            reader = csv.reader(csvfile) # DictReader
            for line in reader:
                # doc = row['APPLN_ABSTRACT'] #컬럼 이름으로 가져오기 -- ThermalPaperList(688) 파일만
                clean_doc = re.sub('[^0-9a-zA-Z\\s]', '', line[0])  # 문장 특수문자 제거 전처리

                # CC: Coordinating conjunction
                # CD: Cardinal number
                # DT: Determiner
                # EX: Existential there
                # FW: Foreign word
                # IN: Preposition or subordinating conjunction
                # JJ: Adjective
                # VP: Verb Phrase
                # JJR: Adjective, comparative
                # JJS: Adjective, superlative
                # LS: List item marker
                # MD: Modal
                # NN: Noun, singular or mass
                # NNS: Noun, plural
                # PP: Preposition Phrase
                # NNP: Proper noun, singular Phrase
                # NNPS: Proper noun, plural
                # PDT: Pre determiner
                # POS: Possessive ending
                # PRP: Personal pronoun Phrase
                # PRP: Possessive pronoun Phrase
                # RB: Adverb
                # RBR: Adverb, comparative
                # RBS: Adverb, superlative
                # RP: Particle
                # S: Simple declarative clause
                # SBAR: Clause introduced by a(possibly empty) subordinating conjunction
                # SBARQ: Direct question introduced by a wh - word or a wh - phrase.
                # SINV: Inverted declarative sentence, i.e.one in which the subject follows the tensed verb or modal.
                # SQ: Inverted yes / no question, or main clause of a wh - question, following the wh - phrase in SBARQ.
                # SYM: Symbol
                # VBD: Verb, past tense
                # VBG: Verb, gerund or present participle
                # VBN: Verb, past participle
                # VBP: Verb, non - 3rd person singular present
                # VBZ: Verb, 3rd person singular present
                # WDT: Wh - determiner
                # WP: Wh - pronoun
                # WP: Possessive wh - pronoun
                # WRB: Wh - adverb
                tokenized_doc = word_tokenize(clean_doc.lower())   # tokenized_doc : ['an', 'image', 'forming']
                tagged_doc = pos_tag(tokenized_doc) # tagged_doc : [('an','DT'), ('image','NN'), ('forming','VBG')]
                sentenceArray = []
                for word in tagged_doc:
                    if word[1][0] not in ('C','D','I','V','J','L','M','R','W'): #org
                    # if word[1] in ('NN','NNS','NNP','NNPS','SYM','FW'): new
                        sentenceArray.append(word[0])
                resrultSent.append(sentenceArray)
                i +=1
                print(i)

            # model 만들기 -----------------------------------------------------
            print(resrultSent)
            print(datetime.now())
            print('====== word2vec 모델 만들기 시작 ======')
            model = gensim.models.Word2Vec(resrultSent, iter=10, min_count=1, size=300)
            model.save('/Users/atec/Desktop/hansol_crawling/model/w2v_2010s.model')
            model.init_sims(replace=True) #학습 완료 후, 필요없는 메모리 unload
            print('====== word2vec 모델 생성 완료 ======')
            print(datetime.now())

            # word2vec 실행 -----------------------------------------------------
            # train.py로 이동

    except KeyError:
        print("not in vocabulary")

main()