from datetime import datetime
from django.test import TestCase
from natureShareApp.models import Organism
from django.utils import timezone

class OrganismTestCase(TestCase):
    def setUp(self):
        Organism.objects.create(name="lion")
        Organism.objects.create(edibility=True)
        Organism.objects.create(ecosystem='Temperate Rainforest')
        Organism.objects.create(weather='Sunny')
        Organism.objects.create(date=datetime.now()) 
    
    def setUp_2(self):
        Organism.objects.create(name="lion")
        Organism.objects.create(edibility=False)
        Organism.objects.create(ecosystem='Tropical Rainforest')
        Organism.objects.create(weather='Sunny')
        Organism.objects.create(date=datetime.now()) 

    def test_name_label(self):
        organism = Organism.objects.get(id=1)
        name_label = organism._meta.get_field('name').verbose_name
        date_label = organism._meta.get_field('date').verbose_name
        self.assertEqual(name_label, 'name')
        self.assertEqual(date_label, 'date')

    def test_edibility_label(self):
        organism = Organism.objects.get(id=1)
        edibility_label = organism._meta.get_field('edibility').verbose_name
        self.assertEqual(edibility_label, 'edibility')

    def test_edibility_label_notequal(self):
        organism = Organism.objects.get(id=1)
        edibility_label = organism._meta.get_field('edibility').verbose_name
        print(edibility_label)
        self.assertNotEqual(edibility_label, 'edibility')

    def test_edibility_false_label(self):
        organism = Organism.objects.get(id=2)
        edibility_label = organism._meta.get_field('edibility').verbose_name
        self.assertEqual(edibility_label, 'edibility')
        
    def test_weather_label(self):
        organism = Organism.objects.get(id=1)
        weather_label = organism._meta.get_field('weather').verbose_name
        self.assertEqual(weather_label, 'weather')
        