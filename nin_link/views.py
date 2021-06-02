from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
from payment.models import PaymentToken
from .models import LinkNin

# Create your views here.
@api_view(["POST"])
def nin_linkage(request):
    if request.method == "POST":
        auth_key = request.META.get("HTTP_AUTHORIZATION")
        if not auth_key:
            no_auth = {
                "status": "error",
                "message": "No Authorization header found"
            }
            return Response(no_auth, status=status.HTTP_401_UNAUTHORIZED)
        else:
            auth_key = auth_key.replace("Bearer ", "")
            if auth_key not in [token.secret for token in PaymentToken.objects.all()]:
                invalid_auth = {
                    "status": "error",
                    "message": "Invalid Authorization header. Make payment and get a token for Authorization"
                }
                return Response(invalid_auth, status=status.HTTP_402_PAYMENT_REQUIRED)
            else:
                try:
                    nin = request.data["nin"]
                    phone_number = request.data["phone_number"]

                    if phone_number != PaymentToken.objects.get(secret=auth_key).payer.phone_number:
                        phone_mismatch = {
                            "status": "error",
                            "message": "This phone number wasn't used to register for the the Authorization token provided"
                        }

                        LinkNin.objects.create(
                            nin=nin,
                            phone_number=phone_number,
                            status=False,
                            price="0",
                            request_message=phone_mismatch["message"]
                        )

                        return Response(phone_mismatch, status=status.HTTP_403_FORBIDDEN)
                    else:
                        success = {
                            "status": "success",
                            "message": "Your NIN was successfully linked. Note that you can no more use the provided Authorization header",
                            "data": {
                                "nin": nin,
                                "phone_number": phone_number
                            }
                        }

                        LinkNin.objects.create(
                            nin=nin,
                            phone_number=phone_number,
                            status=True,
                            price=PaymentToken.objects.get(secret=auth_key).payer.price,
                            request_message=success["message"]
                        )
                        PaymentToken.objects.get(secret=auth_key).delete()

                        return Response(success, status=status.HTTP_200_OK)
                except KeyError:
                    keyerr = {
                        "status": "error",
                        "message": "nin and phone_number object is required."
                    }
                    return Response(keyerr, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def nin_requests(request):
    res = {
        "status": "success",
        "data": []
    }
    for obj in LinkNin.objects.all():
        res["data"].append({
            "phone_number": obj.phone_number,
            "nin": obj.nin,
            "charged_price": obj.price,
            "request_status": obj.status,
            "request_message": obj.request_message,
            "link_time": obj.time,
            "link_date": obj.date,
        })
    return Response(res, status=status.HTTP_200_OK)