#import libraries and initialize scaler
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

from dataframes import total21, final21

#lists of stats to transform using PCA and later use in Linear Regression
basic = ["H","HR","RBI","SB","SO","BB",]
derived = ["BA", "OBP", "SLG", "RC"]

#salary inclusive with some of the biggest offensive indicators
sal_inclusive = ["OPS", "WAR", "RC", "Salary"]

#scale each subset of data
scaler.fit(total21[derived])
derived_scaled = scaler.transform(total21[derived])

scaler.fit(total21[basic])
basic_scaled = scaler.transform(total21[basic])

scaler.fit(total21[basic+derived+["height","weight"]])
total_scaled = scaler.transform(total21[basic+derived+["height","weight"]])

#generate WCSS plot for cluster determination
wcss_d = []
wcss_b = []
for data in [("derived", derived_scaled), ("basic", basic_scaled)]:
    for i in range(1,11):
        model = KMeans(n_clusters = i, init = "k-means++")
        model.fit(data[1])
        if data[0] == "derived":
            wcss_d.append(model.inertia_)
        else:
            wcss_b.append(model.inertia_)
#two subplots
fig, axes = plt.subplots(1, 2, figsize=(16,8))
sns.lineplot(ax = axes[0], x = range(1,11), y = wcss_d)
axes[0].set_title("WCSS of Derived Dataset")
sns.lineplot(ax = axes[1], x = range(1,11), y = wcss_b)
axes[1].set_title("WCSS of Basic Dataset")

#utilize PCA to create a 2D representation of the variation within the data
pca = PCA(n_components = 2)
derived_pca = pca.fit_transform(derived_scaled)

#from the WCSS graph above it is determined that the optimal number of clusters is around 3
km = KMeans(n_clusters = 3)
label_derived = km.fit_predict(derived_pca)

#plot the results of the transformed variables
plt.figure(figsize = (10,10))
sns.scatterplot(x = derived_pca[:,0], y = derived_pca[:,1], hue = label_derived, palette='Set1').set(title = "PCA of Derived Stats")

#plot the labels in the dataset, to preserve the most data, we will use runs created as opposed to WAR
#WAR is not available for all players in the total21 dataset
#print out all stats used in clustering to better understand the results
total21["labels_derived"] = label_derived
for i in total21["labels_derived"].unique():
    stats = total21.loc[total21["labels_derived"] == i]
    print("Statistics for Height, Weight, OPS, RC for cluster {}:".format(i))
    print(stats.agg({"height":["min","max","mean"], "weight":["min","max","mean"], "OBP":["min","max","mean"], "SLG":["min","max","mean"], "RC":["min","max","mean"]}))

pca = PCA(n_components = 2)
basic_pca = pca.fit_transform(basic_scaled)

#from the WCSS plot above it is determined that the optimal number of clusters is between 3 and 4
km = KMeans(n_clusters = 4)
label_basic = km.fit_predict(basic_pca)

#plot the results of the transformed variables
plt.figure(figsize = (10,10))
sns.scatterplot(x = basic_pca[:,0], y = basic_pca[:,1], hue = label_basic, palette='Set1').set(title = "PCA of Basic Stats")

#plot the labels in the dataset, to preserve the most data, we will use runs created as opposed to WAR
#WAR is not available for all players in the total21 dataset
#print out all stats used in clustering to read the results better
total21["labels_basic"] = label_basic
for i in total21["labels_basic"].unique():
    stats = total21.loc[total21["labels_basic"] == i]
    print("Statistics for Height, Weight, OBP, SLG, RC for cluster {}:".format(i))
    print(stats.agg({"height":["min","max","mean"], "weight":["min","max","mean"], "OBP":["min","max","mean"], "SLG":["min","max","mean"], "RC":["min","max","mean"]}))