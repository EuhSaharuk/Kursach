from django.contrib import admin
from django.urls import path, include
from apartment.views import *
from posts.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='administration'),
    path('', Index.as_view(), name='home'),
    path('room/', include('apartment.urls', namespace='room')),
    path('user/', include('log_sys.urls', namespace='user')),
    path('orders/', include('order.urls', namespace='orders')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('', Index.get_custom, name='custom'),
    # path('<str:id>/', Index.get_by_category, name='room_cat_url')
    # re_path(r'^user/(\w+)/$', Profile.as_view())
    # path('user/', include(urls))