#import Matplotlib and numpy for plotting and analysis
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from dataframes import final21, total21

#determine how many players per height
print(total21.groupby(["height"]).size())

#create a new dataframe eliminating outlying players on either end 
#(results in at least 10 players per height)
height_lim = total21.loc[(total21["height"] >= 68) & (total21["height"] <= 77)]
data = height_lim[["height", "OPS"]]
plt.figure(figsize = (10,10))
# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(data=data, x="height", y="OPS", inner = "quart", linewidth=1)
sns.despine(left=True)

#distribution of weight and OPS
plt.figure(figsize = (10,10))
sns.histplot(data=total21, x = "weight", y = "OPS")
#rugplot gives a good reference for the distribution of player weight
sns.rugplot(data=total21, x = "weight", y = "OPS")