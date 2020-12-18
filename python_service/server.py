"""Server: service that compute the test of python file"""

from flask import request, Flask, make_response
from os import environ
import subprocess
from filecmp import cmp

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

def run_test(test_info):
    with open("script.py", "w") as file:
        file.write(test_info["code"])
    
    with open("test_case.txt", "w") as file:
        file.write(test_info["case_tests"])

    with open("out.txt", "w+") as file:
        subprocess.call(["python", "./script.py"], stdout=file, stderr=file)
    
    result = cmp("test_case.txt", "out.txt", shallow=False)

    with open("out.txt", "r") as file:
        output = file.read()

    return result, output

@app.route('/test', methods=['POST', "GET"])
def exec_test():
    test_info = request.get_json()

    result, output = run_test(test_info)

    response = make_response({"output_test":f"test 1: {output}", 
                            "time":120,
                            "status": f"Accepted- {result}"}, 200)
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
