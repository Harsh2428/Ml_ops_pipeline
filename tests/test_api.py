#  Import TestClient so we can make requests to our API/simmulated API.
from fastapi.testclient import TestClient
# Import the app from main.py so we can test it.
from main import app
# Create a reuseable test client that will be used in all tests.
client = TestClient(app)
def test_health_check():
    # verify that the health check endpoint is working as expected and returns the correct response.
    response =client.get("/health")
    # Check that the response status code is 200 OK.
    # assert keyword is used to check if a condition is true. If the condition is false, an AssertionError will be raised, indicating that the test has failed.
    # assert that the response status code is 200 OK, indicating that the health check endpoint is functioning correctly.
    assert response.status_code == 200
    # check that the response body is a JSON object with a "status" key and a value of "healthy".
    assert response.json() == {"status": "healthy"}
def test_valid_prediction():
    # Test a valid prediction request to the /predict endpoint.
    # verify that the /predict endpoint is working as expected and returns the correct response for a valid prediction request.
    payload={
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.6,
        "petal_width": 0.5
    }
    # send a simlated post request with json data to the /predict endpoint using the test client.
    response= client.post("/predict", json=payload)
    # Check that the response status code is 200 OK.
    assert response.status_code == 200
    # convert the response body to a JSON object and store it in the result variable.
    result= response.json()
    # Check that the response contains the expected keys and values.
    assert "prediction" in result
    assert "class_name" in result
    # the predicted class must belong to the set of valid class names.
    assert result["class_name"] in ["setosa", "versicolor", "virginica"]
    assert result["prediction"] in [0, 1, 2]

def test_invalid_iris_input():
    # invalid input data for the /predict endpoint, where sepal_length is negative, are not allowed.
    payload = {
        "sepal_length": -5.1,
        "sepal_width": 3.5,
        "petal_length": 1.6,
        "petal_width": 0.5
    }
    response = client.post("/predict", json=payload)
    # check that error code 422
    assert response.status_code == 422
