from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from location_field.models.plain import PlainLocationField

User = get_user_model()


class Organism(models.Model):
    """A shared organism observation with image, location, and metadata."""

    picture = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=255)
    location = PlainLocationField(
        based_fields=['ecosystem'],
        zoom=18,
        blank=True,
        null=True,
        default='45.502978246693786,-122.67608642578126',
    )
    edibility = models.BooleanField(default=False)

    class Ecosystem(models.TextChoices):
        TEMPERATE_RAINFOREST = 'Temperate Rainforest', 'Temperate Rainforest'
        TROPICAL_RAINFOREST = 'Tropical Rainforest', 'Tropical Rainforest'
        DESERT = 'Desert', 'Desert'
        GRASSLAND = 'Grassland', 'Grassland'
        TAIGA = 'Taiga', 'Taiga'
        TUNDRA = 'Tundra', 'Tundra'
        CHAPARRAL = 'Chaparral', 'Chaparral'
        OCEAN = 'Ocean', 'Ocean'
        UNKNOWN = 'Unknown', 'Unknown'
        OTHER = 'Other', 'Other'

    ecosystem = models.CharField(
        choices=Ecosystem.choices,
        max_length=32,
        blank=True,
        default=Ecosystem.UNKNOWN,
    )

    class Weather(models.TextChoices):
        SUNNY = 'Sunny', 'Sunny'
        CLOUDY = 'Cloudy', 'Cloudy'
        RAINY = 'Rainy', 'Rainy'
        WINDY = 'Windy', 'Windy'
        SNOWY = 'Snowy', 'Snowy'
        OTHER = 'Other', 'Other'

    weather = models.CharField(
        choices=Weather.choices,
        max_length=32,
        blank=True,
        default=Weather.OTHER,
    )

    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organisms')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organism-detail', kwargs={'pk': self.pk})
