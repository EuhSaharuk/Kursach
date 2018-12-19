from django.db import models
from apartment.models import Apartment
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='order')
    apartment = models.ForeignKey(Apartment, on_delete=models.DO_NOTHING, related_name='order')
    phone_number = models.CharField(max_length=14)
    text = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.__str__() + " | " + self.apartment.__str__() + " | " + self.date.__str__()[:19]
