import numpy as np
from sklearn.preprocessing import StandardScaler

import plots as Plots
import data_processing as DataProcessing
import pca as PCA
import knn as KNN

def run():
    df, features = DataProcessing.load_dataset()
    X = df[features]
    
    Plots.plot_country_distribution(df)
    Plots.plot_region_distribution(df)
    Plots.plot_country_region_distribution(df)
    Plots.plot_correlation_matrix(df)

    numeric_df = df.select_dtypes(include=[np.number])
    Plots.plot_descriptive_stats(numeric_df)
    Plots.plot_correlation_heatmap(numeric_df)
    Plots.plot_suicide_counts_over_time_by_region_and_gender(df)
    Plots.plot_total_suicides_over_time_by_region(df)
    Plots.plot_suicide_counts_by_gender(df)
    
    #PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    PCA.plot_pca_2d(X_scaled, df)
    PCA.plot_pca_3d(X_scaled, df)

    #KNN
    target = 'SuicideCount'
    y = df[target]
    knn_model, scaler = KNN.perform_knn(df, y, features)

    # Example of making new predictions (if we have new_data to predict on)
    # new_data = ...
    # predictions = predict_new_data(knn_model, scaler, new_data)
    # print(predictions)

 
if __name__ == "__main__":
    run()
