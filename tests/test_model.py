import pytest
from model import train_model, predict

@pytest.fixture
def trained_model_and_test_data():
    # Fixture to get a trained model and test data
    trained_model, test_data, true_labels = train_model()
    return trained_model, test_data, true_labels

def test_model_prediction(trained_model_and_test_data):
    # Test the prediction functionality of the model

    # Unpack the fixture
    trained_model, test_data, true_labels = trained_model_and_test_data

    # Make predictions
    predicted_labels = predict(trained_model, test_data)

    # Ensure the predicted labels have the correct length
    assert len(predicted_labels) == len(true_labels)

    # Ensure the predicted labels are integers
    assert all(isinstance(label, int) for label in predicted_labels)

def test_model_accuracy(trained_model_and_test_data):
    # Test the accuracy of the model

    # Unpack the fixture
    trained_model, test_data, true_labels = trained_model_and_test_data

    # Make predictions
    predicted_labels = predict(trained_model, test_data)

    # Ensure accuracy is a valid value between 0 and 1
    accuracy = sum(predicted_labels == true_labels) / len(true_labels)
    assert 0 <= accuracy <= 1
