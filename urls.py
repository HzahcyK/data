from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.shortcuts import HttpResponse, redirect, render
from . import views


urlpatterns = [
    path('read_count/', views.read_count),


]
