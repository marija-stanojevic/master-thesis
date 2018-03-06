from sklearn.cluster import KMeans, SpectralClustering
import numpy as np
import csv
import ast
import re

files = ['vectorstitleSgHs.txt', 'vectorstitleSgNs.txt', 'vectorstitleCbowHs.txt', 'vectorstitleCbowNs.txt', 'vectorstitleGlove.txt', 'vectorstitlePVDM.txt', 'vectorstitlePVDBOW.txt']
titles = []
abstracts = []
both = []

for file in files:
    print(file)
    with open(file , 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:
            row[1] = re.sub(' +', ' ', row[1])
            row[2] = re.sub(' +', ' ', row[2])
            row[3] = re.sub(' +', ' ', row[3])
            titles.append(ast.literal_eval(row[1].replace('\n', '').replace('[ ','[').replace(' ', ',')))
            abstracts.append(ast.literal_eval(row[2].replace('\n', '').replace('[ ','[').replace(' ', ',')))
            both.append(ast.literal_eval(row[3].replace('\n', '').replace('[ ','[').replace(' ', ',')))
        titles = np.asarray(titles)
        abstracts = np.asarray(abstracts)
        both = np.asarray(both)
        with open(file + 'clusteringResults.csv', 'ab') as wrfile:
            writer = csv.writer(wrfile)
            writer.writerow(['Data from file:' + file])
            writer.writerow(['K-means clustering into 18 clusters: next rows are titles clustering labels, then centers; abstract clustering labels, then centers; both clustering labels, then centers'])
            kmeans = KMeans(n_clusters=18, random_state=0, n_jobs=1, n_init=2, max_iter=100, tol=1e-2)
            kmeans.fit(titles)
            writer.writerow(kmeans.labels_)
            writer.writerow(kmeans.cluster_centers_)
            kmeans.fit(abstracts)
            writer.writerow(kmeans.labels_)
            writer.writerow(kmeans.cluster_centers_)
            kmeans.fit(both)
            writer.writerow(kmeans.labels_)
            writer.writerow(kmeans.cluster_centers_)
         
