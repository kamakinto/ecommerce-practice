from django.views.generic  import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from carts.models import Cart

class ProductFeaturedListView(ListView):
  #queryset = Product.objects.all() #get all products from the database
	model = Product #also a quick way to get all products from the database
	template_name = "products/list.html"
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
	template_name = "products/featured-detail.html"
	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()


class ProductListView(ListView):
	#queryset = Product.objects.all() #get all products from the database
	model = Product #also a quick way to get all products from the database
	template_name = "products/list.html"


class ProductDetailSlugView(DetailView):
        queryset = Product.objects.all() #get all products from the database
        template_name = "products/detail.html"

        def get_context_data(self, *args, **kwargs):
                context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs) #get context for view
                cart_obj, new_obj = Cart.objects.new_or_get(self.request) #get current user's cart
                context['cart'] = cart_obj #add the current user's cart to the current view
                return context

        def get_object(self, *args, **kwargs):
                request = self.request
                slug = self.kwargs.get('slug')
                try:
                        instance = Product.objects.get(slug=slug)
                except Product.DoesNotExist:
                        raise Http404("Not found..")
                except Product.MultipleObjectsReturned:
                        qs = Product.objects.filter(slug=slug)
                        instance = qs.first()
                except:
                        raise Http404("hmmmm")
                return instance


class ProductDetailView(DetailView):
        queryset = Product.objects.all() #get all products from the database
        template_name = "products/detail.html"

        def get_context_data(self, *args, **kwargs):
                context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
                print(context)
                return context

  # def get_object(self, *args, **kwargs):
  #   request = self.request
  #   pk = self.kwargs.get('pk')
  #   instance = Product.objects.get_by_id(pk)
  #   if instance is None:
  #     raise Http404("Product doesnt exist")

  #   return instance


def product_list_view(request):
  queryset = Product.objects.all()
  context = {
	'object_list': queryset
  }
  return render(request, "products/list.html", context)

def product_detail_view(request, pk=None, *args, **kwargs):

 #instance = Product.objects.get(pk=pk) #pk = internal name for the Unique ID
  #instance = get_object_or_404(Product, pk=pk) #another way to fetch the object
  #instance = Product.objects.get_by_id(pk)
  #print(instance)
  qs = Product.objects.filter(id=pk)
  instance = qs.first()
  print(instance)

  context = {
  'object': instance
  }
  return render(request, "products/detail.html", context)