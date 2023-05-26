from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

# class Login(LoginView):
#     template_name: 'todolist/login.html'
