from django.test import TestCase, RequestFactory
from order.views import Order
from apartment.models import Apartment
from category.models import Category
from django.contrib.auth.models import User
from django.test import Client


class OrderTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="1")
        Apartment.objects.create(name="room1", text="room1", price=100, category=Category.objects.get(id=1))

    def test_Order_success(self):
        resp = self.client.get('/room/1/order')
        resp.user = User.objects.create(username="user", password="123qwe", is_staff=False)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'order.html')
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['success'].__str__(), "None")

    def test_Order_post_void(self):
        resp = self.client.post('/room/1/order')
        resp.user = User.objects.create(username="user", password="123qwe", is_staff=False)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'order.html')
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['success'].__str__(), "False")

    def test_Order_post_fail(self):
        resp = self.client.post('/room/1/order', {'tel_number': '0230'})
        resp.user = User.objects.create(username="user", password="123qwe", is_staff=False)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'order.html')
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['success'].__str__(), "False")


    def test_Order_post_success(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        c.login(username='testuser', password='12345')
        '''
        # resp = self.client.post('/room/1/order', {'tel_number': '295330918'})
        req = RequestFactory().post('/room/1/order', {'tel_number': '295330918'})
        req.user = User.objects.create(username="user", password="123qwezxc", is_staff=False)
        # resp = self.client.request(req)
        o = Order
        resp = o.post(req, "1")
        # resp = self.client.post('/room/1/order', {'tel_number': '295330918', 'user': user})'''
        resp = c.post('/room/1/order', {'tel_number': '295330918', 'text': 'jh l'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'order.html')
        self.assertTrue(resp.context['username'] == 'testuser')
        # self.assertTrue(resp.content['success'].__str__() == "True")

    def test_phone_validator_void(self):
        phone = ""

        res = Order.phone_validator(phone)
        self.assertEqual(res, False)

    def test_phone_validator_not_digit(self):
        phone = "a35748561"

        res = Order.phone_validator(phone)

        self.assertEqual(res, False)

    def test_phone_validator_long(self):
        phone = "123456948498"

        res = Order.phone_validator(phone)

        self.assertEqual(res, False)

    def test_phone_validator_short(self):
        phone = "498651"

        res = Order.phone_validator(phone)

        self.assertEqual(res, False)

    def test_phone_validator_success(self):
        phone = "295330918"

        res = Order.phone_validator(phone)

        self.assertTrue(res)
