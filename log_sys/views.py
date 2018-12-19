from django.views.generic import CreateView
from .forms import MyUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect, render, render_to_response


class UserCreateView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'create.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def username_validation(name):
    if not (len(name) < 3 or len(name) > 255):
        name = name.replace('-', '').replace('_', '').replace('.', '').replace('+', '')
        if name.isalnum():
            return True
    return False

