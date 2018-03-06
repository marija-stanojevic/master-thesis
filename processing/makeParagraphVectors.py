from gensim import models
import csv
from glove import Glove

#save titles and abstracts as vectors
#word2vec
filename = 'C:/Users/Marija/PyCharmProjects/scraping/arxivData '
titleFiles = ['titleSgHs.txt', 'titleSgNs.txt', 'titleCbowHs.txt', 'titleCbowNs.txt']
abstractFiles = ['abstractSgHs.txt', 'abstractSgNs.txt', 'abstractCbowHs.txt', 'abstractCbowNs.txt']
bothFiles = ['bothSgHs.txt', 'bothSgNs.txt', 'bothCbowHs.txt', 'bothCbowNs.txt']

for i in range(0, len(titleFiles)):
    year1 = 2007
    year2 = 2008
    data = []
    print(titleFiles[i])
    modelTitle = models.Word2Vec.load(titleFiles[i])
    modelAbstract = models.Word2Vec.load(abstractFiles[i])
    modelBoth = models.Word2Vec.load(bothFiles[i])
    while year2 < 2018:
        with open(filename + str(year1) + '-' + str(year2) + '.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
            for row in reader:
                # Titles only
                title = (row[0][2:len(row[0]) - 1]).replace('\\n', ' ').replace('.', '').replace(',', '').replace(':', '').replace(')','').replace('(','').lower().split(' ')
                titleVector = [0] * 100
                for word in title:
                    titleVector += modelTitle.wv[word]
                # Abstracts only
                abstract = (row[2][2:len(row[2]) - 1]).replace('\\n', ' ').replace('.', '').replace(',', '').replace(':', '').replace(')','').replace('(','').lower().split(' ')
                abstractVector = [0] * 100
                for word in abstract:
                    abstractVector += modelAbstract.wv[word]
                # Abstracts and titles
                both = (row[2][2:len(row[2]) - 1]).replace('\\n', ' ').replace('.', '').replace(',','').replace(':', '').replace(')', '').replace('(', '').lower().split(' ')
                bothVector = [0] * 100
                for word in both:
                    bothVector += modelBoth.wv[word]
                datarow = [row[1], titleVector, abstractVector, bothVector]
                data.append(datarow)
        year1 += 1
        year2 += 1
    with open('vectors' + titleFiles[i], 'wb') as wrfile:
        writer = csv.writer(wrfile)
        writer.writerows(data)

#glove
titleFile = 'titleGlove.txt'
abstractFile = 'abstractGlove.txt'
bothFile = 'bothGlove.txt'
year1 = 2007
year2 = 2008
data = []
print(titleFile)
modelTitle = Glove.load(titleFile)
modelAbstract = Glove.load(abstractFile)
modelBoth = Glove.load(bothFile)
while year2 < 2018:
    with open(filename + str(year1) + '-' + str(year2) + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:
            # Titles only
            title = (row[0][2:len(row[0]) - 1]).replace('\\n', ' ').replace('.', '').replace(',', '').replace(':','').replace(')', '').replace('(', '').lower().split(' ')
            titleVector = [0] * 100
            for word in title:
                titleVector += modelTitle.word_vectors[modelTitle.dictionary.keys().index(word)]
            # Abstracts only
            abstract = (row[2][2:len(row[2]) - 1]).replace('\\n', ' ').replace('.', '').replace(',', '').replace(':', '').replace(')', '').replace('(', '').lower().split(' ')
            abstractVector = [0] * 100
            for word in abstract:
                abstractVector += modelAbstract.word_vectors[modelAbstract.dictionary.keys().index(word)]
            # Abstracts and titles
            both = (row[2][2:len(row[2]) - 1]).replace('\\n', ' ').replace('.', '').replace(',', '').replace(':','').replace(')','').replace('(', '').lower().split(' ')
            bothVector = [0] * 100
            for word in both:
                bothVector += modelBoth.word_vectors[modelBoth.dictionary.keys().index(word)]
            datarow = [row[1], titleVector, abstractVector, bothVector]
            data.append(datarow)
    year1 += 1
    year2 += 1
with open('vectors' + titleFile, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

#doc2vec
titleFiles = ['titlePVDM.txt', 'titlePVDBOW.txt']
abstractFiles = ['abstractPVDM.txt', 'abstractPVDBOW.txt']
bothFiles = ['bothPVDM.txt', 'bothPVDBOW.txt']

for i in range(0, len(titleFiles)):
    year1 = 2007
    year2 = 2008
    data = []
    print(titleFiles[i])
    modelTitle = models.Doc2Vec.load(titleFiles[i])
    modelAbstract = models.Doc2Vec.load(abstractFiles[i])
    modelBoth = models.Doc2Vec.load(bothFiles[i])
    while year2 < 2018:
        with open(filename + str(year1) + '-' + str(year2) + '.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
            j=0
            for row in reader:
                # Titles only
                titleVector = modelTitle.docvecs[j]
                # Abstracts only
                abstractVector = modelAbstract.docvecs[j]
                # Abstracts and titles
                bothVector = modelBoth.docvecs[j]
                datarow = [row[1], titleVector, abstractVector, bothVector]
                data.append(datarow)
                j += 1
        year1 += 1
        year2 += 1
    with open('vectors' + titleFiles[i], 'wb') as wrfile:
        writer = csv.writer(wrfile)
        writer.writerows(data)