
from django.conf.urls import url
from django.urls import path
from .views import SearchProductListView


from products.views import  (
ProductListView,
)

urlpatterns = [
    path('', SearchProductListView.as_view(), name='query'),
]