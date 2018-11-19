from django.shortcuts import render
from django.views import View
from user_profile.models import User
# Create your views here.

class Profile(View):
    """User Profile Page"""

    def get(self, request, username):

        user = User.objects.get(username=username)
        context = {'user': user}
        return render(request, 'posts.html', context)
