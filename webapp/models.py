from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.DateTimeField(default=False)
    created = models.DateTimeField(auto_now_add=True)
