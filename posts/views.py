from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from apartment.models import Apartment
from category.models import Category, Tag
from django.contrib import auth
from .forms import MyUserCreationForm
# Create your views here. python manage.py runserver


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        print("****************/***************")
        print(request)
        rooms = Apartment.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        username = auth.get_user(request).username
        context = {'rooms': rooms,
                   'category': categories,
                   'tag': tags,
                   'username': username}
        if auth.get_user(request).is_staff:
            context['is_staff'] = "True"
        return render(request, 'index.html', context)

    def post(self, request):
        print("****************/post***********")
        print(request.POST.get("sort"))

        rooms = Apartment.objects.all()
        if request.POST.get("sort"):
            if request.POST.get("sort") == "decrease":
                rooms = rooms.order_by('-price')
            else:
                rooms = rooms.order_by('price')
        print(request.POST.get("category"))
        if request.POST.get("category"):
            by_cat = Category.objects.get(id=request.POST.get("category"))
            rooms = rooms.filter(category=by_cat)
            #rooms = rooms.filter(category= id=int(request.POST.get("category")))


        categories = Category.objects.all()
        tags = Tag.objects.all()
        username = auth.get_user(request).username
        context = {'rooms': rooms,
                   'category': categories,
                   'tag': tags,
                   'username': username}
        if auth.get_user(request).is_staff:
            context['is_staff'] = "True"
        return render(request, 'index.html', context)

    @staticmethod
    def get_absolute_url(self):
        rooms = Apartment.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        context = {'rooms': rooms,
                   'category': categories,
                   'tag': tags}
        return render('index.html', context)

    @staticmethod
    def get_by_category(request, identity):
        by_cat = Category.objects.get(id=identity)
        rooms = by_cat.apartment.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        context = {'rooms': rooms,
                   'categories': categories,
                   'tag': tags}
        return render(request, 'index.html', context)

    @staticmethod
    def by_price(a):
        return a.price()
    # @staticmethod
    # def get_custom(request):
    #     print("****************/***************")
    #     print(request)


