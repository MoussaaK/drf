from django.db import models


# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=100, default='default_task_name')
    description = models.CharField(max_length=1000, blank=True, default='')
    is_done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
