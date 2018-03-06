from gensim import models
import csv
from glove import Glove

#Extract vocabulars (vectors for each word)
files = ['titleSgHs.txt', 'titleSgNs.txt', 'titleCbowHs.txt', 'titleCbowNs.txt',
              'abstractSgHs.txt', 'abstractSgNs.txt', 'abstractCbowHs.txt', 'abstractCbowNs.txt',
              'bothSgHs.txt', 'bothSgNs.txt', 'bothCbowHs.txt', 'bothCbowNs.txt']
for file in files:
    model = models.Word2Vec.load(file)
    with open('vocabular' + file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for word in model.wv.vocab:
            datarow = model.wv[word].tolist()
            datarow.insert(0, word)
            writer.writerow(datarow)

files = ['titleGlove.txt', 'abstractGlove.txt', 'bothGlove.txt']
for file in files:
    model = Glove.load(file)
    with open('vocabular' + file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(0,len(model.dictionary)):
            word = model.dictionary.keys()[i]
            datarow = model.word_vectors[i].tolist()
            datarow.insert(0,word)
            writer.writerow(datarow)