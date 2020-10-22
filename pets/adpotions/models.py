from django.db import models


class Pet(models.Model):  # inherits from models.Model
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]  # relates to "choices=" command
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)  # if we set this as blank, it'll store a 0 instead of a blank
    vaccinations = models.ManyToManyField('Vaccine', blank=True)  # relates to the string model "Vaccine" class


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
