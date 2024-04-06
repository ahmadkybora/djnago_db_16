from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Crud
from .serializers import CrudSerializer
from rest_framework import status

@api_view(['GET'])
def index(request):
    cruds = Crud.objects.all()
    serializer = CrudSerializer(cruds, many=True, context = { "request": request })
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def show(request, pk):
    try:
        crud = Crud.objects.get(pk=pk)
    except Crud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CrudSerializer(crud, context={ "request": request })
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def store(request):
    serializer = CrudSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.error, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST'])
def update(request, pk):
    try:
        serializer = Crud.objects.get(pk=pk)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
    except Crud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    