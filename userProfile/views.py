from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.


def profile(request):
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