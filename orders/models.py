from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()


STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_process', 'В обработке'),
    ('canceled', 'Отмененный'),
    ('finished', 'Завершенный')
)


class Order(models.Model):
    user = models.ForeignKey(User, 
                             on_delete=models.RESTRICT, 
                             related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50, blank=True)
    products = models.ManyToManyField(Product, through='OrderItems')
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f'Order #{self.id}'

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField(default=1)

