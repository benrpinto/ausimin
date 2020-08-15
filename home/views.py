from django.shortcuts import render
from .models import SiteContent

def home(request):
   carouselContent  = SiteContent.objects.filter(content_loc='HomeCarousel')
   marketingContent = SiteContent.objects.filter(content_loc='HomeMarketing')
   context = {
              'car_cont' :carouselContent,
              'mark_cont':marketingContent,
              'app_text':"Home",
              'app_name':"Home"
             }
   return render(request, 'home/home.html', context)


# Create your views here.
