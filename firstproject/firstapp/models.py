from django.db import models

# Menu Item Model
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

# Reservation Model
class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)