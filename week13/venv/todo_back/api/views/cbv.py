from api.models import Task, TaskList
from api.serializers import TaskListSerializer2, TaskListSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


class TaskLists(APIView):

    def get(self, request):
        taskLists = TaskList.objects.all()
        serializer = TaskListSerializer2(taskLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListDetail(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_list = self.get_object(pk)
        task_list.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class Task(APIView):

    def get_object(self, pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist as e:
            raise Http404

    def get(self,request, pk):
        task_list = self.get_object(pk)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)