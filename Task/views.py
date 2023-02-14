from django.shortcuts import render
from .models import Item
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def MyTasksView(request):
    try:
        get_task=Item.objects.all()
    except Item.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TaskSerializer(get_task, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def TaskDetailsView(request,id):
    try:
        get_task=Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        pass
    elif request.method== 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    
