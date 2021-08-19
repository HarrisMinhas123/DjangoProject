from typing import cast
from django.db import models

class Profile(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F','Female')]
    name= models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    cast = models.CharField(max_length=30)
    submission_date = models.DateTimeField()
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Projects(models.Model):
    name  = models.CharField(max_length=50)
    tech_stack = models.TextField()
    description = models.TextField()