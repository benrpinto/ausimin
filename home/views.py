from django.shortcuts import render
from .models import SiteContent

def homepage(request):
   carouselContent = []
   carouselContent = SiteContent.objects.all()
   context = {'car_cont':carouselContent}
   return render(request, 'home/home.html', context)
# Create your views here.
