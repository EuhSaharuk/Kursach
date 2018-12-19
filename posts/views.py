from django.shortcuts import render
from django.views import View
from apartment.models import Apartment
from category.models import Category, Tag
from django.contrib import auth


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        rooms = Apartment.objects.all()
        categories = Category.objects.all()
        tags = Tag.objects.all()
        username = auth.get_user(request).username
        context = {'rooms': rooms,
                   'category': categories,
                   'tag': tags,
                   'username': username,
                   'is_staff': auth.get_user(request).is_staff.__str__()}
        return render(request, 'index.html', context)

    def post(self, request):
        rooms = Apartment.objects.all()
        rooms = self.get_rooms_by_filter(request, rooms)
        categories = Category.objects.all()
        tags = Tag.objects.all()
        username = auth.get_user(request).username
        context = {'rooms': rooms,
                   'category': categories,
                   'tag': tags,
                   'username': username,
                   'is_staff': auth.get_user(request).is_staff.__str__()}
        return render(request, 'index.html', context)

    @staticmethod
    def get_rooms_by_filter(request, rooms):
        if request.POST.get("sort"):
            if request.POST.get("sort") == "decrease":
                rooms = rooms.order_by('-price')
            else:
                rooms = rooms.order_by('price')
        if request.POST.get("category"):
            by_cat = Category.objects.get(id=request.POST.get("category"))
            rooms = rooms.filter(category=by_cat)
        return rooms

    @staticmethod
    def get_absolute_url():
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



