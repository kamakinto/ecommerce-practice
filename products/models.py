from django.db import models
import random
import os
from ecommerce.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
from django.db.models import Q
# Create your models here.

def get_filename_ext(filepath):
  base_name = os.path.basename(filepath)
  name, ext = os.path.splitext(base_name)
  return name, ext

def upload_image_path(instance, filename):
  print(instance)
  print(filename)
  new_filename = random.randint(1, 390439405834903)
  name, ext = get_filename_ext(filename)
  final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
  return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet):
        def featured(self):
                return self.filter(featured=True)

        def search(self, query):
                lookups = (
                        Q(title__icontains=query)
                |       Q(description__icontains=query)
                |       Q(tag__title__icontains=query))
                return self.filter(lookups).distinct()

#Overriding the model manager aka creating our own methods for database lookups
class ProductManager(models.Manager):
        def get_queryset(self):
                return ProductQuerySet(self.model, using=self._db)

        def featured(self):
                return self.get_queryset().filter(featured=True)

        def get_by_id(self, id):
                return self.get_queryset().filter(id=id) #self.get_queryset() == Product.objects

        def search(self, query):
                return self.get_queryset().search(query)



class Product(models.Model):
  title = models.CharField(max_length = 120)
  slug = models.SlugField(blank=True, unique=True)
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=20, default=00.00)
  debit = models.DecimalField(decimal_places=2, max_digits=20, default=00.00)
  image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  featured = models.BooleanField(default=False)
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = ProductManager()
  def get_absolute_url(self):
    #return "/products/{slug}/".format(slug=self.slug)
    return reverse("products:detail", kwargs={"slug": self.slug}) #used for

  def __str__(self):
    return self.title #decides the name within the admin database menu

@property
def name(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
            if not instance.slug:
                    instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


