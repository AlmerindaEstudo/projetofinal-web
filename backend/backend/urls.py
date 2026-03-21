from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # tudo vem do core
    path('', include('core.urls')),
]