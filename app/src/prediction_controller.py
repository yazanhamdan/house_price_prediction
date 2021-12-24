from flask import request, Blueprint, jsonify
from flask_expects_json import expects_json
import pickle
from src import utils
import pandas as pd
import numpy as np

prediction_app = Blueprint('prediction_app', __name__, url_prefix='/api/v1')

# To Open Model
with open("../../app/model/model.sav", 'rb') as model:
    pipeline = pickle.load(model)


@prediction_app.route('/predict', methods=['POST'])
@expects_json(utils.PREDICTION_SCHEMA)
def single_prediction():
    try:
        data = request.json
        response = {
            "status": 200,
            "predicted_value": np.expm1(pipeline.predict(
                pd.json_normalize(data))[0])
        }
    except Exception as e:
        response = {
            'status': type(e),
            "response": str(e)
        }

    return jsonify(response)
