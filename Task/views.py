from django.shortcuts import render
from .models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def MyTasksView(request):
    try:
        get_task=Task.objects.all()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TaskSerializer(get_task, many=True)
        return Response(status=status.HTTP_200_OK
    
