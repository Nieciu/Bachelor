from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'todolist/register.html', {
            'form': form
            })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        return render(request, 'todolist/register.html', {'form': form})
    
class HomeView(TemplateView):
    template_name = "home.html"

class FeaturesView(TemplateView):
    template_name = "features.html"


