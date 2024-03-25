from django.db import models
from django.contrib.auth.models import User
from django_countries import countries
from PIL import Image

class Profile(models.Model):
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
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save_img(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class DoctorUserChat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='sent_messages', null=True)
    recipient = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='received_messages', null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"From: {self.sender} | To: {self.recipient} | Content: {self.content}"

    def delete(self, *args, **kwargs):
        # Override delete method to mark message as deleted
        self.is_deleted = True
        self.save()