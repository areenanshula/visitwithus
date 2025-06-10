from django.urls import path
from . import  views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('signin/', views.signIn, name='signIn'),
    path('rooms/', views.rooms, name='rooms'),
]