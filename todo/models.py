from django.db import models

# Create your models here.
class Todo(models.Model):
    todoItem = models.CharField(max_length=50)
    dateToComplete = models.DateField()