from django.db import models
from django.contrib.auth.models import User
from django_countries import countries
from PIL import Image

class profile(models.Model):
    GENDER_CHOICES = {
        'M': 'Male',
        'F': 'Female'
    }
    all_countries = {}
    for code, name in countries:
        all_countries[code] = name

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES.items(), default = 'Male')
    country = models.CharField(max_length = 30,choices=all_countries.items(), default='Eg')
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save_img(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)