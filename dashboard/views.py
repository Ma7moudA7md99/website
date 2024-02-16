from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctors
from .forms import DoctorForm

# Create your views here.
# function to render dashboard page
def dashboard(request):
    doctors = Doctors.objects.all()
    return render(request, 'dashboard.html', {'doctors': doctors})


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