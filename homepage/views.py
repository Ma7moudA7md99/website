from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userProfile.models import Profile
from dashboard.models import UserMessage, Doctors

# Create your views here.
# function to render and load html content for home page
def home(request):

  user_doctor = False
  if request.user.is_authenticated:
    if Doctors.objects.filter(username=request.user).exists():
      user_doctor = True
  
  return render(request,'index.html', {"is_doctor":user_doctor})

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
    # checks if the username is used before or not
    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username is already taken !!')
      return render(request,'signUp.html')
    # checks if the email is used before or not
    elif User.objects.filter(email=email).exists():
      messages.error(request, 'This email is used before')
      return render(request,'signUp.html')
    elif len(username) < 7:
      messages.error(request, 'Username must be bigger than 7 characters')
      return render(request,'signUp.html')
    else:
      newUser = User.objects.create_user(username, email, password)
      newUser.first_name = fname
      newUser.last_name = lname
      newUser.save()
      try:
        Profile.objects.create(user=newUser, username=username,first_name = fname,last_name = lname,age=age, gender=gender, country=country).save()
      except Exception as r: 
        print(r)
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


    user = authenticate(username=username, password=password)
    profile = Profile.objects.get(user=user)
    try:
        doctor_profile = Doctors.objects.get(username=user)
    except:
      messages.error(request, 'No User Exists Please <a href="/#sign_up">Sign up</a>')
      doctor_profile = False
    if user is not None:
      if not user.is_active:
        messages.error(request, 'Your account is suspended for now. Please <a href="/#contact">contact us</a> for assistance.')
      login (request, user)
      if user.is_staff:
        return redirect('dash')
      if doctor_profile:
        return redirect('doctor dashboard')
      return redirect('/', user)
    else:
      messages.error(request, 'Wrong username or password')
      
  return render(request, 'signin.html')

# function that send a message from contact section
def send_msg(request):
  if request.method == 'POST':
    subject = request.POST['subject']
    email_sender = request.POST['email-contact']
    message = request.POST['message']

    msg = UserMessage.objects.create(user_email= email_sender)
    msg.subject = subject
    msg.message = message
    msg.save()

    return HttpResponse()
# function to logout 
def log_out(request):
  logout(request)
  return redirect('home')
