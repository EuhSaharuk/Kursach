from django.urls import path
from .views import RoomPage
from order.views import Order

app_name = 'room'

urlpatterns = [
    path('<str:identity>/', RoomPage.get_room, name="get_room"),
    path('<str:identity>/order', Order.as_view(), name="get_order")
]
