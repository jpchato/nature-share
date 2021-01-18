from datetime import datetime
from django.test import TestCase
from natureShareApp.models import Organism
from django.utils import timezone
from django.urls import reverse
from natureShareApp.forms import OrganismForm

# Testing model
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
        self.assertNotEqual(edibility_label, 'smile')

    def test_edibility_false_label(self):
        organism = Organism.objects.get(id=2)
        edibility_label = organism._meta.get_field('edibility').verbose_name
        self.assertEqual(edibility_label, 'edibility')
        
    def test_weather_label(self):
        organism = Organism.objects.get(id=1)
        weather_label = organism._meta.get_field('weather').verbose_name
        self.assertEqual(weather_label, 'weather')

# Testing Views
class OrganismViewTest(TestCase):
    def create_organism(self, name='big kitty', ecosystem='Tropical Rainforest'):
        return Organism.objects.create(name=name, ecosystem=ecosystem)

    def test_create_organism(self):
        w = self.create_organism()
        self.assertTrue(isinstance(w, Organism))
        self.assertEqual('big kitty', w.name)

# class WhateverTest(TestCase):

#     def create_whatever(self, title="only a test", body="yes, this is only a test"):
#         return Whatever.objects.create(title=title, body=body, created_at=timezone.now())

#     def test_whatever_creation(self):
#         w = self.create_whatever()
#         self.assertTrue(isinstance(w, Whatever))
#         self.assertEqual(w.__unicode__(), w.title)