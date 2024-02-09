from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import traceback

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
      error_message = "Invalid username or password"
      render(request, 'homepage/signin.html', {'error_message': error_message})
  return render(request, 'homepage/signin.html')

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
  if request.method == "POST":
    try:
      model = load_model('static/models/skinCancer.h5')
      # image = request.FILES['uploadImage']
      # with open('static/image/uploads/' + image.name, 'wb+') as destination:
      #     for chunk in image.chunks():
      #           destination.write(chunk)
      img = cv2.imread("E:/graduate/website/website/static/image/36.jpg")
      resize = tf.image.resize(img, (256, 256))
      model_result = model.predict(np.expand_dims(resize / 255, 0))
      result = model_result_text(model_result)
      return render(request, 'skin cancer/skin cancer.html', {'result': result})
    except Exception as e:
      traceback.print_exc()
      print(e)
      return render(request, 'skin cancer/skin cancer.html')
  

  return render(request, 'skin cancer/skin cancer.html')


def model_result_text(model_result):
    percentage = model_result[0] * 100
    if model_result[0] < 0.4:
      result = f'Your result is {percentage[0]:.2f}% \n  It seems that you don\'t have Skin Cancer.'
    elif 0.4 <= model_result[0] < 0.7:
      result  = f"Your result is {percentage[0]:.2f}% \n The lesion may be benign but it could also be malignant."
    else:
      result = f"Your result is {percentage[0]:.2f}%\n Based on the results, there might be a possibility of having Skin Cancer.\n Please consult a doctor immediately!"
    return  result

def medicalTerm(request):
  return render(request,"terminology/terminology.html")