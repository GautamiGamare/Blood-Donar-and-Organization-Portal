from django.urls import path,include
from django.views.generic import TemplateView,View
from django.conf.urls.static import static
from BloodPortal import settings


urlpatterns = [
    path('admin/',include("Admin.urls")),
    path('donar/',include("Donar.urls")),
    path('',include("NonUser.urls")),
    path('organization/',include("Organization.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
