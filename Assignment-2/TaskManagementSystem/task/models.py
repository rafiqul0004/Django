from django.db import models
from category.models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    taskTitle=models.CharField(max_length=50)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)
    category=models.ManyToManyField(TaskCategory)

    def __str__(self) -> str:
        return self.taskTitle