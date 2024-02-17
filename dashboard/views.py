from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Doctors
from userProfile.models import profile
from .forms import DoctorForm

# Create your views here.
# function to render dashboard page
def dashboard(request):
    doctors = Doctors.objects.all()
    users = User.objects.all()
    return render(request, 'dashboard.html', {'doctors': doctors, 'users': users})


def update_doctor(request, doctor_id):
    
    doctor = Doctors.objects.get(id= doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('dash')  # Redirect to the list of doctors page
        else:
            messages.error(request, 'something went wrong')
    else:
        form = DoctorForm(instance=doctor, initial={
            'name':doctor.name,
            'specialization':doctor.specialization,
            'rating':doctor.rating,
            'doctor_image':doctor.doctor_image,
            'address': doctor.address
        })

    return render(request, 'update.html', {'form': form, 'doctor': doctor, 'btn_title': 'Update'})

def add_doctor(request):
    form = DoctorForm()
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                return redirect('dash') 
    return render(request, 'update.html', {'form': form, 'btn_title': 'Add new doctor'})

def delete_(request, id_delete):
    if Doctors.objects.filter(id=id_delete).exists():
        doctor = Doctors.objects.get(id= id_delete)
        doctor.delete()
    else:
        user = User.objects.get(id=id_delete)
        user.delete()
    return redirect('dash')