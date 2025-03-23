# ml/train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

# Beispiel-Daten: CPU und RAM-Verbrauch (fiktiv)
data = {
    "cpu_usage": [0.2, 0.25, 0.3, 0.23, 0.22, 0.85, 0.9, 0.88, 0.21, 0.23, 0.95],  # 0.9+ sind evtl. Anomalien
    "memory_usage": [0.4, 0.45, 0.5, 0.43, 0.44, 0.95, 0.93, 0.92, 0.41, 0.42, 0.99]
}
df = pd.DataFrame(data)

# Trainiere ein einfaches Anomaly Detection Modell
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(df)

# Speichere das Modell
joblib.dump(model, './ml/model.pkl')

print("Modell gespeichert als model.pkl")
