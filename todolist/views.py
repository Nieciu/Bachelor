from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import ToDoListForm

@login_required(login_url="/login")
def home(request):
    return render(request, 'todolist/home.html')

@login_required(login_url="/login")
def create_list(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
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

def all_lists(request):
    return render(request,'todolist/all_lists.html')

