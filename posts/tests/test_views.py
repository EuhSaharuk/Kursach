from django.test import TestCase, RequestFactory
from posts.views import Index
from apartment.models import Apartment
from category.models import Category, Tag
from django.contrib.auth.models import User


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="1")
        Category.objects.create(name="1")
        Category.objects.create(name="2")
        Apartment.objects.create(name="room1", text="room1", price=100, category=Category.objects.get(id=1))
        Apartment.objects.create(name="room2", text="room1", price=130, category=Category.objects.get(id=1))
        Apartment.objects.create(name="room3", text="room1", price=300, category=Category.objects.get(id=1))
        Apartment.objects.create(name="room4", text="room1", price=200, category=Category.objects.get(id=2))
        Apartment.objects.create(name="room5", text="room5", price=230, category=Category.objects.get(id=2))

    def test_Index_get_success(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertTrue(resp.context['is_staff'] != "True")
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['rooms'].__str__(), Apartment.objects.all().__str__())
        self.assertEqual(resp.context['category'].__str__(), Category.objects.all().__str__())
        self.assertEqual(resp.context['tag'].__str__(), Tag.objects.all().__str__())

    def test_Index_post_success(self):
        resp = self.client.post('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertTrue(resp.context['is_staff'] != "True")
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['rooms'].__str__(), Apartment.objects.all().__str__())
        self.assertEqual(resp.context['category'].__str__(), Category.objects.all().__str__())
        self.assertEqual(resp.context['tag'].__str__(), Tag.objects.all().__str__())

    def test_Index_post_sort_by_cat_success(self):
        resp = self.client.post('/', {'category': '1', 'sort': 'increase'})
        rooms = Apartment.objects.all()
        exp_rooms = rooms.filter(category="1").order_by('price')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertTrue(resp.context['is_staff'] != "True")
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['rooms'].__str__(), exp_rooms.__str__())
        self.assertEqual(resp.context['category'].__str__(), Category.objects.all().__str__())
        self.assertEqual(resp.context['tag'].__str__(), Tag.objects.all().__str__())

    def test_Index_post_by_cat_success(self):
        resp = self.client.post('/', {'category': '1'})
        rooms = Apartment.objects.all()
        exp_rooms = rooms.filter(category="1")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertTrue(resp.context['is_staff'] != "True")
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['rooms'].__str__(), exp_rooms.__str__())
        self.assertEqual(resp.context['category'].__str__(), Category.objects.all().__str__())
        self.assertEqual(resp.context['tag'].__str__(), Tag.objects.all().__str__())

    def test_Index_post_sort_success(self):
        resp = self.client.post('/', {'sort': 'increase'})
        rooms = Apartment.objects.all()
        exp_rooms = rooms.order_by('price')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')
        self.assertTrue(resp.context['is_staff'] != "True")
        self.assertTrue(resp.context['username'] == '')
        self.assertEqual(resp.context['rooms'].__str__(), exp_rooms.__str__())
        self.assertEqual(resp.context['category'].__str__(), Category.objects.all().__str__())
        self.assertEqual(resp.context['tag'].__str__(), Tag.objects.all().__str__())

    def test_Index_get_rooms_by_filter_empty_request_success(self):
        r = RequestFactory().post('/')
        rooms = Apartment.objects.all()

        s_rooms = Index.get_rooms_by_filter(r, rooms)
        exp_rooms = rooms

        self.assertEqual(s_rooms, exp_rooms)

    def test_Index_get_rooms_by_filter_sort_dec_success(self):
        r = RequestFactory().post('/', {'sort': 'decrease'})
        rooms = Apartment.objects.all()

        s_rooms = Index.get_rooms_by_filter(r, rooms)
        exp_rooms = rooms.order_by('-price')

        self.assertEqual(s_rooms.__str__(), exp_rooms.__str__())

    def test_Index_get_rooms_by_filter_sort_inc_success(self):
        r = RequestFactory().post('/', {'sort': 'increase'})
        rooms = Apartment.objects.all()

        s_rooms = Index.get_rooms_by_filter(r, rooms)
        exp_rooms = rooms.order_by('price')

        self.assertEqual(s_rooms.__str__(), exp_rooms.__str__())

    def test_Index_get_rooms_by_filter_with_cat_success(self):
        r = RequestFactory().post('/', {'category': '1'})
        rooms = Apartment.objects.all()

        s_rooms = Index.get_rooms_by_filter(r, rooms)
        exp_rooms = rooms.filter(category="1")

        self.assertEqual(s_rooms.__str__(), exp_rooms.__str__())

    def test_Index_get_rooms_by_filter_sort_with_cat_success(self):
        r = RequestFactory().post('/', {'category': '1', 'sort': 'increase'})
        rooms = Apartment.objects.all()

        s_rooms = Index.get_rooms_by_filter(r, rooms)
        exp_rooms = rooms.filter(category="1").order_by('price')

        self.assertEqual(s_rooms.__str__(), exp_rooms.__str__())
