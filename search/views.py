from django.views.generic  import ListView
from django.shortcuts import render
from django.http import Http404
from products.models import Product
from django.db.models import Q


# Create your views here.
class SearchProductListView(ListView):
	#queryset = Product.objects.all() #get all products from the database
	#model = Product #also a quick way to get all products from the database
        template_name = "search/view.html"

        def get_queryset(self, *args, **kwargs):
                request = self.request
                print(request.GET)
                query = request.GET.get('q')
                if query is not None:
                        return Product.objects.search(query)
                return Product.objects.none()