from django.db import models
from category.models import Category


class Apartment(models.Model):
    name = models.CharField(max_length=30, default="Название")
    text = models.CharField(max_length= 300, default="JОписание номера")
    price = models.SmallIntegerField()
    active = models.BooleanField(default=True)
    # categories = models.ManyToManyField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
