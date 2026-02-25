from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "customer_name",
        "customer_phone",
        "customer_email",
        "created_at",
    )
    search_fields = ("customer_name", "customer_email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)