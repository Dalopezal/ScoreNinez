"""
    Modelo de aprendizaje para la dimension Bienestar Materno
    Random Forest
"""

import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from CargueDatos import *

# Assuming CargueDatos.py loads the data
df = CargueDatos.ExpertosBienestarMaternoDestino()

print(df.head(10))

X = df.drop("Riesgo MA", axis=1)
y = df["Riesgo MA"]

oversample = RandomOverSampler(random_state=42)
X_resampled, y_resampled = oversample.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.25, random_state=42)

modelo = RandomForestClassifier(n_estimators=200, max_depth=4, min_samples_split=3, min_samples_leaf=4)

modelo.fit(X_train, y_train)

# Predict on test data
y_pred = modelo.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Show confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

# Show classification report
class_report = classification_report(y_test, y_pred)
print('Classification Report:')
print(class_report)

data = {
    "age": 0,
    "category": 1,
    "mom_age": 1,
    "professional_assistance": 1,
    "controls": 1
}

print(data)
print('prediction')
df_prediction = pd.DataFrame([data])
prediction = modelo.predict(df_prediction)
print(prediction)

### Save model PKL
pck_file = "BienestarMaterno.pkl"
with open(pck_file, 'wb') as file:
    pickle.dump(modelo, file)
