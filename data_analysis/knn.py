from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def perform_knn(X, y, features, n_neighbors=5, test_size=0.2, random_state=42):
    # Scaling features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X[features])

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=random_state)

    # Model Training
    knn_model = KNeighborsRegressor(n_neighbors=n_neighbors)
    knn_model.fit(X_train, y_train)

    # Model Evaluation
    y_pred = knn_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    #print("Ypred", y_pred)
    print("Mean Squared Error:", mse)

    return knn_model, scaler

def predict_new_data(knn_model, scaler, new_data):
    scaled_new_data = scaler.transform(new_data)
    predictions = knn_model.predict(scaled_new_data)
    return predictions
