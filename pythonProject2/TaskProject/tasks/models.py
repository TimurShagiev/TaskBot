from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    importance = models.IntegerField()


# Create your models here.
