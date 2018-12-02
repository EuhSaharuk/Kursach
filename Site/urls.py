from django.contrib import admin
from django.urls import path, re_path, include
from user_profile.views import Profile
from apartment.views import *
from posts.views import *
from django.contrib.auth.views import auth_login
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
# from user_profile import urls


urlpatterns = [
    path('admin/', admin.site.urls, name='administration'),
    # path('', Index.get_custom, name='custom'),
    path('', Index.as_view(), name='home'),

    path('user/', include('log_sys.urls', namespace='user')),
    # path('<str:id>/', Index.get_by_category, name='room_cat_url')
    # re_path(r'^user/(\w+)/$', Profile.as_view())
    # path('user/', include(urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
