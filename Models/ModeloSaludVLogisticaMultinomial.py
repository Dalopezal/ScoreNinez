"""
    Clase Utilizada para el desarrollo del modelo de aprendizaje para la dimension salud
    LogisticRegression Multinomial
"""

import pickle
import pandas as pd
from CargueDatos import *
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from scipy.stats import chi2_contingency

#Datos Expertos
datosExpertos=CargueDatos.ExpertosSaludDestino()

y = datosExpertos["Riesgo SA"]   #variable Ordinal dependiente
X = datosExpertos.drop("Riesgo SA", axis=1)

ros = RandomOverSampler(random_state=42)

X_resampled, y_resampled = ros.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.30, random_state=42)

modelo = LogisticRegression(penalty="l2", solver="lbfgs", multi_class="multinomial", max_iter=1000)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Exactitud:", accuracy)


# Confusion Matrix
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

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

def chi_square_test(X_test, y_test, feature_name):
    chi2, pval, dof, expected = chi2_contingency(pd.crosstab(X_test[feature_name], y_test))
    print(f"\nChi-Square Test for {feature_name}:")
    print(f"p-value: {pval}")


chi_square_test(X_test, y_test, "CategoriaMunicipio")
chi_square_test(X_test, y_test, "PesoNacer")
chi_square_test(X_test, y_test, "vacunaPentavalente")
chi_square_test(X_test, y_test, "tripleViral")
chi_square_test(X_test, y_test, "Nutricion")
chi_square_test(X_test, y_test, "Lactancia")
chi_square_test(X_test, y_test, "enfermedad")


"""
CategoriaMunicipio: Existe una relación estadísticamente significativa entre la variable "CategoriaMunicipio" y la variable dependiente . Esto se debe a que el valor de p-valor (0.0396) es menor que el nivel de significancia común (por ejemplo, 0.05). Esto significa que es poco probable que observemos este resultado debido al azar.

PesoNacer: La evidencia sugiere que no existe una relación estadísticamente significativa entre el "PesoNacer" y la variable dependiente. Esto se debe a que el valor de p-valor (0.0629) es ligeramente superior al nivel de significancia común (por ejemplo, 0.05). Sin embargo, el valor está lo suficientemente cerca como para que pueda valer la pena investigar más a fondo esta relación, dependiendo de su estudio y cuánto esté dispuesto a correr el riesgo de un falso positivo.

vacunaPentavalente, tripleViral, Lactancia: De manera similar a "PesoNacer", los valores p para "vacunaPentavalente" (0.1100), "tripleViral" (0.0953) y "Lactancia" (0.1700) sugieren que no hay una relación estadísticamente significativa con la variable dependiente.

Nutricion: Existe una relación estadísticamente significativa entre "Nutricion" y la variable dependiente. El valor de p-valor (0.0041) es mucho menor que el nivel de significancia común, lo que indica una relación poco probable debido al azar.

enfermedad:  Existe una relación estadísticamente significativa entre "enfermedad" y la variable dependiente. El valor de p-valor (0.0269) es menor que el nivel de significancia común.

"""


### Save model PKL
pck_file = "SaludVMultinomial.pkl"
with open(pck_file, 'wb') as file:
    pickle.dump(modelo, file)