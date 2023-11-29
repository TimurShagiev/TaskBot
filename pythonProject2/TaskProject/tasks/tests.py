from django.test import TestCase
from .models import Task

class Test(TestCase):
    def test_tasks(self):
        task = Task.objects.create(name="Make lunch", importance="2")
        self.assertEqual(task.get_fields(), "Make lunch, 2")

    def test_importance(self):
        task = Task.objects.create(name="Make lunch", importance="2")
        self.assertEqual(task.importance, "2")

    def test_name(self):
        task = Task.objects.create(name="Make lunch", importance="2")
        self.assertEqual(task.name, "Make lunch")
# Create your tests here.
