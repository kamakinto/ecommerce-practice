from django.db import models
from carts.models import Cart
# Create your models here.

ORDER_STATUS_CHOICES = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('refunded', 'Refunded'),
)
class Order(models.Model):
        #billing_profile = ?
        # shipping_address
        # billing_address

        order_id  = models.CharField(max_length=120)
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        status  = models.CharField(max_length=120, default='created')
        shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
        total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

