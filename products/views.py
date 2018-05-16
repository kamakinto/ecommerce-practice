from django.views.generic  import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product

class ProductListView(ListView):
  #queryset = Product.objects.all() #get all products from the database
  model = Product #also a quick way to get all products from the database
  template_name = "products/list.html"

class ProductDetailView(DetailView):
  queryset = Product.objects.all() #get all products from the database
  template_name = "products/detail.html"

  def get_context_data(self, *args, **kwargs):
      context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
      print(context)
      return context


def product_list_view(request):
  queryset = Product.objects.all()
  context = {
    'object_list': queryset
  }
  return render(request, "products/list.html", context)

def product_detail_view(request, pk=None, *args, **kwargs):
  print (args)
  print(kwargs)
 #instance = Product.objects.get(pk=pk) #pk = internal name for the Unique ID
  instance = get_object_or_404(Product, pk=pk) #another way to fetch the object

  context = {
  'object': instance
  }
  return render(request, "products/detail.html", context)