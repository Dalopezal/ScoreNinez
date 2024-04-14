from CargueDatos import *
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler

#Datos Expertos
datosExpertos=CargueDatos.ExpertosSaludDestino()

print(datosExpertos.shape)

y = datosExpertos["Riesgo SA"]   #variable Ordinal dependiente
X = datosExpertos.drop("Riesgo SA", axis=1)

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)

print(X_resampled.shape)

print(y_resampled)

