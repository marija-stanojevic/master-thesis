import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from gensim import models
from glove import Glove

#word2vec
files = ['titleSgHs.txt', 'titleSgNs.txt', 'titleCbowHs.txt', 'titleCbowNs.txt']
headers = []
word = 'bacteria'
for file in files:
    model = models.Word2Vec.load(file)
    words = []
    tuples = model.wv.most_similar(positive=[word, 'weakness'], negative=['weakness'], topn=100)
    for tuple in tuples:
        words.append(tuple[0])
    with open('tsne' + file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            if i == 0:
                headers = row
            elif i == 1:
                x = row
            else:
                y = row
            i += 1
    i=-1
    cleanHeaders = []
    for txt in headers:
        i += 1
        if txt.isalpha() and txt in words:
            cleanHeaders.append(txt)
        else:
            x.pop(i)
            y.pop(i)
            i -= 1
    matplotlib.rcParams.update({'font.size':6})
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x, y, s=5)
    for i,txt in enumerate(cleanHeaders):
        ax.annotate(txt, (float(x[i]) + 0.1, float(y[i])))
    plt.savefig(word + 'Visualisation' + file + '.png', dpi=900)

#glove
files = ['titleGlove.txt']
headers = []
word = ''
for file in files:
    model = Glove.load(file)
    words = []
    tuples = model.most_similar(word, number=100)
    for tuple in tuples:
        words.append(tuple[0])
    with open('tsne' + file, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            if i == 0:
                headers = row
            elif i == 1:
                x = row
            else:
                y = row
            i += 1
    i=-1
    cleanHeaders = []
    for txt in headers:
        i += 1
        if txt.isalpha(): # and txt in words:
            cleanHeaders.append(txt)
        else:
            x.pop(i)
            y.pop(i)
            i -= 1
    matplotlib.rcParams.update({'font.size':6})
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x, y, s=5)
    for i,txt in enumerate(cleanHeaders):
        ax.annotate(txt, (float(x[i]) + 0.1, float(y[i])))
    plt.savefig(word + 'Visualisation' + file + '.png', dpi=900)
