from django.shortcuts import render
from django.core.mail import send_mail
def contact(request):
   context = {
              'app_text':"Contact Us",
              'app_name':"Contact"
             } 
   return render(request, 'contact/contact.html', context)

def mail(request):
   print("form received")
   send_mail(
      'Subject here',
      'Here is the message.',
      None,
      ['ausimintest@mailinator.com'],
      fail_silently=False,
   )
   return contact(request)
# Create your views here.
