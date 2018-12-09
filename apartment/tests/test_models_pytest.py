from django.test import TestCase
from apartment.models import Apartment
from category.models import Category, Tag
from django.db import models


class ApartmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="1")
        Category.objects.create(name="1")
        Apartment.objects.create(name="room", text='description', price=300, category=Category.objects.get(id=1),
                                 image='room_pictures/default.jpg')

    def test_name_label(self):
        author = Apartment.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        author = Apartment.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

    def test_text_label(self):
        author = Apartment.objects.get(id=1)
        field_label = author._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_text_max_length(self):
        author = Apartment.objects.get(id=1)
        max_length = author._meta.get_field('text').max_length
        self.assertEquals(max_length, 300)

    def test_price_label(self):
        author = Apartment.objects.get(id=1)
        field_label = author._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_category_label(self):
        author = Apartment.objects.get(id=1)
        field_label = author._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_image_label(self):
        author = Apartment.objects.get(id=1)
        field_label = author._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')

    def test_image_upload_to(self):
        author = Apartment.objects.get(id=1)
        field_upload_to = author._meta.get_field('image').upload_to
        self.assertEquals(field_upload_to, 'room_pictures')

    def test_active_label(self):
        author = Apartment.objects.get(id=1)
        field_label = author._meta.get_field('active').verbose_name
        self.assertEquals(field_label, 'active')