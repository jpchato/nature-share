import datetime
from django.test import TestCase
from natureShareApp.models import Organism
from django.utils import timezone

class OrganismTestCase(TestCase):
    def setUp(self):
        Organism.objects.create(name="lion")
        Organism.objects.create(edibility=True)
        Organism.objects.create(ecosystem='True')
        Organism.objects.create(weather='Sunny')
        

    def test_name_label(self):
        organism = Organism.objects.get(id=1)
        name_label = organism._meta.get_field('name').verbose_name
        edibility_label = organism._meta.get_field('edibility').verbose_name
        weather_label = organism._meta.get_field('weather').verbose_name
        self.assertEqual(name_label, 'name')
        self.assertEqual(edibility_label, 'edibility')
        self.assertEqual(weather_label, 'weather')
