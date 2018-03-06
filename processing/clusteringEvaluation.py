from sklearn.metrics.cluster import normalized_mutual_info_score
import csv

files = ['vectorstitlePVDM.txt', 'vectorstitlePVDBOW.txt']

labels = []
with open('labels.csv', 'rb') as rfile:
    reader = csv.reader(rfile)
    for row in reader:
        labels.append(row)

for file in files:
    clusters = []
    labelsTrue = []
    mapping = {}
    print(file)
    with open(file + 'clusteringResults.csv', 'rb') as rfile:
        reader = csv.reader(rfile)
        labelsNext = False
        for row in reader:
            if labelsNext:
                clusters = row
                clusters = map(int, clusters)
                break
            if '148' in row[0] and 'K-means' in row[0]: #exchange for '148' for '18'
                labelsNext = True
        for i in range(0, len(labels)):
            if (labels[i][0]) not in mapping:
                mapping[labels[i][0]] = clusters[i]
            labelsTrue.append(mapping[labels[i][0]])
        print (normalized_mutual_info_score(labels_true=labelsTrue[0:100000], labels_pred=clusters[0:100000]))