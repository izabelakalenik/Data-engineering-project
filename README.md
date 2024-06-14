# Data-engineering-project

This project, developed as a part of a Data Engineering course - 6th semester, was done in a group of 3 people.
<br />
<br />

## Project overview
The project involves analyzing a publicly available dataset - Suicide rates & socioeconomic factors (1990 - 22) - downloaded from kaggle.com. 
It is focused on suicide rates among men and women across different countries from 1990 to 2022. The analysis utilizes various machine learning algorithms and data visualization techniques to uncover 
patterns and correlations between suicide rates and socioeconomic factors.

## Dataset
The dataset includes:
* Year
* Region and Country identifiers
* Gender
* Suicide counts and population
* Economic indicators (GDP per capita, GNI per capita, employment ratio, inflation rate)

## Analysis and methodology
### KNN Prediction
We used the K-Nearest Neighbors (KNN) algorithm to predict suicide counts based on various socioeconomic factors. 
The dataset was split into training and testing sets, and features were standardized using StandardScaler. 
The performance of the KNN model was evaluated through residual analysis and prediction accuracy.

### KMeans Clustering Analysis
KMeans clustering was applied to group countries based on socioeconomic factors and suicide rates. 
The data was normalized, and clustering was performed with six clusters, 
each representing different socioeconomic profiles and suicide rates.

### Principal Component Analysis (PCA)
PCA was utilized to reduce the dimensionality of the dataset, 
revealing the underlying structure and key factors driving suicide rates across countries.

### Information Retrieval
We evaluated the performance of a ranking system applied to the dataset using precision, recall, and F1-score at 
different ranking thresholds, and plotted a precision-recall curve to visualize the performance.

## Technologies
* pandas
* sklearn
* matplotlib
* numpy
* seaborn
