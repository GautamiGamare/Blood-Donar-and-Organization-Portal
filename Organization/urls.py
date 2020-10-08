from django.urls import path
from Organization import views

urlpatterns = [
    path('login/',views.login,name="login_org"),
    path('org_registration/',views.org_registration,name="org_registration"),
    path('save_org/',views.save_org,name="save_org"),
    path('validate_org/',views.validate_org,name="validate_org"),
    path('welcome_org/',views.welcome_org,name="welcome_org"),
    path('check_admin_msg/',views.check_admin_msg,name="check_admin_msg"),
    path('reply_message1/',views.reply_message1,name="reply_message1"),
    path('msg_read1/',views.msg_read1,name="msg_read1"),
    path('send_msg_admin/',views.send_msg_admin,name="send_msg_admin"),
    path('org_logout/',views.org_logout,name="org_logout"),
]
