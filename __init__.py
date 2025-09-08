from flask import render_template
import numpy as np
from sklearn.linear_model import LinearRegression

def monitor_geofencing():
    return render_template('geofencing.html')

def predict_geofence_events(historical_data):
    """
    Predict future geofence events based on historical data.
    :param historical_data: List of tuples (timestamp, event_count)
    :return: Predicted event count for the next time period
    """
    # Prepare data for regression
    timestamps = np.array([t[0] for t in historical_data]).reshape(-1, 1)
    event_counts = np.array([t[1] for t in historical_data])
    model = LinearRegression()
    model.fit(timestamps, event_counts)
    next_timestamp = np.array([[timestamps[-1][0] + 1]])
    predicted_count = model.predict(next_timestamp)
    return predicted_count[0]