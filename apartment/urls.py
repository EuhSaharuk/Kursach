from django.urls import path
from .views import Room_page
from order.views import Order

app_name = 'room'

urlpatterns = [
    path('<str:identity>/', Room_page.get_room, name="get_room"),
    path('<str:identity>/order', Order.as_view(), name="get_order")
]
