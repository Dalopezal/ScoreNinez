from response import response, json_response
import pickle
import json


def load_model_and_predict(model_path, data):
    """
    Loads a pickled model and makes a prediction on the provided data.

    Returns:
        object: The prediction made by the model.
    """

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(data)

    return prediction


class Controller:

    def bienestar_material(self, request):

        content_length = int(request.headers['Content-Length'])
        datos_post = request.rfile.read(content_length)
        datos_json = json.loads(datos_post.decode('utf-8'))
        variable1 = datos_json['variable1']

        data = {
            'mensaje': variable1
        }

        predict = load_model_and_predict('../Models/BienestarMaterial.pkl', data)

        json_response(request, {
            'predict': predict
        })

    def bienestar_materno(self):
        response(self, b'<h1>Bienestar Materno</h1>')

    def cuidado(self):
        response(self, b'<h1>Cuidado</h1>')

    def salud(self):
        response(self, b'<h1>Salud</h1>')

    def seguridad(self):
        response(self, b'<h1>Seguridad</h1>')
