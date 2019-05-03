from nltk.tokenize import word_tokenize
from nltk import pos_tag

print("Hello, Hansol!")

resrultSent = []
try:
    list = ["A thermal scale radio frequency identification (RFID) label is described which includes a top layer, a bottom layer and a middle layer glued together to form a label body. The top layer is of thermal paper. The middle layer is an RFID antenna on polyester paper. The RFID antenna has a thickness in the range of 30-60um and covers an area of at least 57 x 49mm. The label body has a thickness in a range of 40-75 lbs.", "school is good"]
    for doc in list:
        tokenized_doc = word_tokenize(doc.lower())   # tokenized_doc : ['an', 'image', 'forming']
        tagged_doc = pos_tag(tokenized_doc) # tagged_doc : [('an','DT'), ('image','NN'), ('forming','VBG')]

        sentenceArray = []
        for word in tagged_doc:
            if word[1][0] == "N" or word[1][0] == "V":
                sentenceArray.append(word[0])
        resrultSent.append(sentenceArray)
    print('------------------ S')
    print(resrultSent)
    print('------------------ E')


except KeyError:
    print("not in vocabulary")