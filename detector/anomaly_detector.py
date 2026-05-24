from sklearn.ensemble import IsolationForest
import numpy as np

# Training data (normal behavior)
training_data = np.array([
    [1],
    [2],
    [1],
    [2],
    [3],
    [2],
    [1],
    [2]
])

# Train model
model = IsolationForest(contamination=0.2)

model.fit(training_data)

def detect_anomaly(value):

    prediction = model.predict([[value]])

    if prediction[0] == -1:
        return True

    return False