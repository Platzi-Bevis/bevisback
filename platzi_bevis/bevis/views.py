"""View to manage the tests endpoint"""

#Django
from django.shortcuts import render

#DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#utils
from bevis.mocks.mocks import tests

@api_view(['GET', 'POST'])
def test(request, id_course, id_material):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        print(id_course, id_material)
        return Response({"Bevis API version": "1.0", 
                        "id_course": id_course,
                        "id_material": id_material,
                        "test": tests["test1"]}, status=status.HTTP_200_OK)
