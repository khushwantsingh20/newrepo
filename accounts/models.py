
from django.db import models
from django.contrib.auth.models import User
from django.db import models


# models.py

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True , null=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    postcode = models.CharField(max_length=10)
    landmark = models.CharField(max_length=250)
    def __str__(self):
        return self.user.username  # Display the username as the profile name



   
