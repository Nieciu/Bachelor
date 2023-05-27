from django.contrib import admin

from .models import ToDoList, ListItem, ListTag

admin.site.register(ToDoList)
admin.site.register(ListTag)
admin.site.register(ListItem)

# Register your models here.
