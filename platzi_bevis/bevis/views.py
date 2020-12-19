"""View to manage the tests endpoint"""

# Django
import requests

# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Models
from bevis.models.practice_tests import Practice_tests

# Serializers
from bevis.serializers.tests_practice import TestPracticeModelSerializer

# utils
from bevis.mocks.mocks import tests


def get_result(data, case_tests):

    try:
        if data["language"] == "JS":
            try:
                r = requests.post(
                    "http://python:5000/test",
                    json={
                        "language": data["language"],
                        "code": data["code"],
                        "case_tests": f"{case_tests}\n",
                    },
                )
                return r.json()
            except Exception as e:
                print(e)
                return e
        elif data["language"] == "PY":
            try:
                r = requests.post(
                    "http://python:5000/test",
                    json={
                        "language": data["language"],
                        "code": data["code"],
                        "case_tests": f"{case_tests}\n",
                    },
                )
                return r.json()
            except Exception as e:
                print(e)
                return e
    except Exception as e:
        return e


@api_view(["GET", "POST"])
def get_test(request, id_course, id_material):

    try:
        if request.method == "GET":
            query_tests = Practice_tests.objects.filter(id_material=id_material)
            result_tests = TestPracticeModelSerializer(query_tests, many=True).data
            try:
                result_tests[0]
            except Exception as e:
                return Response(
                    {
                        "Bevis API version": "1.0",
                        "id_course": id_course,
                        "id_material": id_material,
                        # "test": tests["test1"]}, status=status.HTTP_200_OK)
                        "test": {},
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {
                    "Bevis API version": "1.0",
                    "id_course": id_course,
                    "id_material": id_material,
                    # "test": tests["test1"]}, status=status.HTTP_200_OK)
                    "test": result_tests[0],
                },
                status=status.HTTP_200_OK,
            )
        elif request.method == "POST":
            query_tests = Practice_tests.objects.filter(id_material=id_material)
            result_tests = TestPracticeModelSerializer(query_tests, many=True).data
            try:
                result_tests[0]
            except Exception as e:
                return Response(
                    {
                        "data": {
                            "output_test": "No tests for this material",
                            "status": False,
                            "time": "0.0 s",
                        }
                    },
                    status=status.HTTP_200_OK,
                )

            response = get_result(request.data, result_tests[0]["case_tests"])
            return Response({"data": response}, status=status.HTTP_200_OK)
    except Exception as e:
        return e

