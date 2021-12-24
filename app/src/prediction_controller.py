from flask import request, Blueprint
from flask_expects_json import expects_json
import pickle
from src import utils

prediction_app = Blueprint('prediction_app', __name__, url_prefix='/api/v1')

# To Open Model
with open("../model/model.sav", 'rb') as model:
    pipeline = pickle.load(model)


@prediction_app.route('/predict', methods=['POST'])
@expects_json(utils.PREDICTION_SCHEMA)
def single_prediction():
    try:
        data = request.get_json()
        response = {
            "status": 200,
            "predicted_value": pipeline
            .predict([utils.get_json_data(data)])[0][0]
        }
    except Exception as e:
        response = {
            'status': type(e),
            "response": str(e)
        }

    return response
