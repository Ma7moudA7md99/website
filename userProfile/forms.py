from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import profile
from django.contrib.auth.models import User

class ProfileUserUpdateForm(forms.ModelForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput, required=False)

    class Meta:
        model = profile
        fields = ['first_name', 'last_name','email','gender', 'age', 'country','image']

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.user.check_password(old_password):
            raise forms.ValidationError("Incorrect old password")
        new_first_name  = self.cleaned_data.get('first_name')
        new_last_name = self.cleaned_data.get('last_name')
        new_email = self.cleaned_data.get('email')
        self.instance.user.first_name = new_first_name 
        self.instance.user.last_name = new_last_name
        self.instance.user.email = new_email
        return old_password
    
    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if self.instance.image:
                self.instance.image.delete()  # Delete old image
        return image
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        if new_password1 != new_password2:
            self.add_error('new_password2', "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = self.instance.user
        new_password = self.cleaned_data.get('new_password1')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
        return super().save(commit)
