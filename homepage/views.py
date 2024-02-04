from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
  
  return render(request, 'homepage/index.html')

def sign_in(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    username = request.POST['email']
    password = request.POST['password']
    print(username, password)
    return HttpResponse('i did it')
  return HttpResponse('wrong ')

def send_msg(request):
  if request.method == 'POST':
    subject = request.POST['subject']
    email = request.POST['email-contact']
    message = request.POST['message']

    print(subject)
    print(email)
    print(message)
    # send_mail(
    #   subject,
    #   message,
    #   settings.EMAIL_HOST_USER,
    #   [email]
    # )

  return render(request,'homepage/index.html')