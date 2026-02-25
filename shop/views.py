from django.shortcuts import render

from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .forms import OrderForm
from .services import send_telegram_notification

def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = UserCreationForm()

    return render(request, "shop/register.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("product_list")
    return redirect("product_list")

def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()

            message = (
                f"Новый заказ!\n"
                f"Товар: {product.name}\n"
                f"Имя: {order.customer_name}\n"
                f"Телефон: {order.customer_phone}\n"
                f"Email: {order.customer_email}"
            )

            send_telegram_notification(message)
            return redirect("order_success")
    else:
        form = OrderForm()

    return render(request, "shop/order_form.html", {
        "form": form,
        "product": product
    })

def order_success(request):
    return render(request, "shop/order_success.html")