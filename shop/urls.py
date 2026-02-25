from django.urls import path

from .views import product_list,register,logout_view, create_order, order_success


urlpatterns = [
    path("", product_list, name="product_list"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("order/<int:product_id>/", create_order, name="create_order"),
    path("order/success/", order_success, name="order_success"),
]