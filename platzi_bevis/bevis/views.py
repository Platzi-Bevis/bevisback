"""View to manage the tests endpoint"""

#Django
import requests

#DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#utils
from bevis.mocks.mocks import tests

def get_result(data):
    try:
        r = requests.post("http://python:5000/test", json= {
            "language": "1",
            "code": "def add(a,b): return a+b"
        })
        print(r.json())
    except Exception as e:
        print(e)


@api_view(["GET"])
def get_test(request, id_course, id_material):
    print(id_course, id_material)
    return Response({"Bevis API version": "1.0", 
                    "id_course": id_course,
                    "id_material": id_material,
                    "test": tests["test1"]}, status=status.HTTP_200_OK)



@api_view(["POST"])
def exec_test(request):
    get_result(request.data)
    return Response({"data":request.data}, status=status.HTTP_200_OK)
