import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList, Task
from api.serializers import TaskSerializer, TaskListSerializer2


@csrf_exempt
def tasks_list(request):
    if request.method == 'GET':
        tasks = TaskList.objects.all()
        ser = TaskListSerializer2(tasks, many=True)
        return JsonResponse(ser.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        ser = TaskListSerializer2(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
        return JsonResponse(ser.errors)


@csrf_exempt
def tasks_detail(request, pk):
    try:
        task = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        ser = TaskListSerializer2(task)
        return JsonResponse(ser.data, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        ser = TaskListSerializer2(data=data, instance=task)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
        return JsonResponse(ser.errors)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({})


@csrf_exempt
def list_of_tasks(request, pk):
    try:
        task = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        tasks = task.task_set.all()
        ser = TaskSerializer(tasks, many=True)
        return JsonResponse(ser.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        ser = TaskSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data)
    elif request.method == 'DELETE':
        # task.delete()
        return JsonResponse({})