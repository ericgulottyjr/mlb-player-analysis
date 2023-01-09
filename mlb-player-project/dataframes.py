#import libraries
import pandas as pd

#reading CSVs into python
people = pd.read_csv("data/People.csv")
batting = pd.read_csv("data/Batting.csv")
#salaries.csv copied from baseball-reference.com
salaries = pd.read_csv("data/Salaries.csv")
#the dataset runs from 1871~ filter to display more relevant results
batting[batting["yearID"] >= 2021].head()

#create the "people" dataframe, focused solely on a player's name, height, and weight
people1 = people[["playerID","nameFirst","nameLast","weight","height"]]

#filter out statistics before 2021 (last year in dataset)
batting21 = batting.loc[(batting["yearID"] == 2021)]

#collapse the data for players who were on multiple teams in 2021 (csv contains more than one row for their stats)
statistics = ["playerID","G","AB","R","H","2B","3B","HR","RBI","SB","CS","BB","SO","IBB","HBP","SH","SF","GIDP"]
stats21 = batting21[statistics]
stats21_sum = stats21.groupby('playerID', as_index = False).sum()

#filter out players with less than 100 At Bats (ABs)
filtered21 = stats21_sum.loc[(stats21_sum["AB"] >= 100)]

#removing the dollar sign to make salaries comparable
salaries["Salary"] = salaries["Salary▼"].str.replace("$", "")
salaries["Salary"] = salaries["Salary"].astype(int)

#create columns for Batting Average (BA), On-Base Percentage (OBP), Slugging (SLG), OPS (On-Base+Slugging)
s = filtered21 #s for "sabermetrics" (these statistics aren't necessarily sabermetric but its a fun represenation)
s["BA"] = s["H"]/s["AB"]
s["OBP"] = (s["H"]+s["BB"]+s["HBP"])/(s["AB"]+s["BB"]+s["HBP"]+s["SF"])
s["SLG"] = ((s["H"]-s["2B"]-s["3B"]-s["HR"]) + 2*s["2B"] + 3*s["3B"] + 4*s["HR"])/s["AB"]
s["OPS"] = s["OBP"] + s["SLG"]
#new statistic, Runs Created (RC)
s["RC"] = ((s["H"]+s["BB"]+s["HBP"]-s["CS"]-s["GIDP"])*
(((s["H"]-s["2B"]-s["3B"]-s["HR"])+2*s["2B"]+3*s["3B"]+4*s["HR"])+0.26*(s["BB"]-s["HBP"]+s["IBB"])
+0.52*(s["SH"]+s["SF"]+s["SB"])))/(s["AB"]+s["BB"]+s["HBP"]+s["SH"]+s["SF"])

#create a final table with relevant baseball statistics combined with biographical information
total21 = s.merge(people1, on = "playerID")
#check for null values
print(total21.isnull().sum())

#extract just player name and their salary from salaries.csv
salaries1 = salaries[["Name", "WAR", "Salary"]]
salaries1["playerID"] = salaries["Name-additional"]

#combine salaries1 with the total player statistics dataframe
tot_w_sal21 = total21.merge(salaries1, how = "left", on = "playerID")

#check how many players are missing salary numbers
print(tot_w_sal21.isnull().sum())

#create final dataframe
final21 = tot_w_sal21.dropna()
final21.head()