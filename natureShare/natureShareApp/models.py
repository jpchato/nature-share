from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Organism(models.Model):
    # picture = 
    name = models.CharField(max_length=255, blank=True, null=True)
    # location = 
    edibility = models.BooleanField(blank=True, null=True)
    class Ecosystem(models.TextChoices):
        TEMPERATE_RAINFOREST = 'Temperate Rainforest',
        TROPICAL_RAINFOREST = 'Tropical Rainforest',
        DESERT = 'DESERT',
        GRASSLAND = 'Grassland',
        TAIGA = 'Taiga',
        TUNDRA = 'Tundra',
        CHAPARRAL = 'Chaparral',
        OCEAN = 'Ocean'
    ecosystem = models.CharField(
        choices = Ecosystem.choices,
        blank = True,
        null = True
    )
    # weather = 
    # date = 
