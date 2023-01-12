# MLB Player Analysis 

Python scripts dedicated to determining the height and weight of the average MLB player as well as the height and weight which yield the most successful major leaguers.

Data present in this repo is taken from the Lahman Baseball Dataset.

Data selection is done using the `pandas` library in python.

The analysis is broken down into the following four sections: explortory data analysis, conventional analysis, clustering, and linear regression.

### Exploratory Data Analysis 
- Uses simple distribution graphs and plots to identify trends in players' heights and weights.
### Conventional Analysis
- Analyzed the dataset through taking the average WAR of all height and weight combinations, as well as taking the average WAR of height and weight separately. With the ultimate goal being to find a combination with the highest WAR.
- cluster players based upon basic and derived stats, using PCA to reduce dimensionality in the process, in an attempt to better visualize similar players in the form of a 2D scatterplot. Basic refers to any statistic which was already present in the initial lahman dataset, while derived refers to statistics which were calculated in this notebook.
### Clustering
- Clustering was performed on the dataset to identify similarities between players.
- `Basic` refers to any statistic which was already present in the initial lahman dataset, 
- `Derived` refers to statistics which were calculated in this notebook.
### Linear Regression
- Performs linear regression to analyze the relationship between WAR and salary, as well as WAR and perfromance on the field.
