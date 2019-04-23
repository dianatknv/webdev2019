from rest_framework.decorators import api_view
from api.models import Task, TaskList
from api.serializers import TaskListSerializer2, TaskListSerializer,TaskSerializer
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def show_taskLists(request):
    if request.method == 'GET':
        taskLists = TaskList.objects.all()
        serializer = TaskListSerializer2(taskLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def show_current_taskList(request, pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({{'error': str(e)}}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TaskListSerializer(taskList)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=taskList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        taskList.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def show_current_tasks(request, pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({{'error': str(e)}}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        tasks = taskList.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'bad request'}, status=status.HTTP_404_NOT_FOUND)