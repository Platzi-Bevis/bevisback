"""View to manage the tests endpoint"""

#Django
from django.shortcuts import render

#DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return Response({"API versión": "1"}, status=status.HTTP_200_OK)
