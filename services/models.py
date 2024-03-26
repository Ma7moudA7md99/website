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
  

class LungCancer(models.Model):
  SMOKING_CHOICES = [(0, 'No'), (1, 'Yes')]
  SMOKING = models.IntegerField(choices=SMOKING_CHOICES)
  YELLOW_FINGERS = models.IntegerField(choices=SMOKING_CHOICES)
  ANXIETY = models.IntegerField(choices=SMOKING_CHOICES)
  PEER_PRESSURE = models.IntegerField(choices=SMOKING_CHOICES)
  CHRONIC_DISEASE = models.IntegerField(choices=SMOKING_CHOICES)
  FATIGUE = models.IntegerField(choices=SMOKING_CHOICES)
  ALLERGY = models.IntegerField(choices=SMOKING_CHOICES)
  WHEEZING = models.IntegerField(choices=SMOKING_CHOICES)
  ALCOHOL_CONSUMING = models.IntegerField(choices=SMOKING_CHOICES)
  COUGHING = models.IntegerField(choices=SMOKING_CHOICES)
  SHORTNESS_OF_BREATH = models.IntegerField(choices=SMOKING_CHOICES)
  SWALLOWING_DIFFICULTY = models.IntegerField(choices=SMOKING_CHOICES)
  CHEST_PAIN = models.IntegerField(choices=SMOKING_CHOICES)
  GENDER_CHOICES = [(0, 'Male'), (1, 'Female')]
  gender = models.IntegerField(choices=GENDER_CHOICES)
  age = models.IntegerField()

  def __str__(self):
    return f'{self.age}'