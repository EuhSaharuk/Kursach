from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        field_classes = {'username': UsernameField}
        fields = ("username", "first_name", "last_name", "email")
