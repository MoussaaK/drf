from django.urls import path
from . import views

urlpatterns = [
    path('todolist/tasks/', views.task_list),
    path('todolist/tasks/<int:pk>/', views.task_detail),
]
