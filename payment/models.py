from django.db import models

# Create your models here.
class MakePayment(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    bank = models.CharField(max_length=5, null=True)
    account_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.phone_number

class ApiPrice(models.Model):
    price = models.IntegerField(default=500)

    def __str__(self):
        return f"NGN {price}"

class PaymentToken(models.Model):
    payer = models.ForeignKey(MakePayment, on_delete=models.CASCADE)
    secret = models.CharField(unique=True, max_length=100, null=True)

    def __str__(self):
        return self.secret