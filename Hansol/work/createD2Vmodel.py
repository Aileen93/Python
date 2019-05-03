# -*- coding: utf-8 -*-
import csv
import ssl
import nltk
import re
import gensim
from nltk.tokenize import word_tokenize
from nltk import pos_tag

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
        sentenceArray = []
        #ThermalPaperList_org(1464693)-1
        # 파일 읽기 -----------------------------------------------------
        with open('/Users/atec/Desktop/hansol_crawling/trainData/ThermalPaperList(688).csv', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                doc = row['APPLN_ABSTRACT'] #컬럼 이름으로 가져오기
                clean_doc = re.sub('[^0-9a-zA-Z\\s]', '', doc.strip())  # 문장 특수문자 제거 전처리
                tagged_doc = pos_tag(word_tokenize(clean_doc.lower()))

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
                for t in tagged_doc:
                    sentenceArray.append([t])
                i+=1
                print(i)

            # model 만들기 -----------------------------------------------------
            model = gensim.models.Doc2Vec(doc, vector_size=5, window=2, min_count=1, workers=4)
            model.save('/Users/atec/Desktop/hansol_crawling/model/doc2vec20190503.model')

            # doc2vec 실행 -----------------------------------------------------
            # train.py로 이동
            print('====== doc2vec 모델 생성 완료 ======')

    except KeyError:
        print("not in vocabulary")

main()