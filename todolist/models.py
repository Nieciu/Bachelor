from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ListTag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    
class ToDoList(models.Model):
    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    list_tag = models.ForeignKey(ListTag, on_delete=models.SET_NULL, null=True)
    importance = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    

    def __str__(self):
        return self.title

class ListItem(models.Model):
    todo = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo
    




# Create your models here.
