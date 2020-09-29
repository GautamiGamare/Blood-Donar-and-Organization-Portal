from django.urls import path
from Organization import views

urlpatterns = [
    path('login/',views.login,name="login_org"),
    path('org_registration/',views.org_registration,name="org_registration"),
    path('save_org/',views.save_org,name="save_org"),
    path('validate_org/',views.validate_org,name="validate_org"),
]
