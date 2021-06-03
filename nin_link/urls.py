from django.urls import path
from . import views

app_name = "nin_link"

urlpatterns = [
    path('', views.nin_requests, name="linked_nin"),
    path('nin/link', views.nin_linkage, name="nin_linkage")
]