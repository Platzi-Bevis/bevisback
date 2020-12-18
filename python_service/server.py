"""Server: service that compute the test of python file"""

from flask import request, Flask, make_response
import json
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

@app.route('/test', methods=['POST', "GET"])
def exec_test():
    test_info = request.get_json()

    response = make_response({"Information":test_info}, 200)
    return response 


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
