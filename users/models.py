from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_location = models.CharField(max_length=50)
    facebook_id = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    profile_pic = models.URLField()
    animal_preference = models.CharField(max_length=50)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
