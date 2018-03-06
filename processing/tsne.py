import csv
from sklearn.manifold import TSNE

files = ['titleSgHs.txt', 'titleSgNs.txt', 'titleCbowHs.txt', 'titleCbowNs.txt','abstractSgHs.txt', 'abstractSgNs.txt', 'abstractCbowHs.txt', 'abstractCbowNs.txt',
              'bothSgHs.txt', 'bothSgNs.txt', 'bothCbowHs.txt', 'bothCbowNs.txt', 'titleGlove.txt', 'abstractGlove.txt', 'bothGlove.txt']
tsne = TSNE(n_components=2)
for file in files:
    X = []
    headers = []
    with open('vocabular' + file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\"')
        for row in reader:
            headers.append(row[0])
            X.append(row[1:len(row)])
        X_tsne = tsne.fit_transform(X)
        with open('tsne' + file, 'w', newline='') as wrfile:
            writer = csv.writer(wrfile)
            writer.writerow(headers)
            writer.writerow(X_tsne[:,0])
            writer.writerow(X_tsne[:,1])