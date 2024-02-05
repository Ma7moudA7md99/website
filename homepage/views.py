from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
  user = User.objects.filter(is_active=True).order_by('username')
  return render(request,'homepage/index.html',{'user':user})


def sign_up_page(request):
  return render(request, 'homepage/signup.html')


def sign_in(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    username = request.POST['username']
    password = request.POST['password']
    user= authenticate(username=username, password=password)

    if user is not None:
      login (request, user)
      return redirect('/')
    else:
      messages.error(request, "Bad Credentials!")
      # return redirect( 'home')
    
  return HttpResponse('wrong')


def sign_up(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    fname = request.POST['firstName']
    lname = request.POST['lastName']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # print(fname, lname, username, email,password)
    newUser = User.objects.create_user(username, email, password)
    newUser.first_name = fname
    newUser.last_name = lname


    newUser.save()
    messages.success(request, 'Your acount has been created')
    # print(email, password)
    return render(request ,'homepage/index.html')
  
  return HttpResponse('wrong')

def send_msg(request):
  if request.method == 'POST':
    subject = request.POST['subject']
    email_sender = request.POST['email-contact']
    message = request.POST['message']

    print(subject)
    print(email_sender)
    print(message)
    send_mail(
      subject,
      message,
      email_sender,
      [settings.EMAIL_HOST_USER],
      fail_silently=False,
    )

  return render(request,'homepage/index.html')