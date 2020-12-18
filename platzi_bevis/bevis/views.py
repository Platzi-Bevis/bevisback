"""View to manage the tests endpoint"""

#Django
import requests

#DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#utils
from bevis.mocks.mocks import tests

def get_result(data, case_tests):
    try:
        r = requests.post("http://python:5000/test", json= {
            "language": data["language"],
            "code": data["code"],
            "case_tests":case_tests
        })
        return r.json()
    except Exception as e:
        print(e)
        return e


@api_view(["GET", "POST"])
def get_test(request, id_course, id_material):

    if request.method == "GET":
        return Response({"Bevis API version": "1.0", 
                        "id_course": id_course,
                        "id_material": id_material,
                        "test": tests["test1"]}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        response = get_result(request.data, tests["test1"]["case_tests"])
        return Response({"data":response}, status=status.HTTP_200_OK)