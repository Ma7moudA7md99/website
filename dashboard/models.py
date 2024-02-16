from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_positive_integer(value):
    if value < 0:
        raise ValidationError('Value must be a positive integer')

def validate_max_value(value):
    max_value = 10  # Change this to your desired maximum value
    if value > max_value:
        raise ValidationError(f'Value must be less than or equal to {max_value}')
    

class Doctors(models.Model):
    name = models.CharField(max_length= 150)
    specialization = models.CharField(max_length= 150)
    rating = models.PositiveIntegerField(
        help_text='Enter a doctor rating',
        default=0,
        validators=[validate_positive_integer, validate_max_value]
        )
    cellphone = models.CharField(max_length=15)
    doctor_image = models.ImageField( default='default.jpg', upload_to="doctor_images/")
    address = models.TextField()


    def  __str__(self):
        return f'{self.name}, {self.specialization}'