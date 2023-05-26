from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='todolist/login.html'), name='login')
]
