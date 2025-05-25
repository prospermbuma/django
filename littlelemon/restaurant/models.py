from django.db import models

# MODELS
# Booking Model
class Booking(models.Model):
   first_name = models.CharField(max_length=200) 
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name

# Menu Model
class Menu(models.Model):
   name = models.CharField(max_length=255)
   price = models.IntegerField()
   description = models.CharField(max_length=1000, default='')
   photo = models.ImageField(upload_to='menu_photos/', default='')
   
   def __str__(self):
      return self.name