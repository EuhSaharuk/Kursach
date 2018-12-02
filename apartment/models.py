from django.db import models
from category.models import Category


class Apartment(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    price = models.SmallIntegerField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='apartment', default="Однокомнатная")
    image = models.ImageField(upload_to='room_pictures', blank=True)
    tags = models.ManyToManyField('category.Tag', blank=True, related_name='apartment')

    def __str__(self):
        return self.name
