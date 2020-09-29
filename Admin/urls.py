from django.contrib import admin
from django.urls import path
from Admin import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="admin/login.html"),name="login"),
    path('validate_login/',views.validate_login,name="validate_login"),
    path('donar_details/',views.donar_details,name="donar_details"),
    path('org_details/',views.org_details,name="org_details"),
    path('give_access/',views.give_access,name="give_access"),
]
