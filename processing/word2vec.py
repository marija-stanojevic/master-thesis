import csv
from gensim import models

year1 = 2007
year2 = 2008
filename = 'C:/Users/Marija/PyCharmProjects/scraping/arxivData '
data = []
type = 'title'

while year2 < 2018:
    with open(filename + str(year1) + '-' + str(year2) + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:
            # Titles only
            sentence = row[0][2:len(row[0]) - 1]
            sentence = sentence.replace('\\n', ' ').replace('.', '').replace(',', '').replace(':', '').replace(')','').replace('(','').lower().split(' ')
            data.append(sentence)
    year1 += 1
    year2 += 1

#Skip-gram: hierarchical softmax
model = models.Word2Vec(data, size=100, window=5, min_count=2, workers=4, negative=5, hs=1)
model.save(type + 'SgHs.txt')

#Skip-gram: negative sampling
model = models.Word2Vec(data, size=100, window=5, min_count=2, workers=4, sg=1, negative=5)
model.save(type + 'SgNs.txt')

#CBOW: hiearachical softmax
model = models.Word2Vec(data, size=100, window=5, min_count=2, workers=4, hs=1)
model.save(type + 'CbowHs.txt')

#CBOW: negative sampling
model = models.Word2Vec(data, size=100, window=5, min_count=2, workers=4)
model.save(type + 'CbowNs.txt')
