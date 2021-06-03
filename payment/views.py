from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import random, string, requests
from .models import MakePayment, PaymentToken, ApiPrice

# Create your views here.
def banks_fetcher():
    return requests.get(
        "https://api.paystack.co/bank",
        headers={
            "Content-Type": "aplication/json",
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET}"
        }
    ).json()

@api_view(["GET"])
def fetch_banks(request):
    res = banks_fetcher()
    return Response(res, status=status.HTTP_200_OK)

@api_view(["POST"])
def make_payment(request):
    if request.method == "POST":
        try:
            phone_number = request.data['phone_number']
            bank_code = request.data['bank_code']
            account_number = request.data['account_number']

            available_bank_codes = [bank["code"] for bank in banks_fetcher()["data"]]
            if bank_code not in available_bank_codes:
                code_err = {
                    "status":"error",
                    "message": "Invalid bank code"
                }
                return Response(code_err, status=status.HTTP_400_BAD_REQUEST)
            else:
                if phone_number in [payer.phone_number for payer in MakePayment.objects.all()]:
                    phone_exists = {
                        "status": "error",
                        "message": "Your phone number has already been linked with a NIN"
                    }
                    return Response(phone_exists, status=status.HTTP_403_FORBIDDEN)
                all_alnum = string.ascii_letters+string.digits+"_"
                auth_code = 'NIN_'+''.join(random.sample(all_alnum, 50))

                price = ApiPrice.objects.first() if ApiPrice.objects.all().exists() else "500"

                """
                Write the code/algorithm to withdraw amount of the variable "price" above if there's a payment gateway to implement price charge from user.
                """

                payment = MakePayment.objects.create(
                    phone_number=phone_number,
                    price=price,
                    bank=bank_code,
                    account_number=account_number
                )
                PaymentToken.objects.create(
                    payer=payment,
                    secret=auth_code
                )
                success_res = {
                    "status": "success",
                    "message": "Your payment was successful. Note that your secret key can only be used once to link NIN with the phone number you provided, and can't be retrived once this response is closed.",
                    "data": {
                        "amount": price,
                        "currency": "NGN",
                        "secret_key": auth_code
                    }
                }
                return Response(success_res, status=status.HTTP_200_OK)
        except KeyError:
            keyerr = {
                "status": "error",
                "message": "phone_number, bank_code, account_number is required."
            }
            return Response(keyerr, status=status.HTTP_400_BAD_REQUEST)

