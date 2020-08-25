from django.shortcuts import render
from .models import PageContent

def products(request):
   productContent = PageContent.objects.filter(content_loc='ProductContent')
   context = {
              'prod_cont':productContent,
              'app_text':"Products",
              'app_name':"Products"
             }
   return render(request, 'products/products.html', context)
# Create your views here.
