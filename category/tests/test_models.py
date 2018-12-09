from django.test import TestCase
from apartment.models import Apartment
from category.models import Category, Tag
from django.db import models
# Create your tests here.


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="room_category")

    def test_name_label(self):
        ct = Category.objects.get(id=1)
        field_label = ct._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        ct = Category.objects.get(id=1)
        max_length = ct._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

