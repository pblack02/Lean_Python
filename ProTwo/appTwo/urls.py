from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
]