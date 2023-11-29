from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    importance = models.IntegerField()

    def get_fields(self):
        return f"{self.name}, {self.importance}"


# Create your models here.
