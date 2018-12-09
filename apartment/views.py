from .models import Apartment
from django.contrib import auth
from django.shortcuts import render, reverse
# Create your views here.

'''
def room_list(request):
    rooms = Apartment.objects.all()
    return render()'''


class Room_page():

    @staticmethod
    def get_room(request, identity):
        print("***\n***\n***\n")
        print(request)
        print(identity)
        ap = Apartment.objects.get(id=int(identity))
        username = auth.get_user(request).username
        print(ap.tags.all())
        context = {'room': ap,
                   'tag': ap.tags.all(),
                   'username': username,
                   'is_staff': auth.get_user(request).is_staff.__str__()
                   }
        return render(request, 'room.html', context)

