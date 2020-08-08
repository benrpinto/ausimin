from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='Home'),
   path('products/', views.products, name='Products'),
   path('about/', views.about, name='About Us'),
   path('contact/', views.contact, name='Contact Us'),
]
