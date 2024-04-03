"""
    Modelo de aprendizaje para la dimension Bienestar material
    Random Forest
    Fecha:18/01/2024
"""

import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

from CargueDatos import *

df = CargueDatos.ExpertosBienestarMaterialDestino()

print(df.head(10))

X = df.drop("Riesgo BM", axis=1)
y = df["Riesgo BM"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, min_samples_split=7, min_samples_leaf=1)

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Mostrar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Mostrar el informe de clasificación
class_report = classification_report(y_test, y_pred)
print('Classification Report:')
print(class_report)

data = {
    "age": 3,
    "category": 1,
    "rooms": 1,
    "total_people": 2,
    "income": 3,
    "public_service": 0
}

print(data)
print('prediction')
df_prediction = pd.DataFrame([data])
prediction = modelo.predict(df_prediction)
print(prediction)

### Save model PKL
pck_file = "BienestarMaterial.pkl"
with open(pck_file, 'wb') as file:
    pickle.dump(modelo, file)
