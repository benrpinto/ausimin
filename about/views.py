from django.shortcuts import render

def about(request):
   context = {
              'app_text':"About Us",
              'app_name':"About"
             }
   return render(request, 'about/about.html', context)
# Create your views here.
