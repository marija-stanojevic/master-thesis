from gensim import models
from glove import Glove

#find similarities between certain words
words = ['particles', 'collide', 'magnetic', 'statistics', 'bacteria', 'cancer']

#word2vec
titleFiles = ['titleSgHs.txt', 'titleSgNs.txt', 'titleCbowHs.txt', 'titleCbowNs.txt']
abstractFiles = ['abstractSgHs.txt', 'abstractSgNs.txt', 'abstractCbowHs.txt', 'abstractCbowNs.txt']
bothFiles = ['bothSgHs.txt', 'bothSgNs.txt', 'bothCbowHs.txt', 'bothCbowNs.txt']

for i in range(0, len(titleFiles)):
    for word in words:
        modelTitle = models.Word2Vec.load(titleFiles[i])
        modelTitle.wv.most_similar(positive=[word, 'weekness'], negative=['weekness'])
        modelAbstract = models.Word2Vec.load(abstractFiles[i])
        modelAbstract.wv.most_similar(positive=[word, 'weekness'], negative=['weekness'])
        modelBoth = models.Word2Vec.load(bothFiles[i])
        modelBoth.wv.most_similar(positive=[word, 'weekness'], negative=['weekness'])

#doc2vec
titleFiles = ['titlePVDM.txt', 'titlePVDBOW.txt']
abstractFiles = ['abstractPVDM.txt', 'abstractPVDBOW.txt']
bothFiles = ['bothPVDM.txt', 'bothPVDBOW.txt']

for i in range(0, len(titleFiles)):
    for word in words:
        modelTitle = models.Doc2Vec.load(titleFiles[i])
        modelTitle.wv.most_similar(positive=[word, 'weekness'], negative=['weekness'])
        modelAbstract = models.Doc2Vec.load(abstractFiles[i])
        modelAbstract.wv.most_similar(positive=[word, 'weekness'], negative=['weekness'])
        modelBoth = models.Doc2Vec.load(bothFiles[i])
        modelBoth.wv.most_similar(positive=[word, 'weekness'], negative=['weekness'])

#glove
for word in words:
    titleFile = 'titleGlove.txt'
    abstractFile = 'abstractGlove.txt'
    bothFile = 'bothGlove.txt'
    print(word)
    modelTitle = Glove.load(titleFile)
    print(modelTitle.most_similar(word, number=10))
    modelAbstract = Glove.load(abstractFile)
    print(modelAbstract.most_similar(word, number = 10))
    modelBoth = Glove.load(bothFile)
    print(modelBoth.most_similar(word, number = 10))
