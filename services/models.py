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
  

class VirusC(models.Model):
  gender_choices = {
    0: 'Male',
    1: 'Female'
  }
  age = models.FloatField( blank=False)
  gender = models.IntegerField(choices=gender_choices, blank=False)
  alb = models.FloatField( blank=False)
  alp = models.FloatField( blank=False)
  alt = models.FloatField( blank=False)
  ast = models.FloatField( blank=False)
  bil = models.FloatField( blank=False)
  che = models.FloatField( blank=False)
  chol = models.FloatField( blank=False)
  crea = models.FloatField( blank=False)
  ggt = models.FloatField( blank=False)
  prot = models.FloatField( blank=False)

  def __str__(self):
    return f'{self.age}'