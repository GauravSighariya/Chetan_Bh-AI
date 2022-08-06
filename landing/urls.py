from django import views
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('generate-blog-topic',views.blogSection, name='blogSection'),
]
