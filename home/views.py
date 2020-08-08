from django.shortcuts import render
from .models import SiteContent

def home(request):
   carouselContent  = SiteContent.objects.filter(content_loc='HomeCarousel')
   marketingContent = SiteContent.objects.filter(content_loc='HomeMarketing')
   context = {
              'car_cont' :carouselContent,
              'mark_cont':marketingContent
             }
   return render(request, 'home/home.html', context)

def products(request):
   return render(request, 'products/products.html')

def about(request):
   return render(request, 'about/about.html')

def contact(request):
   return render(request, 'contact/contact.html')
# Create your views here.
