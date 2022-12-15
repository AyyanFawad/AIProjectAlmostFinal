import warnings
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import random
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn.cluster import KMeans

sns.set()

data = pd.read_csv(r"E:\AIProjectFrontEnd\testset.csv")
data.info()
data.isnull().sum()

df = data.drop(columns=['id', 'name', 'artists', 'release_date', 'year'])
df.corr()


datatypes = ['int', 'int', 'int', 'float', 'float', 'float']
normarization = data.select_dtypes(include=datatypes)
result = preprocessing.normalize(normarization, axis=0)


def euclidean(point, data):
    """
    Euclidean distance between point & data.
    Point has dimensions (m,), data has dimensions (n,m), and output will be of size (n,).
    """
    return np.sqrt(np.sum((point - data)**2, axis=1))


class KMeans:
    def __init__(self, n_clusters=8, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X_train):
        # Initialize the centroids, using the "k-means++" method, where a random datapoint is selected as the first,
        # then the rest are initialized w/ probabilities proportional to their distances to the first
        # Pick a random point from train data for first centroid
        self.centroids = [random.choice(X_train)]
        for _ in range(self.n_clusters-1):
            # Calculate distances from points to the centroids
            dists = np.sum([euclidean(centroid, X_train)
                           for centroid in self.centroids], axis=0)
            # Normalize the distances
            dists = np.sum(dists)
            # Choose remaining points based on their distances
            new_centroid_idx, = np.random.choice(
                range(len(X_train)), size=1, p=dists)
            self.centroids += [X_train[new_centroid_idx]]

        # Iterate, adjusting centroids until converged or until passed max_iter
        iteration = 0
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and iteration < self.max_iter:
            # Sort each datapoint, assigning to nearest centroid
            sorted_points = [[] for _ in range(self.n_clusters)]
            for x in X_train:
                dists = euclidean(x, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(x)
            # Push current centroids to previous, reassign centroids as mean of the points belonging to them
            prev_centroids = self.centroids
            self.centroids = [np.mean(cluster, axis=0)
                              for cluster in sorted_points]
            for i, centroid in enumerate(self.centroids):
                # Catch any np.nans, resulting from a centroid having no points
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            iteration += 1

    def evaluate(self, X):
        centroids = []
        centroid_idxs = []
        for x in X:
            dists = euclidean(x, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)
        return centroids, centroid_idxs


kmeans = KMeans(n_clusters=10)
features = kmeans.fit_predict(normarization)
data['features'] = features
MinMaxScaler(data['features'])


def recommend(songs, amount=1):
    distance = []
    song = data[(data.name.str.lower() == songs.lower())].head(1).values[0]
    rec = data[data.name.str.lower() != songs.lower()]
    for songs in tqdm(rec.values):
        d = 0
        for col in np.arange(len(rec.columns)):
            if not col in [1, 6, 12, 14, 18]:
                d = d + np.absolute(float(song[col]) - float(songs[col]))
        distance.append(d)
    rec['distance'] = distance
    rec = rec.sort_values('distance')
    columns = ['artists', 'name']
    return rec[columns][:amount]


print(recommend("lovers rock", 10))

# def recsystem():
#     sns.set()

#     data = pd.read_csv(r"C:\Users\erajr\Desktop\AI proj\spotify.csv")
#     data.info()
#     data.isnull().sum()

#     df = data.drop(columns=['id', 'name', 'artists', 'release_date', 'year'])
#     df.corr()

#     datatypes = ['int', 'int', 'int', 'float', 'float', 'float']
#     normarization = data.select_dtypes(include=datatypes)
#     result = preprocessing.normalize(normarization, axis=0)
#     kmeans = KMeans(n_clusters=10)
#     features = kmeans.fit_predict(normarization)
#     data['features'] = features
#     MinMaxScaler(data['features'])
#
