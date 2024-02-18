from django.db import models
from datetime import *

# Create your models here.
class SkinCancer(models.Model):
  current_date = datetime.now()
  first_name = models.CharField(max_length= 50)
  last_name = models.CharField(max_length= 50)
  age = models.CharField(max_length= 50)
  image = models.ImageField(upload_to=f'skin cancer/images/{str(current_date.year)}/{str(current_date.month)}/{str(current_date.day)}', null=False)

  def __str__(self):
    return f'{self.first_name}'
  