import datetime
from django.test import TestCase
from natureShareApp.models import Organism
from django.utils import timezone

class OrganismTestCase(TestCase):
    def setUp(self):
        Organism.objects.create(name="lion")
        # Organism.objects.create(date=datetime.now)

    def test_name_label(self):
        organism = Organism.objects.get(id=1)
        field_label = organism._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # def test_Organisms_can_speak(self):
    #     """Organisms that can speak are correctly identified"""
    #     lion = Organism.objects.get(name="lion")
    #     cat = Organism.objects.get(name="cat")
    #     self.assertEqual(lion, 'lion')
    #     self.assertEqual(cat, 'cat')

# class Ecosystem(models.TextChoices):
#         TEMPERATE_RAINFOREST = 'Temperate Rainforest',
#         TROPICAL_RAINFOREST = 'Tropical Rainforest',
#         DESERT = 'Desert',
#         GRASSLAND = 'Grassland',
#         TAIGA = 'Taiga',
#         TUNDRA = 'Tundra',
#         CHAPARRAL = 'Chaparral',
#         OCEAN = 'Ocean',
#         UNKNOWN = 'Unknown',
#         OTHER = 'Other'

# class YourTestClass(TestCase):
#     def setUp(self):
#         # Setup run before every test method.
#         pass

#     def tearDown(self):
#         # Clean up run after every test method.
#         pass

#     def test_something_that_will_pass(self):
#         self.assertFalse(False)

#     def test_something_that_will_fail(self):
#         self.assertTrue(False)

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)