from glove import Corpus, Glove
import csv

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

corpus = Corpus()
corpus.fit(data, window=10)
glove = Glove(no_components=100, learning_rate=0.025)
glove.fit(corpus.matrix, epochs=5, no_threads=4)
glove.add_dictionary(corpus.dictionary)
glove.save(type + 'Glove.txt')
