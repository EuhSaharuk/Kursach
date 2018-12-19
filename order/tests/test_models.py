from django.test import TestCase
from apartment.models import Apartment
from category.models import Category, Tag
from order.models import Order
from django.contrib.auth.models import User


class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="1")
        Category.objects.create(name="1")
        Apartment.objects.create(name="room", text='description', price=300, category=Category.objects.get(id=1),
                                 image='room_pictures/default.jpg')
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        Order.objects.create(customer=User.objects.get(id=1),
                             apartment=Apartment.objects.get(id=1),
                             phone_number="2953309180",
                             text="d")

    def test_cust_label(self):
        o = Order.objects.get(id=1)
        field_label = o._meta.get_field('apartment').verbose_name
        self.assertEquals(field_label, 'apartment')

    def test_ap_label(self):
        o = Order.objects.get(id=1)
        field_label = o._meta.get_field('customer').verbose_name
        self.assertEquals(field_label, 'customer')

    def test_num_label(self):
        o = Order.objects.get(id=1)
        field_label = o._meta.get_field('phone_number').verbose_name
        self.assertEquals(field_label, 'phone number')

    def test_num_max_length(self):
        o = Order.objects.get(id=1)
        max_length = o._meta.get_field('phone_number').max_length
        self.assertEquals(max_length, 14)

    def test_text_label(self):
        o = Order.objects.get(id=1)
        field_label = o._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_text_max_length(self):
        o = Order.objects.get(id=1)
        max_length = o._meta.get_field('text').max_length
        self.assertEquals(max_length, 300)

    def test_is_active_label(self):
        o = Order.objects.get(id=1)
        field_label = o._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'is active')

    def test_date_label(self):
        o = Order.objects.get(id=1)
        field_label = o._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')
