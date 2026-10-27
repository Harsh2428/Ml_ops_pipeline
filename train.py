from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

# load the iris dataset
iris = load_iris()
X=iris.data
y=iris.target
# split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
# train the model
clf.fit(X_train, y_train)
# make predictions on the test set
y_pred = clf.predict(X_test)
# accuracy
accuracy =accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# save the model to a file
model_dir=Path("models")
model_path=model_dir/"random_forest_model.joblib"
joblib.dump(clf, model_path)
print(f"Model saved to {model_path}")