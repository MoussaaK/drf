from .models import Task
from .serializers import TaskSerializer


class Payload:
    task = Task(name='Learn Python', description='Tutorials to learn and master django', is_done=True)
    task.save()

    task = Task(name='Learn Java', description='Tutorials to learn and master Spring Boot', is_done=True)
    task.save()

    task = Task(name='Learn Clean Code', description='On my way to read Uncle BOB\'s Clean Code', is_done=True)
    task.save()

    serializer = TaskSerializer(task)
