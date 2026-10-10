from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

def train_random_forest(df):
    # Prepare your data
    feature_cols = ['weather_conditions', 'speed_limit', 'hour', 'day_of_week', 'road_type']  # Example features
    X = df[feature_cols]  # Features
    y = df['legacy_collision_severity']  # The target variable (accident severity)

    # Handle categorical variables (if any)
    X = pd.get_dummies(X, drop_first=True)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)  # Train the model

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    return model


def predict_severity(model, input_data):
    # Recreate the column structure used during training
    input_data_encoded = pd.get_dummies(input_data, drop_first=True)

    # Align columns with model's training data (fill missing with 0)
    model_features = model.feature_names_in_
    input_data_aligned = input_data_encoded.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(input_data_aligned)
    return prediction[0]

