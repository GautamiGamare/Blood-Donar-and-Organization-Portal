from django.contrib import admin
from django.urls import path
from Admin import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name="admin/login.html"),name="login"),
    path('welcome_admin/',views.welcome_admin,name="welcome_admin"),
    path('validate_login/',views.validate_login,name="validate_login"),
    path('donar_details/',views.donar_details,name="donar_details"),
    path('org_details/',views.org_details,name="org_details"),
    path('give_access/',views.give_access,name="give_access"),
    path('nonuser_msg_display/',views.nonuser_msg_display,name="nonuser_msg_display"),
    path('msg_display/',views.msg_display,name="msg_display"),
    path('reply_message/',views.reply_message,name="reply_message"),
    path('msg_read/',views.msg_read,name="msg_read"),
    path('send_nonuser_email/',views.send_nonuser_email,name="send_nonuser_email"),
    path('send_msg_donar/',views.send_msg_donar,name="send_msg_donar"),
    path('send_msg_org/',views.send_msg_org,name="send_msg_org"),
    path('save_donar_msg/',views.save_donar_msg,name="save_donar_msg"),
    path('save_org_msg/',views.save_org_msg,name="save_org_msg"),
    path('logout/',views.logout,name="logout"),
]
