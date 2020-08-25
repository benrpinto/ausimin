from django.shortcuts import render
from .models import PageContent

def about(request):
   aboutContent = PageContent.objects.filter(content_loc='AboutContent')
   context = {
              'ab_cont':aboutContent,
              'app_text':"About Us",
              'app_name':"About"
             }
   return render(request, 'about/about.html', context)
# Create your views here.
