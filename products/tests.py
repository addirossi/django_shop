from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Category, Product
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

User = get_user_model()


class TestProducts(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='test@test.com',
            password='qwerty12',
            name='testuser',
            is_active=True
        )
        self.admin1 = User.objects.create_superuser(
            email='admin@test.com',
            password='admin123',
            name='superuser1'
        )
        self.user1_token = get_tokens_for_user(self.user1)
        self.admin1_token = get_tokens_for_user(self.admin1)
        self.category = Category.objects.create(name='Игрушки', slug='igrushku')
        self.product1 = Product.objects.create(
            name='световой меч',
            description='Меч Скайуокера',
            category = self.category,
            price=1000
        )
        self.product2 = Product.objects.create(
            name='Футбольный мяч',
            description='Мяч для игры в футбол',
            category = self.category,
            price=500
        )
        self.product3 = Product.objects.create(
            name='Плюшевый медведь',
            description='Мягкий медведь',
            category = self.category,
            price=1500
        )
        self.product_payload = {
            'name': 'SegaMegaDrive',
            'description': 'Лучшая приставка!',
            'category': self.category.id,
            'price': 2000
        }

    def test_create_product_as_anonymous_user(self):
        data = self.product_payload.copy()
        client = APIClient()
        url = 'http://localhost:8000/products/'
        response = client.post(url, data)
        self.assertEqual(response.status_code, 401)

    def test_create_product_as_user(self):
        data = self.product_payload.copy()
        client = APIClient()
        url = 'http://localhost:8000/products/'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user1_token.get("access")}')
        response = client.post(url, data)
        self.assertEqual(response.status_code, 403)

    def test_create_product_as_superuser(self):
        data = self.product_payload.copy()
        client = APIClient()
        url = 'http://localhost:8000/products/'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin1_token.get("access")}')
        response = client.post(url, data)
        self.assertEqual(response.status_code, 201)


