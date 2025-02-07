from django.urls import path
from . import views

urlpatterns = [
    path('register_task', views.register_task, name='register_task'),
    path('task_list', views.task_list, name='task_list'),
]
