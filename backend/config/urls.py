from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.main.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
]
