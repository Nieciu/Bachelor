from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ToDoListForm, ListItemForm, EditItemForm, DeleteForm
from .models import ToDoList, ListItem
from django.core.exceptions import PermissionDenied

@login_required(login_url="/login")
def home(request):
    lists = ToDoList.objects.filter(author=request.user).order_by("-updated_at")[:3]
    return render(request, 'todolist/home.html',{
        'lists': lists,
    })

@login_required(login_url="/login")
def create_list(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.author = request.user
            lista.save()
            return redirect(home)
    else:
        form = ToDoListForm()

    return render(request, 'todolist/create_list.html', {
        'form': form
    })
    

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {
            'form': form
            })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/register.html', {'form': form})

class FeaturesView(TemplateView):
    template_name = "features.html"

def login_redir(request):
    return redirect('home')

@login_required(login_url="/login")
def all_lists(request):

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            instance = ToDoList.objects.get(title = form.cleaned_data['delete'])
            instance.delete()
            return redirect(all_lists)
    else:
        form = DeleteForm()
    
    low_imp = ToDoList.objects.filter(author=request.user, importance=1).order_by("-updated_at")
    medium_imp = ToDoList.objects.filter(author=request.user, importance=2).order_by("-updated_at")
    high_imp = ToDoList.objects.filter(author=request.user, importance=3).order_by("-updated_at")
    return render(request,'todolist/all_lists.html', {
        "form": form,
        "low_imp": low_imp,
        "medium_imp": medium_imp,
        "high_imp": high_imp
    })
@login_required(login_url="/login")
def single_list(request, slug):

    project = ToDoList.objects.get(slug=slug)

    if project.author != request.user:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            instance = ListItem.objects.get(todo = form.cleaned_data['delete'])
            instance.delete()
            return redirect(project, slug)
    else:
        form = DeleteForm()
    
    return render(request, 'todolist/single_list.html',{
        "form": form,
        "project": project
    })

@login_required(login_url="/login")
def single_item(request,slug):
    project = ToDoList.objects.filter(author=request.user, importance=1).order_by("-updated_at")
    if project.author != request.user:
        raise PermissionDenied
    return render(request, 'todolist/single_list.html',{
        "project": project
    })

@login_required(login_url="/login")
def create_item(request, slug):
    project = ToDoList.objects.get(slug=slug)
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.todolist = project
            item.save()
            return redirect(single_list, slug)
    else:
        form = ListItemForm()

    return render(request, 'todolist/create_list.html', {
        'form': form
    })

@login_required(login_url="/login")
def edit_item(request, slug, slug_item):
    item = ListItem.objects.get(slug_item=slug_item)
    if request.method == 'POST':
        form = EditItemForm(request.POST)
        if form.is_valid():
            item.todo = form.cleaned_data['todo']
            item.is_done = form.cleaned_data['is_done']
            item.save()
            return redirect(single_list, slug)
    else:
        form = EditItemForm()
    return render(request, 'todolist/edit_item.html', {
        'form': form
    })

# @login_required(login_url="/login")
# def delete_item(request, slug):
#     project = ToDoList.objects.get(slug=slug)
#     if request.method == 'POST':
#         form = ListItemForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.todolist = project
#             item.save()
#             return redirect(single_list, slug)
#     else:
#         form = ListItemForm()

#     return render(request, 'todolist/delete_item.html', {
#         'form': form
#     })
