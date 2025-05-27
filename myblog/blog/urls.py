from django.urls import path
from . import  views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('places/', views.places, name='places'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('signin/', views.signIn, name='signIn')
]