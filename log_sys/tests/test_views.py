from django.test import TestCase
from log_sys import views
from django.contrib.auth.models import User
from django.test import Client


class log_sys_view_Test(TestCase):

    def test_username_validation_void(self):
        name = ""

        res = views.username_validation(name)

        self.assertEqual(res, False)

    def test_username_validation_short(self):
        name = "as"

        res = views.username_validation(name)

        self.assertEqual(res, False)

    def test_username_validation_long(self):
        name = "a"
        for i in range(255):
            name = name + "f"

        res = views.username_validation(name)

        self.assertEqual(res, False)

    def test_username_validation_forbidden_symbol(self):
        name = "oed30-2*"

        res = views.username_validation(name)

        self.assertEqual(res, False)

    def test_username_validation_success(self):
        name = "vasyaf.+-_"

        res = views.username_validation(name)

        self.assertEqual(res, True)