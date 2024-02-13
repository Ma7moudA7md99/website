from django.db import models

# Create your models here.
class SkinCancer(models.Model):
  first_name = models.CharField(max_length= 50)
  last_name = models.CharField(max_length= 50)
  age = models.CharField(max_length= 50)
  image = models.ImageField(upload_to='skin cancer/images', null=False)

  def __str__(self):
    return f'{self.first_name}'
  