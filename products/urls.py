
from django.conf.urls import url
from django.urls import path


from .views import  (
ProductListView,
ProductDetailSlugView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug>/', ProductDetailSlugView.as_view(), name='detail'),

]