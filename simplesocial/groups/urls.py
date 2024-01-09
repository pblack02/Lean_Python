from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('create/', views.CreateGroup.as_view(), name='create'),
    path('posts/<slug>/', views.SingleGroup.as_view(), name='single'),
    path('join/<slug>/', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGroup.as_view(), name='leave'),
    path('<slug>/delete', views.DeleteGroup.as_view(), name='delete_group'),
]
