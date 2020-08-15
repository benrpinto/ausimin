from django.shortcuts import render

def products(request):
   context = {
              'app_text':"Products",
              'app_name':"Products"
             }
   return render(request, 'products/products.html', context)
# Create your views here.
