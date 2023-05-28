from django.urls import path, include
from . import views
from .views import RegisterView, FeaturesView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', RegisterView.as_view(), name='register'),
    path('features', FeaturesView.as_view(), name='features'),
    path('', views.home, name='home'),
    path('create-list', views.create_list, name='create-list'),
    path('login_redir', views.login_redir, name='login_redir'),
    path('all-lists', views.all_lists, name='all-lists'),
    path('all-lists/<slug:slug>', views.single_list, name='project'),
    path('all-lists/<slug:slug>/create-item', views.create_item, name='create-item'),
    # path('all-lists/<slug:slug>/delete-item', views.delete_item, name='delete-item'),
    path('all-lists/<slug:slug>/<slug:slug_item>', views.edit_item, name='edit-item'),
]