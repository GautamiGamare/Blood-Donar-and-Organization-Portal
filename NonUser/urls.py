from django.contrib import admin
from django.urls import path
from NonUser import views

urlpatterns = [
    path('',views.showIndex,name="main"),
    path('search_details/',views.search_details,name="search_details"),
    path('result/',views.result,name="result"),
    path('nonuser_msg/',views.nonuser_msg,name="nonuser_msg"),
]
