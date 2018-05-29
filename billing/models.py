from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

class BillingProfile(models.Model):
        user = models.ForeignKey(User, null=True, unique=True, blank=True, on_delete=models.CASCADE)
        email = models.EmailField()
        active = models.BooleanField(default=True)
        update = models.DateTimeField(auto_now=True)
        timestamp = models.DateTimeField(auto_now_add=True)
        #customer_id = Stripe customer ID associated with this billing profile

        def __str__(self):
                return self.email

# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#         if created:
#                 newID =  print("This would be an API request to get the customer id")
#                 instance.customer_id = newID
#                 instance.save()

def user_created_receiver(sender, instance, created, *args, **kwargs):
        if created:
                BillingProfile.objects.get_or_create(user=instance)


post_save.connect(user_created_receiver, sender=User)
