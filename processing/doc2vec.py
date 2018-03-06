import csv
from gensim import models


year1 = 2007
year2 = 2008
filename = 'C:/Users/Marija/PyCharmProjects/scraping/arxivData '
data = []
type = 'title'

i = 0
while year2 < 2018:
    with open(filename + str(year1) + '-' + str(year2) + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:
            # Titles only
            document = row[0][2:len(row[0]) - 1]
            document = models.doc2vec.TaggedDocument(words=document.replace('\\n', ' ').replace('.', '').replace(',', '').replace(':', '').replace(')','').replace('(','').lower().split(), tags=[i])
            data.append(document)
            i += 1
    year1 += 1
    year2 += 1

#Skip-gram (PV-DM)
model = models.Doc2Vec(data, size=100, window=5, min_count=2, workers=4)
model.save(type + 'PVDM.txt')

#CBOW (PV-DBOW):
model = models.Doc2Vec(data, size=100, window=5, min_count=2, workers=4, dm=0)
model.save(type + 'PVDBOW.txt')
