from flask import Flask
from src import prediction_controller
import os
app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.register_blueprint(prediction_controller.prediction_app)
    app.run(debug=True, port=port, host="0.0.0.0")
