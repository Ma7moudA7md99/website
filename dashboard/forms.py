from django import forms
from .models import Doctors

class DoctorForm(forms.ModelForm):
    doctor_image = forms.ImageField()

    class Meta:
        model = Doctors
        fields = ['name', 'specialization', 'rating', 'cellphone', 'doctor_image', 'address']

    def save(self, commit=True):
        doctor = super(DoctorForm, self).save(commit=False)
        if self.cleaned_data['doctor_image']:
            doctor.doctor_image = self.cleaned_data['doctor_image']
        if commit:
            doctor.save()
        return doctor