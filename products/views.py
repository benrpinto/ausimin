from django.shortcuts import render
from .models import ProductContent
from .models import UsesContent
from .models import CertContent

def products(request):
   #myProducts = ProductContent.objects
   myCerts    = CertContent.objects.all
   context = {
   #           'prod_cont':myProducts,
              'cert_cont':myCerts,
              'app_text':"Products",
              'app_name':"Products"
             }
   return render(request, 'products/products.html', context)
# Create your views here.
