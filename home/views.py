from django.shortcuts import render
from .models import CarouselContent
from .models import PageContent

def home(request):
   carouselContent  = CarouselContent.objects.filter(content_loc='HomeCarousel')
   marketingContent = PageContent.objects.filter(content_loc='HomeMarketing')
   context = {
              'car_cont' :carouselContent,
              'mark_cont':marketingContent,
              'app_text':"Home",
              'app_name':"Home"
             }
   return render(request, 'home/home.html', context)


# Create your views here.
