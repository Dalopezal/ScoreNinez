"""
    Clase Utilizada para el desarrollo del modelo de aprendizaje para la dimension salud
    RandomForest
"""

import pickle
import pandas as pd
from CargueDatos import *
#randon Forest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import RandomOverSampler


#Datos Expertos
datosExpertos=CargueDatos.ExpertosSaludDestino()

#variables destino.
X = datosExpertos.drop("Riesgo SA", axis=1)
y = datosExpertos["Riesgo SA"]

oversample = RandomOverSampler(random_state=42)
X_resampled, y_resampled = oversample.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.30, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42,criterion='gini')

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

# Mostrar el informe de clasificación
class_report = classification_report(y_test, y_pred)
print('-------------------------------------Reporte de Clasificacion -------------------:')
print(class_report)

#Datos ingresados desde un API.
dataPrediccion = {
    "Edad": 0,
    "CategoriaMunicipio": 7,
    "PesoNacer": 3,
    "vacunaPentavalente": 3,
    "tripleViral": 3,
    "Nutricion": 1,
    "Lactancia":3,
    "enfermedad": 3
}

print('-------------------------------------Prediccion ---------------------------------:')
df_prediction = pd.DataFrame([dataPrediccion])
prediction=modelo.predict(df_prediction)
print(prediction)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')


# Mostrar la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(conf_matrix)

### Save model PKL
pck_file = "Salud.pkl"
with open(pck_file, 'wb') as file:
    pickle.dump(modelo, file)