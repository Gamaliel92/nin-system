from django.db import models

# Create your models here.
class nin_links(models.Model):
    nin = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    status = models.BooleanField(default=False)
    request_message = models.TextField(null=True)
    price = models.CharField(max_length=20, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
