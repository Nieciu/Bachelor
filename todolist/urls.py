from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from .views import RegisterView, FeaturesView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', RegisterView.as_view(), name='register'),
    path('features', FeaturesView.as_view(), name='features'),
    path('', views.home, name='home'),
    path('create-list', views.create_list, name='create-list'),
    path('login_redir', views.login_redir, name='login_redir'),
    path('all-lists', views.all_lists, name='all-lists')
]