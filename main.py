
from pathlib import Path
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Load the trained model
Model_Path = Path("models/random_forest_model.joblib")
model = joblib.load(Model_Path)

# Initialize FastAPI
app = FastAPI(title="Iris Random Forest Classifier")


# Define input schema
class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)


# Root endpoint
@app.get("/")
def health_check():
    return {"status": "ready to serve"}


# Health endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Prediction endpoint
@app.post("/predict")
def predict(data: IrisInput):
    # Pass features as a two-dimensional array
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # Predict the class
    prediction = int(model.predict(features)[0])

    # Map prediction to class name
    class_names = ["setosa", "versicolor", "virginica"]

    return {
        "prediction": prediction,
        "class_name": class_names[prediction]
    }
