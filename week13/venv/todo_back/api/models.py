from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User


class TaskListManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user).order_by('name')


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = TaskListManager()

    class Meta:
            verbose_name = 'TaskList'
            verbose_name_plural = 'TaskLists'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    due_on = models.DateTimeField(null=True) #created_at + timedelta(days=7)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created at': self.created_at,
            'due on': self.due_on,
            'status': self.status,
        }