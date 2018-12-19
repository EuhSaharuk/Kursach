from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=20, default="Назв. категории")

    def get_absolute_url(self):
        return reverse('room_cat_url', kwargs={'id': str(self.id)})

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, default="tag")

    def __str__(self):
        return self.name
