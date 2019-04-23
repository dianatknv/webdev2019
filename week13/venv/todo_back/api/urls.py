from django.urls import path
from api import views

# urlpatterns = [
#     path('tasklist/', views.tasks_list),
#     path('tasklist/<int:pk>/', views.tasks_detail),
#     path('tasklist/<int:pk>/task/', views.list_of_tasks),
#     # path('tasklist/<int:pk>/task/<int:pk/>', views.list_of_tasks)
# ]

urlpatterns = [
    path('task_lists/', TaskList.as_view()),
    path('task_lists/<int:pk>/', TaskListDetail.as_view()),
    path('users/', UserList.as_view()),
    path('login/', login),
    path('logout/', logout),
    path('task_lists/<int:pk>/tasks/', TaskListTasks.as_view())
]