from django.shortcuts import render
from .models import PageContent

def applications(request):
   applicationsContent = PageContent.objects.filter(content_loc='ApplContent')
   context = {
              'appl_cont':applicationsContent,
              'app_text':"Applications",
              'app_name':"Applications"
             }
   return render(request, 'applications/applications.html', context)
# Create your views here.
