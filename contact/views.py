from django.shortcuts import render

def contact(request):
   context = {
              'app_text':"Contact Us",
              'app_name':"Contact"
             } 
   return render(request, 'contact/contact.html', context)
# Create your views here.