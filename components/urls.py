from django.urls import path
from . import views

app_name = "components"

urlpatterns = [
    path('<str:url>', views.page_404, name="page_404")
]