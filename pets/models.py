from django.db import models
from django.contrib.postgres.fields import ArrayField


class Pet(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    animal = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    size = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    breed = models.CharField(max_length=30)
    altered = models.BooleanField()
    shots = models.BooleanField()
    special_needs = models.BooleanField()
    photos = ArrayField(models.URLField())
    shelter = models.ForeignKey('pets.Shelter', on_delete=models.CASCADE)


class Shelter(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
