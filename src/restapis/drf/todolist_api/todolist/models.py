from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, default='default_task_name')
    description = models.CharField(max_length=1000, blank=True, default='')
    complete = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id', 'date')
