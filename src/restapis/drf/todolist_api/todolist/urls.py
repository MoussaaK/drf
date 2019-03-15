from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('todolist/tasks/', views.TaskList.as_view()),
    path('todolist/tasks/<int:pk>/', views.TaskDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
