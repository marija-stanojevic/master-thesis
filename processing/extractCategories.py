import csv
from gensim import models

filename = 'C:/Users/Marija/PyCharmProjects/scraping/arxivData '

labels = []
year1 = 2007
year2 = 2008
while year2 < 2018:
    with open(filename + str(year1) + '-' + str(year2) + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:
            labels.append(row[3][2:len(row[3]) - 1].split(' '))
    year1 += 1
    year2 += 1
with open('labels.csv', 'wb') as wrfile:
    writer = csv.writer(wrfile)
    writer.writerows(labels)
