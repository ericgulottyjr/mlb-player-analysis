#import libraries and initialize scaler
import matplotlib as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from dataframes import total21, final21

scaler = StandardScaler()

#clustering based on height weight and WAR for some visualization
scaler.fit(final21[["height", "weight","WAR"]])
#transform the data so each variable is weighted equally
war_scaled = scaler.transform(final21[["height", "weight","WAR"]])

#Elbow Method for finding optimum number of clusters
wcss = []
for i in range(1,11):
    model = KMeans(n_clusters = i, init = "k-means++")
    model.fit(war_scaled)
    wcss.append(model.inertia_)

#Plot Graph
plt.figure(figsize=(10,10))
plt.plot(range(1,11), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#from the wcss graph, 4~7 clusters seem ideal
#since there are already only three dimensions to this data, we won't use PCA to further reduce its dimensions
km = KMeans(n_clusters = 5)
war_labels = km.fit_predict(war_scaled)

plt.figure(figsize = (10,10))
ax = plt.axes(projection = '3d')
ax.scatter3D(final21["height"], final21["weight"], final21["WAR"], c = war_labels)
ax.set_xlabel('height')
ax.set_ylabel('weight')
ax.set_zlabel('WAR')

#print the min, max, and mean height, weight, and WAR of players in each cluster
final21["war_labels"] = war_labels
for i in final21["war_labels"].unique():
    players = final21.loc[final21["war_labels"] == i, ["nameFirst","nameLast", "height", "weight", "WAR"]]
    print("Statistics for height, weight, & WAR for cluster {}:".format(i))
    print(players.agg({"height":["min","max","mean"],"weight":["min","max","mean"],"WAR":["min","max","mean"]}))

