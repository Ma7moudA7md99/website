from django.shortcuts import render, redirect
from django.http import JsonResponse
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
        # Get data from the AJAX request
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')
        
        # Check if username or email already exist
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username is already taken !!'})
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'This email is used before'})
        elif len(username) < 7:
            return JsonResponse({'success': False, 'message': 'Username must be bigger than 7 characters'})
        else:
            # Create new user and profile
            newUser = User.objects.create_user(username, email, password)
            newUser.first_name = fname
            newUser.last_name = lname
            newUser.save()
            try:
                Profile.objects.create(user=newUser, username=username, first_name=fname, last_name=lname, age=age, gender=gender, country=country)
            except Exception as e:
                print(e)
            login(request, newUser)
            return JsonResponse({'success': True, 'redirect_url': '/'})  # or any other URL you want to redirect to after successful signup

    # If not an AJAX request, return error
    return render(request, 'signup.html')
# function to render and load html content for sign in page
# and it check if the information's from the user is signed or not
def sign_in(request):
    if request.method == 'POST':
        # Get the username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists in the database
        if User.objects.filter(username=username).exists():
            # If username exists, attempt authentication
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Check if the user account is active
                if user.is_active:
                    # Log in the user
                    login(request, user)
                    # Redirect to appropriate dashboard based on user type
                    if user.is_staff:
                        return JsonResponse({'success': True, 'redirect_url': 'dashboard/dash/'})
                    else:
                        return JsonResponse({'success': True, 'redirect_url': '/'})
                else:
                    # Display error message for suspended account
                    return JsonResponse({'success': False, 'message': 'Your account is suspended for now. Please <a href="/#contact">contact us</a> for assistance.'})
            else:
                # Display error message for wrong password
                return JsonResponse({'success': False, 'message': 'Wrong username or password.'})
        else:
            # Display error message for user not found
            return JsonResponse({'success': False, 'message': 'This User does not exist. Please <a href="/sign_up">Sign up</a>'})

    # If the request is not POST, return HTML template
    return render(request, 'signin.html')


# function that send a message from contact section
def send_msg(request):
  if request.method == 'POST':
    subject = request.POST['subject']
    email_sender = request.POST['email-contact']
    message = request.POST['message']
    # save the message in database 
    msg = UserMessage.objects.create(user_email= email_sender)
    msg.subject = subject
    msg.message = message
    msg.save()

    message = "Message Sent Successfully ! \n We will contact you as soon as possible"
    return JsonResponse({'message': message})
  

# function to logout 
def log_out(request):
  logout(request)
  return redirect('home')
