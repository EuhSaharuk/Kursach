from django.views.generic import CreateView
from .forms import MyUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect, render, render_to_response


class UserCreateView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'create.html'
    success_url = '/'

    # def get(self, request, *args, **kwargs):
    #     print("***********************************************************************")
    #     return render_to_response('create.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
