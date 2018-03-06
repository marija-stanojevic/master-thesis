from glove import Glove
import csv

filename = 'C:/Users/Marija/PyCharmProjects/scraping/arxivData '

titleFile = 'titleGlove.txt'
abstractFile = 'abstractGlove.txt'
bothFile = 'bothGlove.txt'
year1 = 2007
year2 = 2008
data = []
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