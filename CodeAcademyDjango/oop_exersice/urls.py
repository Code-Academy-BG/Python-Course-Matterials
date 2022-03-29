from django.urls import path

from . import views

app_name = "oop"

urlpatterns = [
    path("api/orders/files", views.OrdersDBAPI.as_view(), name="orders_search"),
    path("api/orders/file", views.OrdersFileAPI.as_view(), name="orders_files"),
]
