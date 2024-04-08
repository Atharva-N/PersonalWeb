from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about',views.abt, name='about'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name = 'contact'),
    path('about.html',views.abt, name='about'),
    path('projects.html', views.project, name='project'),
    path('contact.html', views.contact, name = 'contact'),
    path('home', views.index),
    path('home.html', views.index),
]

