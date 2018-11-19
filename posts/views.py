from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here. python manage.py runserver


class Index(View):

    def get(self, request):
        context = {'text': 'Hello world'}
        return render(request, 'base.html', context)