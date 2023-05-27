from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import RegisterView, FeaturesView, HomeView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='todolist/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('features/', FeaturesView.as_view(), name='features'),
    path('home/', HomeView.as_view(), name='home'),
]