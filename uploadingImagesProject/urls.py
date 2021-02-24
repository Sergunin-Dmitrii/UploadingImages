from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('uploadapp.urls')),
    path('api-auth', include('rest_framework.urls')),
]

if settings.DEBUG:
 urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)