from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from category.models import Category, Tag
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        category = forms.CharField()
        tag = forms.CharField()
        sort = forms.CharField()
        fields = ("category", "tag", "sort")
