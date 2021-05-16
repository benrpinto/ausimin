from django.shortcuts import render
from .models import CertifyContent
# Create your views here.
def certify(request):
   myCert = CertifyContent.objects.all()
   context = {
              'cert_cont':myCert,
              'app_text':"Certifications",
              'app_name':"Certify"
             }
   return render(request, 'certify/certify.html', context)


