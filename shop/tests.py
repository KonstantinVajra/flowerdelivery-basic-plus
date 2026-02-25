from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product, Order
from django.contrib.auth import get_user_model


class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(
            name="Test Flower",
            description="Test description",
            price=1000,
        )

        self.assertEqual(product.name, "Test Flower")
        self.assertEqual(product.price, 1000)
        self.assertIsNotNone(product.created_at)


class OrderModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Rose",
            description="Red rose",
            price=500,
        )

    def test_order_creation(self):
        order = Order.objects.create(
            product=self.product,
            customer_name="John",
            customer_phone="123456789",
            customer_email="john@example.com",
        )

        self.assertEqual(order.product.name, "Rose")
        self.assertEqual(order.customer_name, "John")
        self.assertIsNotNone(order.created_at)

class ProductListViewTest(TestCase):
    def test_product_list_page(self):
        Product.objects.create(name="A", description="A", price=100)
        Product.objects.create(name="B", description="B", price=200)

        resp = self.client.get("/")

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "shop/product_list.html")
        self.assertContains(resp, "A")
        self.assertContains(resp, "B")

class OrderFlowTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Rose",
            description="Red rose",
            price=500,
        )

    def test_order_get_form(self):
        resp = self.client.get(f"/order/{self.product.id}/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "shop/order_form.html")

    def test_order_post_creates_order_and_redirects(self):
        resp = self.client.post(
            f"/order/{self.product.id}/",
            data={
                "customer_name": "John",
                "customer_phone": "123456789",
                "customer_email": "john@example.com",
            },
        )
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Order.objects.filter(product=self.product, customer_email="john@example.com").exists())


class OrderSuccessPageTest(TestCase):
    def test_order_success_page(self):
        resp = self.client.get("/order/success/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "shop/order_success.html")

class AuthSmokeTest(TestCase):
    def test_login_page(self):
        resp = self.client.get("/accounts/login/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "registration/login.html")

    def test_register_page(self):
        resp = self.client.get("/register/")
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "shop/register.html")

    def test_logout_post(self):
        User = get_user_model()
        user = User.objects.create_user(username="u1", password="pass12345")

        login_ok = self.client.login(username="u1", password="pass12345")
        self.assertTrue(login_ok)

        resp = self.client.post("/logout/")
        self.assertEqual(resp.status_code, 302)

        # после logout доступ к защищённому контенту должен быть как у анонима
        resp2 = self.client.get("/accounts/login/")
        self.assertEqual(resp2.status_code, 200)