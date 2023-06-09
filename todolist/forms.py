from .models import ToDoList, ListItem
from django import forms

class ToDoListForm(forms.ModelForm):
    
    class Meta:
        model = ToDoList
        fields = ("title", "importance",)

class ListItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ("todo",)

class EditItemForm(forms.ModelForm):

    class Meta:
        model = ListItem
        fields = ("todo", "is_done",)

class DeleteForm(forms.Form):
    delete = forms.CharField()

        
