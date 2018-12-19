from django.test import TestCase
from apartment.models import Apartment
from category.models import Category


class RoomPageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name="1")
        Apartment.objects.create(name="room1", text="room1", price=100, category=Category.objects.get(id=1),
                                 image='\room_pictures\default.jpg')

    def test_RoomPage_get_success(self):
        self.resp = self.client.get('/room/1/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertTemplateUsed(self.resp, 'room.html')
        self.assertTrue(self.resp.context['is_staff'] != "True")
        self.assertTrue(self.resp.context['username'] == '')
        self.assertTrue(self.resp.context['room'] == Apartment.objects.get(id=1))
