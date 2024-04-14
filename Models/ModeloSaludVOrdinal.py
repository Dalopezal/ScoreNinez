"""
    Clase Utilizada para el desarrollo del modelo de aprendizaje para la dimension salud
    Regresion Ordinal
"""

import pickle
import pandas as pd
from CargueDatos import *
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from statsmodels.miscmodels.ordinal_model import OrderedModel
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from scipy.stats import chi2_contingency
from lifelines import KaplanMeierFitter  # Install lifelines library if needed
from lifelines.utils import concordance_index


#Datos Expertos
datosExpertos=CargueDatos.ExpertosSaludDestino()

print(datosExpertos.head(10))

riesgo_sa_dummy = pd.get_dummies(datosExpertos["Riesgo SA"], prefix="RiesgoSA", dtype=int)

datosExpertos = pd.concat([datosExpertos, riesgo_sa_dummy], axis=1)
datosExpertos.drop("Riesgo SA", axis=1, inplace=True)

print(datosExpertos.head(10))

y = datosExpertos["RiesgoSA_1"]  # Variable dependiente ordinal (dummy)
X = datosExpertos.drop("RiesgoSA_1", axis=1)

ros = RandomOverSampler(random_state=42)

X_resampled, y_resampled = ros.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.30, random_state=42)

modelo = OrderedModel(y_train, X_train)
modelo_fit = modelo.fit()

# Predicciones
y_pred = modelo_fit.predict(X_test)

print(y_pred)