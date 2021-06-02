from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import requests

# Create your views here.
@api_view(["GET"])
def fetch_banks(request):
    res = requests.get(
        "https://api.paystack.co/bank",
        headers={
            "Content-Type": "aplication/json",
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET}"
        }
    )
    return Response(res.json(), status=status.HTTP_200_OK)

