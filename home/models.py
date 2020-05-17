from django.db import models

class Register(models.Model):
  first_name=models.CharField(max_length=50)
  middle_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  mobile_number=models.CharField(max_length=15)
  collage_name=models.CharField(max_length=100)
  gender=models.CharField(max_length=10)
  hobbies=models.CharField(max_length=100)

  def __str__(self):
      return self.first_name



# Create your models here.
