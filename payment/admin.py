from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MakePayment)
admin.site.register(models.ApiPrice)
admin.site.register(models.PaymentToken)