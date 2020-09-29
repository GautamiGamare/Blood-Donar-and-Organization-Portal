from django.urls import path
from BloodPortal import settings
from Donar import views
from django.conf.urls.static import static

urlpatterns = [
    path('donar_login/',views.donar_login,name='donar_login'),
    path('donar_registration/',views.donar_registration,name='donar_registration'),
    path('save_donar/',views.save_donar,name="save_donar"),
    path('validate_donar/',views.validate_donar,name="validate_donar"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
