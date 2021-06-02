from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import requests

# Create your views here.
@api_view(["GET", "POST"])
def page_404(request, url):
    res = {
        "status": "error",
        "message": "invalid endpoint"
    }
    return Response(res, status=status.HTTP_404_NOT_FOUND)