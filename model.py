from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

def train_model():
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train a Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test

def predict(model, X_test):
    # Make predictions on the test set
    predictions = model.predict(X_test)
    return predictions

if __name__ == "__main__":
    # Train the model
    trained_model, test_data, true_labels = train_model()

    # Make predictions
    predicted_labels = predict(trained_model, test_data)

    # Evaluate the model
    accuracy = accuracy_score(true_labels, predicted_labels)
    print(f"Model Accuracy: {accuracy}")
