from django.shortcuts import render
from apartment.models import Apartment
from django.contrib import auth
from .models import Order as O
from django.views import View


class Order(View):
    template_name = 'order.html'

    def get(self, request, identity):
        ap = Apartment.objects.get(id=int(identity))
        username = auth.get_user(request).username
        context = {'room': ap,
                   'username': username,
                   'success': 'None'}

        return render(request, 'order.html', context)

    def post(self, request, identity):
        success = 'False'
        number = request.POST.get("tel_number")
        print(number)
        print("\n\n\t*******\t***********\t********************************\n")
        text = request.POST.get("text")
        if len(number) > 8:
            O.objects.create(customer=auth.get_user(request), text=text, phone_number=number,
                                 apartment=Apartment.objects.get(id=int(identity)))
            success = 'True'
        ap = Apartment.objects.get(id=int(identity))
        username = auth.get_user(request).username
        context = {'room': ap,
                   'username': username,
                   'success': success}
        return render(request, 'order.html', context)

    @staticmethod
    def get_order(request, identity):
        ap = Apartment.objects.get(id=int(identity))
        username = auth.get_user(request).username
        context = {'room': ap,
                   'username': username,
                   'success': 'None'}

        return render(request, 'order.html', context)
