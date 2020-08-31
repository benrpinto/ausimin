from django.shortcuts import render
from django.core.mail import send_mail
def contact(request):
   context = {
              'app_text':"Contact Us",
              'app_name':"Contact"
             } 
   return render(request, 'contact/contact.html', context)

def mail(request):
   if (request.method == "POST"):
      print("form received")
      subject = "Message from "\
      + request.POST['honorific'] +" "\
      + request.POST['fName'] + " "\
      + request.POST['lName']
      message_body = "Company: " + request.POST['company']\
      + "\n" + "Country: " + request.POST['country']\
      + "\n" + "Email: "   + request.POST['emailAddress']\
      + "\n" + "Phone: "   + request.POST['phone']\
      + "\n" + "Reason: "  + request.POST['reason']\
      + "\n" + "Message: " + request.POST['message']
      send_mail(
         subject,
         message_body,
         None,
         ['ausimintest@mailinator.com'],
         fail_silently=False,
      )
   return contact(request)
# Create your views here.
