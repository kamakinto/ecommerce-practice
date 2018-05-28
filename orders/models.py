from django.db import models
from carts.models import Cart
import math
from ecommerce.utils import unique_order_id_generator
from django.db.models.signals import pre_save, post_save

ORDER_STATUS_CHOICES = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('refunded', 'Refunded'),
)
class Order(models.Model):
        #billing_profile = ?
        # shipping_address =
        # billing_address =

        order_id  = models.CharField(max_length=120, blank=True)
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        status  = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
        shipping_total = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
        total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

        def __str__(self):
                return self.order_id


        def update_total(self):
                cart_total = self.cart.total
                shipping_total = self.shipping_total
                new_total = math.fsum([cart_total + shipping_total])
                formatted_total = format(new_total, '.2f')
                self.total = formatted_total
                self.save()
                return new_total


#-------------------------------- Signals --------------------------------#
# Pre and Post save signals for the checkout Model object instances
#----------------------------------------------------------------------------


# Methods fired off whenever we save an "orders" object.
def pre_save_create_order_id(sender, instance, *args, **kwargs):
        if not instance.order_id:
                instance.order_id = unique_order_id_generator(instance)

def post_save_cart_total(sender, instance, created, *args, **kwargs):
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1: #if the query only has 1 result aka. if we find only one Order
                order_obj = qs.first()
                order_obj.update_total()


def post_save_order(sender, instance, created, *args, **kwargs):
        if created:
                instance.update_total


#Method used to bind/connect the model being overridden with the function that is handling the override process.
#in this case, pre_save_create_order_id
pre_save.connect(pre_save_create_order_id, sender=Order)
post_save.connect(post_save_cart_total, sender=Cart)
post_save.connect(post_save_order, sender=Order)



