# from django.test import TestCase
# from natureShareApp.models import Organism

# class OrganismTestCase(TestCase):
#     def setUp(self):
#         Organism.objects.create(name="lion", sound="roar")
#         Organism.objects.create(name="cat", sound="meow")

#     def test_Organisms_can_speak(self):
#         """Organisms that can speak are correctly identified"""
#         lion = Organism.objects.get(name="lion")
#         cat = Organism.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')