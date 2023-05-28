from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify


class ToDoList(models.Model):
    PRIORITY_CHOICES = (
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    made_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    importance = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    slug = models.SlugField(default='', null=False)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ListItem(models.Model):
    todo = models.CharField(max_length=100, unique=True)
    is_done = models.BooleanField(default=False)
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE, name='todolist')
    slug_item = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug_item = slugify(self.todo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.todo
    




# Create your models here.
