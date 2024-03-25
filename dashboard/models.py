from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from userProfile.models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
def validate_positive_integer(value):
    if value < 0:
        raise ValidationError('Value must be a positive integer')

def validate_max_value(value):
    max_value = 10  # Change this to your desired maximum value
    if value > max_value:
        raise ValidationError(f'Value must be less than or equal to {max_value}')
    

class Doctors(models.Model):
    username = models.OneToOneField(User,  on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length= 150)
    specialization = models.CharField(max_length= 150)
    rating = models.PositiveIntegerField(
        help_text='Enter a doctor rating',
        default=0,
        validators=[validate_positive_integer, validate_max_value]
        )
    cellphone = models.CharField(max_length=15)
    doctor_image = models.ImageField(default='default.jpg', upload_to="doctor_images/")
    address = models.TextField()


    def  __str__(self):
        return f'{self.name}, {self.specialization}'
    

@receiver(post_save, sender=Profile)
def update_doctor_image(sender, instance, created, **kwargs):
    if created:  # If profile instance is created
        # Get the associated doctor instance
        doctor_instance = Doctors.objects.filter(username=instance).first()
        if doctor_instance:
            # Update doctor_image with profile image
            doctor_instance.doctor_image = instance.image
            doctor_instance.save()


class UserMessage(models.Model):
    subject = models.TextField(max_length=200)
    message = models.TextField()
    user_email = models.EmailField(max_length=254)
    send_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()