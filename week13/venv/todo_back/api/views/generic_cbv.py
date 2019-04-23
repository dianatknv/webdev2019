from api.models import Task, TaskList
from django.contrib.auth.models import User
from api.serializers import TaskListSerializer2, TaskListSerializer,TaskSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.http import Http404


class TaskLists(generics.ListCreateAPIView):
    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        return TaskList.objects.for_user_order_by_name(self.request.user)
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)


class TaskListTasks(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404
        return task_list.task_set.all()