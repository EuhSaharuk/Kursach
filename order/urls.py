from django.urls import path
from .views import Order

app_name = "orders"

urlpatterns = [
    path('', Order.get_orders_page, name='orders_page'),

]
