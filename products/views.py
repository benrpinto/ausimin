from django.shortcuts import render
from .models import PageContent

def products(request):
   productContent = PageContent.objects.filter(content_loc='ProductContent')
   certContent    = PageContent.objects.filter(content_loc='CertContent')
   context = {
              'prod_cont':productContent,
              'cert_cont':certContent,
              'app_text':"Products",
              'app_name':"Products"
             }
   return render(request, 'products/products.html', context)
# Create your views here.
