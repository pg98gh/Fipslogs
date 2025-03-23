# ml/preprocess.py
import joblib
import pandas as pd

# Laden des Modells
model = joblib.load('ml/model.pkl')

def load_model_and_predict(metrics_dict):
    # Beispiel: {'cpu_usage': 0.85, 'memory_usage': 0.94}
    df = pd.DataFrame([metrics_dict])
    prediction = model.predict(df)  # -1 = Anomalie, 1 = normal
    return 'Anomaly' if prediction[0] == -1 else 'Normal'
