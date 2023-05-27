from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class ListImportance(models.Model):
    importance = models.CharField(max_length=50)
    number = models.IntegerField(default=1, validators=[
        MaxValueValidator(1),
        MinValueValidator(3)
    ])
    def __str__(self):
        return self.importance
    
class ListItem(models.Model):
    todo = models.CharField(max_length=500)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.todo
    
class ListTag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    
class ToDoList(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True)
    list_item = models.ForeignKey(ListItem, on_delete=models.SET_NULL, null=True)
    list_tag = models.ForeignKey(ListTag, on_delete=models.SET_NULL, null=True)
    importance = models.OneToOneField(ListImportance, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title






# Create your models here.
