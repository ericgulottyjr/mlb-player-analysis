import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from dataframes import total21, final21
#find the combinations of height and weight which exist in the dataset, calculate average WAR for said height and weight
war = final21[["height", "weight","WAR"]].groupby(["height","weight"]).agg({"WAR":"mean"}) #produces 7.3
#find highest average WAR
print("The highest WAR for height and weight when calculated together is:", war["WAR"].max())
print(final21.loc[(final21["height"] == 72) & (final21["weight"] == 195), ["nameFirst", "nameLast", "WAR"]])

#highest mean WAR by height, first we eliminate heights with under 10 players
war_height1 = final21[["height", "weight","WAR"]].groupby(["height"])
#figure out how many players per height
print(war_height1.size())
#new height dataframe
height_lim = final21.loc[(final21["height"] >= 70) & (final21["height"] <= 76)]
war_height = height_lim[["height", "weight","WAR"]].groupby(["height"])
#find the mean WAR at each height
print(war_height.agg({"WAR":"mean"}))
#find the highest mean WAR
print(war_height.agg({"WAR":"mean"}).idxmax()) #produces a height of 74 inches w/ highest WAR
#find a list of the players who are listed at this height
print(final21.loc[final21["height"] == 74, ["nameFirst", "nameLast", "WAR"]])

#using a weight histogram to determine how to narrow down the distribution
sns.histplot(data=final21, x = "weight", binwidth = 5, kde = True)

#create a new variable containing ranges of weights (ex. 200 = 200~204.999)
weights = list(range(160,290,5))
for i in range(len(weights)-1):
    for weight in final21["weight"]:
        if (int(weight) >= weights[i]) & (int(weight) < weights[i+1]):
            final21.loc[final21["weight"]==weight, ["weight_agg"]] = weights[i]

#highest mean WAR by height, first we eliminate heights with under 10 players
war_weight1 = final21[["height", "weight_agg","WAR"]].groupby(["weight_agg"])
#figure out how many players per weight range
print(war_weight1.size())
#new weight dataframe
weight_lim = final21.loc[(final21["weight_agg"] >= 180) & (final21["weight_agg"] <= 235)]
war_weight = weight_lim[["height", "weight_agg","WAR"]].groupby(["weight_agg"])
#find the mean WAR at each weight
print(war_weight.agg({"WAR":"mean"}))
#find the highest mean WAR
print(war_weight.agg({"WAR":"mean"}).idxmax()) #produces a weight of 190 lbs. w/ highest WAR
#find a list the players who are listed at this weight
print(final21.loc[final21["weight_agg"] == 190, ["nameFirst", "nameLast", "WAR"]])

#find a player from the height and weight with highest respective mean WAR
info = ["nameFirst","nameLast","WAR","height","weight"]
players = final21.loc[(final21["height"] == 74) & (final21["weight_agg"] == 190), info]
print(players)
print("Mean WAR among players of 74 inches and 190lbs of weight:", players["WAR"].mean())

war_hw = weight_lim[["height", "weight_agg","WAR"]]
table = pd.pivot_table(war_hw, values = "WAR", index = "weight_agg", columns = "height", aggfunc = np.mean)
#limit table by height, given that weight is already limited in weight_lim
table_lim = table[[column for column in table.columns if (column >= 70) & (column <= 76)]]

#plot visualizations of all this math!
fig, axes = plt.subplots(1, 2, figsize=(16,8))
sns.scatterplot(ax=axes[0], data=total21, x = "height", y = "weight")
axes[0].set_title("Scatterplot of Height and Weight")

#heatmap to help visualize the distribution of WAR among players of a given height and weight (organized in groups of 5 lbs.)
sns.heatmap(ax=axes[1], data=table_lim, annot=True, fmt=".1f", cmap="crest")
axes[1].invert_yaxis()
axes[1].set_title("Heatmap of Height, Weight, and WAR")