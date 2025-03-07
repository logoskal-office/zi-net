from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user_auth import views as user_auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__', include('django_browser_reload.urls')),
   # path("silk/",include('silk.urls', namespace='silk')),
    path('', include('display.urls')),
    path('api/', include('api.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('auth/', include('user_auth.urls')),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)