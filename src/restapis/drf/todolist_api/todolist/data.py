from src.restapis.drf.todolist_api.todolist.models import Task
from src.restapis.drf.todolist_api.todolist.serializers import TaskSerializer


class Payload:
    task = Task(name='Learn Django', description='Tutorials to learn and master django', is_done=True)
    task.save()

    task = Task(name='Learn Java', description='Tutorials to learn and master Spring Boot', is_done=True)
    task.save()

    task = Task(name='Learn Clean Code', description='On my way to read Uncle BOB\'s Clean Code', is_done=False)
    task.save()

    serializer = TaskSerializer(task)
