from flask import Flask, jsonify, request

from src.calc.pears_coef_corr import pearson_corr_coef
from src.db.db import add_data_to_db
from src.db.db import get_data_from_db
from src.service.schemas import DataInModel

app = Flask(__name__)


@app.route('/get/correlation', methods=['get'])
def get_correlation():
    x_data_type_in = request.args.get("x_data_type")
    y_data_type_in = request.args.get("y_data_type")
    user_id_in = request.args.get("user_id")
    data_from_db = get_data_from_db(user_id_in)
    if x_data_type_in == data_from_db['x_data_type'] and y_data_type_in == data_from_db['y_data_type']:
        x_date = []
        x_value = []
        for element in data_from_db['x']:
            x_date.append(element['date'])
            x_value.append(element['value'])
        y_date = []
        y_value = []
        for element in data_from_db['y']:
            y_date.append(element['date'])
            y_value.append(element['value'])
        import numpy as np
        x_value = np.array(x_value)
        y_value = np.array(y_value)
        pears_corr_coef, p_value = pearson_corr_coef(x_value, y_value)
        return jsonify({
            "user_id": int(user_id_in),
            "x_data_type": str(x_data_type_in),
            "y_data_type": str(y_data_type_in),
            "correlation": {
                "value": float(pears_corr_coef),
                "p_value": float(p_value),
            }
        })
    return "Wrong request, please try again. code 404"


@app.route('/post/calculate', methods=['POST'])
def post_correlation() -> None:
    request_data = request.get_json()
    request_data_in_model = DataInModel(user_id=request_data['user_id'], data=request_data['data'])
    add_data_to_db(request_data_in_model)
    return 'data added successfully'
