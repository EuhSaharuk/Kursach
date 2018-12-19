from .models import Apartment
from django.contrib import auth
from django.shortcuts import render, reverse


class RoomPage:

    @staticmethod
    def get_room(request, identity):
        ap = Apartment.objects.get(id=int(identity))
        username = auth.get_user(request).username
        context = {'room': ap,
                   'tag': ap.tags.all(),
                   'username': username,
                   'is_staff': auth.get_user(request).is_staff.__str__()
                   }
        return render(request, 'room.html', context)
