from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userProfile.models import profile
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import traceback

# Create your views here.
# function to render and load html content for home page
def home(request):
  return render(request,template_name='index.html')

# function to render and load html content for sign up page
# and it creates a new user too 
def sign_up(request):
  if request.method == 'POST':
    # Get the username and password provided by the user.
    fname = request.POST['firstName']
    lname = request.POST['lastName']
    username = request.POST['username']
    gender = request.POST['gender']
    country = request.POST['country']
    email = request.POST['email']
    age = request.POST['age']
    password = request.POST['password']

    newUser = User.objects.create_user(username, email, password)
    newUser.first_name = fname
    newUser.last_name = lname
    newUser.save()
    profile.objects.create(user=newUser, age=age, gender=gender, country=country).save()
    login(request, newUser)
    return redirect('home')
  return render(request, 'signup.html')

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
      print(user)
      render(request, 'signin.html')
  return render(request, 'signin.html')

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

  return render(request,'index.html')
# function to logout 
def log_out(request):
  logout(request)
  return redirect('home')
# function to render skin cancer page
