from django.db import models

# Create your models here.
class MakePayment(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, null=True)
    bank = models.CharField(max_length=3, null=True)
    account_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.email

class ApiPrice(models.Model):
    price = models.IntegerField(default=500)

    def __str__(self):
        return f"NGN {price}"

class PaymentToken(models.Model):
    payer = models.ForeignKey(MakePayment, on_delete=models.CASCADE)
    secret = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.payer.email