from django.urls import path, include
from core import views

urlpatterns = [
    path('index/', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('shop/', views.shop, name='shop'),
    path('thankyou/', views.thankyou, name='thankyou'),

]