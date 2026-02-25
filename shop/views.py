from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import escape

from .forms import OrderForm
from .models import Product
from .services import send_telegram_notification, send_telegram_photo




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


def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()

            message = (
                f"🛒 <b>Новый заказ #{order.id}</b>\n\n"
                f"<b>Товар:</b> {escape(product.name)}\n"
                f"<b>Цена:</b> {product.price} ₽\n\n"
                f"<b>Клиент:</b>\n"
                f"Имя: {escape(order.customer_name)}\n"
                f"Телефон: {escape(order.customer_phone)}\n"
                f"Email: {escape(order.customer_email)}"
            )

            image_url = ""
            if product.image:
                image_url = product.image.url

            if image_url.startswith("http://") or image_url.startswith("https://"):
                send_telegram_photo(image_url, caption=message, parse_mode="HTML")
            else:
                send_telegram_notification(message, parse_mode="HTML")

            messages.success(request, "Заказ оформлен! Мы скоро свяжемся с вами.")
            return redirect("order_success")
    else:
        form = OrderForm()

    return render(
        request,
        "shop/order_form.html",
        {"form": form, "product": product},
    )


def order_success(request):
    return render(request, "shop/order_success.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/product_detail.html", {"product": product})