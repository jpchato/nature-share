from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from location_field.models.plain import PlainLocationField
from django import forms
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Organism(models.Model):
    picture = models.ImageField(upload_to='images/', default = None)
    name = models.CharField(
        max_length=255, 
        blank = False
        )
    # https://readthedocs.org/projects/django-location-field/downloads/pdf/latest/
    # default coordinates for Portland
    location = PlainLocationField(based_fields=['ecosystem'], zoom=18, blank=True, null=True, default='45.502978246693786,-122.67608642578126')
    edibility = models.BooleanField(blank=True, null=True)
    class Ecosystem(models.TextChoices):
        TEMPERATE_RAINFOREST = 'Temperate Rainforest',
        TROPICAL_RAINFOREST = 'Tropical Rainforest',
        DESERT = 'Desert',
        GRASSLAND = 'Grassland',
        TAIGA = 'Taiga',
        TUNDRA = 'Tundra',
        CHAPARRAL = 'Chaparral',
        OCEAN = 'Ocean',
        UNKNOWN = 'Unknown',
        OTHER = 'Other'
    ecosystem = models.CharField(
        choices = Ecosystem.choices,
        blank = True,
        null = True,
        max_length = 255
    )
    class Weather(models.TextChoices):
        SUNNY = 'Sunny',
        CLOUDY = 'Cloudy',
        RAINY = 'Rainy',
        WINDY = 'Windy',
        SNOWY = 'Snowy',
        OTHER = 'Other'
    weather = models.CharField(
        choices = Weather.choices,
        blank = True,
        null = True,
        max_length = 255
    )
    date = models.DateTimeField(
        null = False, 
        blank = True, 
        default=datetime.now
        )

    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, default = '')
    
    def __str__(self):
        return self.name
