"""Server: service that compute the test of python file"""

from flask import request, Flask, make_response
from os import environ
from filecmp import cmp
import subprocess
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

def run_test(test_info):
    with open("script.py", "w") as file:
        file.write(test_info["code"])
    
    with open("test_case.txt", "w") as file:
        file.write(test_info["case_tests"].replace('\r', ''))

    current = time.time()

    with open("out.txt", "w+") as file:
        subprocess.call(["python", "./script.py"], stdout=file, stderr=file)
    
    time_elapsed = time.time() - current

    result = cmp("test_case.txt", "out.txt", shallow=False)

    with open("out.txt", "r") as file:
        output = file.read()

    return result, output, round(time_elapsed,3)

@app.route('/test', methods=['POST'])
def exec_test():
    test_info = request.get_json()

    result, output, time_elapsed = run_test(test_info)

    response = make_response({"output_test":output, 
                            "time":f"{time_elapsed} s",
                            "status": result}, 200)
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
