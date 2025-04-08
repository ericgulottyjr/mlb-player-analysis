# MLB Player Analysis 

Python scripts dedicated to determining the height and weight of the average MLB player as well as the height and weight which yield the most successful major leaguers.

## Introduction

Baseball is an incredibly popular sport, also known as America's pasttime. For many watching from home, the true size of baseball players may be a mystery. Some tower over the masses, such as Aaron Judge at 6'7", others, like Jose Altuve, are an unassuming 5'6". Like in many other sports, great athletes can excel in baseball through hard work and talent, no matter their size. However, the question still lingers, what is the height and weight the average MLB player? Or perhaps more importantly, what combination of height and weight tends to produce the most successful ballplayers? These are all questions which I attempt to answer in this project.

Statistics such as Wins Above Replacement (WAR) and Runs Created (RC) aim to provide a means of measurement regarding a player's ability to contribute to his team, and are a good reference of a player's production within the game of baseball. A simple rundown of a WAR score is as follows: 0-2 refers to a basic level player, 2-4 is a fringe all-star, 4-6 is an all-star/superstar, a 6+ WAR means a player is typically having a career-defining season.

*For reference, in 2022, American League MVP Aaron Judge hit a league-record 62 home runs and racked up a WAR of 10.6, the next closest player being generational dual-threat talent Shohei Ohtani with 9.6.*

## Project Goals

This project aims to use 2021 hitting data to achieve two primary goals:

1. **Find the ideal physical build for MLB success**: By analyzing the relationship between players' height, weight, and performance metrics (WAR), we can identify whether certain physical attributes correlate with baseball success. This information could be valuable for scouting departments when evaluating prospective talent.

2. **Determine the dollar value of performance metrics**: By analyzing salary data in relation to performance statistics like WAR and RC, we can estimate the market value of these performance metrics. This could provide insights into player valuation for contract negotiations and team budget allocation.

Additionally, this analysis explores the relationship between various offensive statistics and overall player value, which can help teams identify undervalued skills in the player market.

## Data Sources

The data used in this project come from two sources:
- **Lahman Baseball Database**: Provides comprehensive statistical data on players, including biographical information
- **Baseball-reference.com**: Source for salary information and additional metrics

Due to differences in these sources, the number of players with available salary statistics is quite limited compared to those available for analysis when looking purely at batting statistics.

Data selection is done using the `pandas` library in Python. Only players with more than 100 at-bats (ABs) in a season were selected to be part of the final datasets, as players with fewer ABs likely have less of a main role on their teams and are outside the scope of this analysis.

## Methodology

In this project, I employ:
- Basic graph-based data analysis using scatter plots and violin plots
- Principle Component Analysis (PCA) in tandem with KMeans clustering to identify trends or anomalies
- Linear regression techniques to analyze relationships between various statistics

PCA is a method of transforming data where its dimensions are reduced while simultaneously capturing the maximum variance in the data. This is particularly useful given the many statistics relating to a player's performance.

The analysis is broken down into the following four sections:

### Exploratory Data Analysis 

This section uses simple distribution graphs and plots to identify trends in players' heights and weights.

Key findings:
- The most common height for MLB players is 72-73 inches (6'0"-6'1")
- Players with a height of 74 inches (6'2") have the highest average WAR at 2.23
- Players weighing approximately 190 pounds have the highest average WAR at 2.71
- Notable players at the "optimal" height of 74 inches include Juan Soto (WAR 7.1), Trea Turner (WAR 6.5), and Trevor Story (WAR 4.2)

Due to WAR statistics only being available for a subset of players, many analyses also use OPS (On-base Plus Slugging) as an alternative measure of player performance.

### Conventional Analysis

This section analyzes the dataset by taking the average WAR of all height and weight combinations, as well as analyzing height and weight separately, with the ultimate goal of finding a combination with the highest WAR.

Key observations:
- Height has a stronger correlation with WAR than weight does
- The "sweet spot" for player build appears to be around 6'2" (74 inches) and 190 pounds
- There's significant variation in performance even among players with similar builds, indicating that physical attributes are just one factor in player success

The analysis revealed that players of height 74 inches (6'2") had the highest mean WAR at 2.23, significantly higher than other height groups. This height group includes notable players such as Juan Soto (WAR 7.1), Trea Turner (WAR 6.5), and Xander Bogaerts (WAR 4.9).

For weight, players around 190 pounds showed the highest mean WAR at 2.71, with standout performers like Jose Ramirez (WAR 6.7) and Enrique Hernandez (WAR 4.9). When analyzing specific height-weight combinations, the analysis found that certain combinations performed better than others, suggesting an optimal physical build for baseball performance.

However, the considerable variation within each height-weight category indicates that while physical attributes may provide certain advantages, they are far from the only determinant of success in baseball.

### Clustering

This section uses machine learning to cluster players based on their statistics, using PCA to reduce dimensionality and better visualize similarities between players.

The clustering analysis was performed using two different sets of statistics:
- **Basic statistics**: Standard baseball stats already present in the Lahman dataset (H, HR, RBI, SB, SO, BB)
- **Derived statistics**: Calculated metrics such as BA, OBP, SLG, and RC

For each clustering result, summary statistics were generated to characterize the players within each cluster, revealing patterns such as:
- Power hitters tend to cluster together regardless of height/weight
- Contact hitters with high batting average but lower power also form distinct clusters
- Players with exceptional speed and base-stealing ability form their own cluster

The KMeans algorithm was used to create these clusters, with an optimal number of clusters determined through the Elbow Method. After applying PCA to reduce the dimensionality of player statistics, the resulting 2D visualization allows us to see clear groupings of similar players that wouldn't be obvious from simply looking at the raw statistics.

For example, one cluster contains elite players like Juan Soto, Mike Trout, and Fernando Tatis Jr., while another includes consistent contact hitters with less power. This clustering approach provides valuable insights for team construction, scouting, and player development strategies.

> **Note on Visualizations**: The notebook contains several informative visualizations including:
> - Scatter plots of height vs. weight colored by WAR
> - PCA-reduced 2D visualizations of player clusters
> - Distribution plots of player measurements
> - Regression plots showing relationships between statistics and salary
>
> These visualizations are available when viewing the full Jupyter notebook.

### Linear Regression

This section performs linear regression to analyze relationships between:
- WAR and salary
- WAR and on-field performance metrics
- RC and basic statistics

Key findings:
- Basic statistics can predict Runs Created with reasonable accuracy
- WAR has a positive correlation with salary, though many outliers exist
- The statistical "value" of WAR in terms of salary appears to be significant, with each additional point of WAR corresponding to approximately $2-4 million in salary on average

The regression analysis used matrix transformation and multiplication to find the best-fitting model, implementing the formula:

β = (X^T X)^(-1) X^T y

where X is the matrix of predictor variables and y is the target variable (either WAR, RC, or Salary depending on the specific regression).

Four separate regression models were created:
1. Using basic statistics to predict Runs Created
2. Using basic statistics to predict WAR
3. Using salary data to predict RC
4. Using salary data to predict WAR

The results showed that offensive production metrics correlate well with both WAR and salary, though there are interesting outliers - players who are either underpaid relative to their performance or overpaid relative to their statistics. This analysis helps answer the question of the dollar value of WAR, which is valuable information for MLB front offices during contract negotiations.

## Conclusion

The analysis reveals that while physical attributes like height and weight do correlate with player performance in MLB, the relationship is not straightforward. The most successful build appears to be around 6'2" (74 inches) and 190 pounds, though exceptional players can be found with various body types.

Some key takeaways from this analysis:

1. **Physical attributes matter, but aren't deterministic**: While the data shows that players of certain heights and weights tend to perform better on average, there is significant variation within each group. This suggests that technical skills, training, and natural talent play crucial roles beyond physical attributes.

2. **Clustering reveals natural player types**: The clustering analysis identified distinct groups of players with similar statistical profiles, which aligns with traditional baseball archetypes like "power hitters," "contact specialists," and "speed-focused players."

3. **WAR does translate to financial value**: The regression analysis suggests that each point of WAR is worth approximately $2-4 million in player salary, though market inefficiencies exist that teams could potentially exploit.

This project demonstrates the power of data analysis in understanding the complex factors that contribute to success in professional baseball. The methods used here could be extended to analyze pitchers, defensive specialists, or to examine how these relationships change over time as the game evolves.

For MLB front offices, these insights could inform scouting priorities, player development strategies, and contract negotiations. For fans, it provides a deeper understanding of the physical and statistical factors that contribute to success in America's pastime.
