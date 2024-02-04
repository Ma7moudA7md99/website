from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request, 'homepage/index.html')

def sign_up_page(request):
  return render(request, 'homepage/signup.html')


def sign_in(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    username = request.POST['email']
    password = request.POST['password']
    print(username, password)
    return HttpResponse('i did it')
  return HttpResponse('wrong ')


def sign_up(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    fname = request.POST['firstName']
    lname = request.POST['lastName']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    print(fname, lname, username, email,password)
    newUser = User.objects.create(username, email, password)
    newUser.first_name = fname
    newUser.last_name = lname


    newUser.save()
    messages.success(request, 'Your acount has been created')
    print(email, password)
    return render(request ,'homepage/index.html')
  
  return HttpResponse('wrong')

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