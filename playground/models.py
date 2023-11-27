from django.db import models


# Create your models here.

# class Tasks(models.Model):
#     name = models.CharField(max_length=100)
#     completed = models.BooleanField(default=False)
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField(auto_now_add=True)
#     rare = models.SmallIntegerField(default=0)

class Task(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    rare = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name