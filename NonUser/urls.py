from django.contrib import admin
from django.urls import path
from NonUser import views

urlpatterns = [
    path('',views.showIndex,name="main"),
]
