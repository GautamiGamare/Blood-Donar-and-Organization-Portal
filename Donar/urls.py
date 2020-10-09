from django.urls import path
from BloodPortal import settings
from Donar import views
from django.conf.urls.static import static

urlpatterns = [
    path('donar_login/',views.donar_login,name='donar_login'),
    path('donar_registration/',views.donar_registration,name='donar_registration'),
    path('donar_welcome/',views.donar_welcome,name="donar_welcome"),
    path('save_donar/',views.save_donar,name="save_donar"),
    path('validate_donar/',views.validate_donar,name="validate_donar"),
    path('show_msg/',views.show_msg,name="show_msg"),
    path('msg_donar/',views.msg_donar,name="msg_donar"),
    path('make_msg_read/',views.make_msg_read,name="make_msg_read"),
    path('reply_msg/',views.reply_msg,name="reply_msg"),
    path('save_donar_msg1/',views.save_donar_msg1,name="save_donar_msg1"),
    path('save_admin_msg1/',views.save_admin_msg1,name="save_admin_msg1"),
    path('msg_admin/',views.msg_admin,name="msg_admin"),
    path('donar_logout/',views.donar_logout,name="donar_logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
