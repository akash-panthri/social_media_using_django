from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.CharField(max_length=255)
    id_user = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    profileimg = models.ImageField(upload_to='profile_images')
    location = models.CharField(max_length=255)
