import re
from urllib.parse import parse_qs

from response import response, json_response
import pickle
import pandas as pd
import json


def load_model_and_predict(model_path, data):
    """
    Loads a pickled model and makes a prediction on the provided data.

    Returns:
        object: The prediction made by the model.
    """

    df_prediction = pd.DataFrame([data])

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(df_prediction)

    return prediction[0]


class Controller:

    def bienestar_material(self, request):
        content_length = int(request.headers.get('Content-Length', 0))
        raw_data = request.rfile.read(content_length)

        data = parse_qs(raw_data.decode('utf-8'))

        data_end = {
            "age": int(data['age'][0]),
            "category": 1,
            "rooms": int(data['rooms'][0]),
            "total_people": int(data['total_people'][0]),
            "income": int(data['income'][0]),
            "public_service": int(data['public_service'][0])
        }

        predict = load_model_and_predict('../Models/Output/BienestarMaterialRF.pkl', data_end)

        json_response(request, {"prediction": int(predict)})

    def bienestar_materno(self):
        response(self, b'<h1>Bienestar Materno</h1>')

    def cuidado(self):
        response(self, b'<h1>Cuidado</h1>')

    def salud(self, request):
        response(request, b'<h1>Salud</h1>')

    def seguridad(self):
        response(self, b'<h1>Seguridad</h1>')
