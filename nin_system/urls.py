"""nin_system URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payment.urls')),
    path('', include('nin_link.urls')),
    path('', include('components.urls'))
]
