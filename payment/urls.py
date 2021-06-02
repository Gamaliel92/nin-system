from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [
    path('banks', views.fetch_banks, name="fetch_banks")
]