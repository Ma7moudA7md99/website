from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
import urllib.request
import json, socket, pytz
# Create your views here.


def profile_page(request):
    if request.method == 'POST':
        form = ProfileUserUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            login(request, request.user)
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = ProfileUserUpdateForm(instance=request.user.profile, initial={
            # 'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'gender':request.user.profile.gender,
            'country':request.user.profile.country,
            'age': request.user.profile.age,
            'image': request.user.profile.image,
        })
    return render(request, 'profile.html', {'form': form})


# doctor dashboard
def doctor_dash(request):
    doctor = Doctors.objects.get(username= request.user)
    doctor_messages = DoctorUserChat.objects.filter(recipient= doctor.username)
    grouped_messages = {}
    for message in doctor_messages:
        if message.sender not in grouped_messages:
            grouped_messages[message.sender] = []
        grouped_messages[message.sender].append({'message': message.content, 'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S.%f%z')})

    if request.method == "POST":
        form = DoctorUpdate(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request,"Information Updated Successfully")
    form = DoctorUpdate(instance=doctor, initial={
        'cellphone': doctor.cellphone,
        'address': doctor.address,
    })
    return render(request, 'doctor_dash.html', {'doctor': doctor, 'form':form, 'user_messages':grouped_messages})

from django.http import HttpResponse
from django.template.loader import render_to_string

def send(request):
    sender = request.POST['sender']
    receiver = request.POST['receiver']
    content = request.POST['message']
    print(sender, receiver, content)
    new_message = DoctorUserChat.objects.create(sender= User.objects.get(username=sender), recipient = User.objects.get(username=receiver), content = content)
    new_message.save()
    data = {
        'message': new_message.content,
        'date': new_message.timestamp.strftime("%d-%m %Y %H:%M"),  # Example output: "September 01 2017 03:46"
    }
    return JsonResponse(data)


def show_messages(request):
    # Retrieve all messages sent to and from the doctor, ordered by timestamp in descending order
    doctor_messages_sent = DoctorUserChat.objects.filter(sender=request.user).order_by('-timestamp')
    doctor_messages_received = DoctorUserChat.objects.filter(recipient=request.user).order_by('-timestamp')

    # Combine sent and received messages and sort them by timestamp
    all_doctor_messages = list(doctor_messages_sent) + list(doctor_messages_received)
    all_doctor_messages.sort(key=lambda message: message.timestamp, reverse=True)

    # Retrieve user's IP address
    

    # Prepare data to send as JSON
    messages = []
    for message in all_doctor_messages:
        # Convert timestamp to user's timezone
        user_timestamp = message.timestamp.astimezone(pytz.timezone('Africa/Cairo'))
        # Format timestamp in user's timezone
        formatted_timestamp = user_timestamp.strftime('%Y-%m-%d %H:%M:%S')

        messages.append({
            'timestamp': formatted_timestamp,
            'sender': message.sender.username,
            'content': message.content,
        })

    return JsonResponse({'messages': messages})
