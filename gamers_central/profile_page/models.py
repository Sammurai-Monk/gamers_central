from django.db import models

# Create your models here.
class ProfilePage(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=15)
    password_confirmation = models.CharField(max_length=15)
    