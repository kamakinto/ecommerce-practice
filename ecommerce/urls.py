"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.urls import path
from .views import home_page, about_page, contact_page
from accounts.views import login_page, register_page, guest_register_page
from carts.views import cart_home


urlpatterns = [
    path('', home_page, name='homepage'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
     path('register/guest/', guest_register_page, name='guest_register'),
    path('register/', register_page, name='register'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('products/', include(("products.urls",  'products'), namespace='products')),
    path('cart/', include(("carts.urls",  'cart'), namespace='cart')),
    path('search/', include(('search.urls', 'search'), namespace='search')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
