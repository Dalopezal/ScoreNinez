"""
    Clase Utilizada para el desarrollo del modelo de aprendizaje para la dimension salud
    Regresion Ordinal
"""

import pickle
import pandas as pd
from statsmodels.stats.diagnostic import het_breuschpagan

from CargueDatos import *
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from scipy.stats import kendalltau
from statsmodels.miscmodels.ordinal_model import OrderedModel
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from scipy.stats import chi2_contingency
from lifelines import KaplanMeierFitter  # Install lifelines library if needed
from lifelines.utils import concordance_index
#https://www.statsmodels.org/dev/examples/notebooks/generated/ordinal_regression.html

import numpy as np
import pandas as pd
import scipy.stats as stats

from statsmodels.miscmodels.ordinal_model import OrderedModel

#Datos Expertos
datosExpertos=CargueDatos.ExpertosSaludDestino()

print(datosExpertos.head(10))

print(datosExpertos.dtypes)

print(datosExpertos['Riesgo SA'].dtype)


y = datosExpertos["Riesgo SA"]  # Variable dependiente ordinal
X = datosExpertos.drop("Riesgo SA", axis=1)

ros = RandomOverSampler(random_state=42)

X_resampled, y_resampled = ros.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.30, random_state=42)


mod_prob = OrderedModel(y_train,
                        X_train,
                        distr='probit')

res_prob = mod_prob.fit(method='bfgs')
print(res_prob.summary())

r= mod_prob.predict(res_prob.params, X_test)

print(r)

# Convertir las probabilidades en etiquetas de clase

predicted_labels = np.argmax(r, axis=1)
predicted_labels_plus_one = predicted_labels + 1
print(predicted_labels_plus_one)
print(predicted_labels)
print(y_test)

tau, _ = kendalltau(y_test, predicted_labels_plus_one)

print("Índice de concordancia de Kendall:", tau)

print('------')

mod_log = OrderedModel(y_train,
                        X_train,
                        distr='logit')

res_log = mod_log.fit(method='bfgs', disp=False)
print(res_log.summary())

r_log= mod_log.predict(res_log.params, X_test)
print(r_log)


predicted_labels = np.argmax(r_log, axis=1)
predicted_labels_plus_one = predicted_labels + 1
print(predicted_labels_plus_one)
print(predicted_labels)
print(y_test)

tau, _ = kendalltau(y_test, predicted_labels_plus_one)

print("Índice de concordancia de Kendall:", tau)



# Calcula la suma de cuadrados total (SST)
mean_y = np.mean(y_test)
SST = np.sum((y_test - mean_y) ** 2)

# Calcula la suma de cuadrados residuales (SSE)
SSE = np.sum((y_test - predicted_labels_plus_one) ** 2)

# Calcula el pseudo-R cuadrado aproximado
pseudo_r_squared = 1 - (SSE / SST)

print("Pseudo-R cuadrado aproximado:", pseudo_r_squared)

print('------')
print(y_test)

#ayudame ahora a hacer las pruebas estadisticas al modelo de regresion ordinal
#https://www.statsmodels.org/dev/examples/notebooks/generated/ordinal_regression.html

#Datos ingresados desde un API.
dataPrediccion = {
    "Edad": 1,
    "CategoriaMunicipio": 1,
    "PesoNacer": 1,
    "vacunaPentavalente": 1,
    "tripleViral": 1,
    "Nutricion": 3,
    "Lactancia":1,
    "enfermedad": 2
}

print('-------------------------------------Prediccion PROBIT ---------------------------------:')
df_prediction = pd.DataFrame([dataPrediccion])
prediction=mod_prob.predict(res_prob.params,df_prediction)
print(prediction)


print('-------------------------------------Prediccion LOGIT ---------------------------------:')
df_prediction = pd.DataFrame([dataPrediccion])
prediction=mod_log.predict(res_log.params,df_prediction)
print(prediction)
