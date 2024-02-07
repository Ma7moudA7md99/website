from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# function to render and load html content for home page
def home(request):
  return render(request,'homepage/index.html')

# function to render and load html content for sign up page
# and it creates a new user too 
def sign_up(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    fname = request.POST['firstName']
    lname = request.POST['lastName']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    newUser = User.objects.create_user(username, email, password)
    newUser.first_name = fname
    newUser.last_name = lname
    newUser.save()

    messages.success(request, 'Your acount has been created')
    login(request, newUser)
    return redirect('home')
  return render(request, 'homepage/signup.html')

# function to render and load html content for sign in page
# and it check if the information's from the user is signed or not
def sign_in(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    username = request.POST['username']
    password = request.POST['password']
    user= authenticate(username=username, password=password)

    if user is not None:
      login (request, user)
      return redirect('/', user)
    else:
<<<<<<< HEAD
      render(request, 'homepage/signin.html', authorized=False)
      # return redirect( 'home')
    
  return redirect('sign_in')

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
=======
      render(request, 'homepage/signin.html')
  return render(request, 'homepage/signin.html')
>>>>>>> 16e1d5c2c1ba9b5a297f0ab97741c06d2b4cef98

# function that send a message from contact section
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
      from_email=email_sender,
      recipient_list=['nasr66440@gmail.com'],
      fail_silently=False,
    )

  return render(request,'homepage/index.html')
# function to logout 
def log_out(request):
  logout(request)
  return redirect('home')
# function to render skin cancer page
def skinCancer(request):
  return render(request,"skin cancer/skin cancer.html")