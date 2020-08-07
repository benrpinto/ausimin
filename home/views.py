from django.shortcuts import render
from .models import SiteContent

def homepage(request):
   carouselContent  = SiteContent.objects.filter(content_loc='HomeCarousel')
   marketingContent = SiteContent.objects.filter(content_loc='HomeMarketing')
   context = {
              'car_cont' :carouselContent,
              'mark_cont':marketingContent
             }
   return render(request, 'home/home.html', context)
# Create your views here.
