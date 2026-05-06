from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Organism

User = get_user_model()


class OrganismModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='password123')
        self.organism = Organism.objects.create(name='lion', user=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.organism), 'lion')

    def test_default_choice_values(self):
        self.assertEqual(self.organism.ecosystem, Organism.Ecosystem.UNKNOWN)
        self.assertEqual(self.organism.weather, Organism.Weather.OTHER)
        self.assertFalse(self.organism.edibility)
        self.assertIsNotNone(self.organism.date)


class OrganismViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='viewer', password='password123')
        self.client.login(username='viewer', password='password123')
        self.organism = Organism.objects.create(name='oak', user=self.user)

    def test_home_get_renders_form_authenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'natureShareApp/home.html')
        self.assertIn('form', response.context)

    def test_home_get_guest_access(self):
        """Guests can view the home page with the organism gallery."""
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'natureShareApp/home.html')
        self.assertIn('organism_images', response.context)
        # Guest should not have a form
        self.assertIsNone(response.context.get('form'))

    def test_home_post_creates_organism(self):
        response = self.client.post(reverse('home'), {
            'name': 'maple',
            'edibility': 'on',
            'ecosystem': Organism.Ecosystem.OTHER,
            'weather': Organism.Weather.OTHER,
            'date': timezone.now().date().isoformat(),
            'location': '',
        })
        self.assertRedirects(response, reverse('organism_images'))
        self.assertTrue(Organism.objects.filter(name='maple', user=self.user).exists())

    def test_organism_images_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('organism_images'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_search_results(self):
        response = self.client.get(reverse('search_results') + '?q=oak')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'oak')

    def test_update_permission_is_restricted(self):
        other_user = User.objects.create_user(username='other', password='password123')
        other_organism = Organism.objects.create(name='pine', user=other_user)
        response = self.client.get(reverse('edit', kwargs={'pk': other_organism.pk}))
        self.assertEqual(response.status_code, 404)

    def test_delete_permission_is_restricted(self):
        other_user = User.objects.create_user(username='other2', password='password123')
        other_organism = Organism.objects.create(name='birch', user=other_user)
        response = self.client.post(reverse('delete', kwargs={'pk': other_organism.pk}))
        self.assertEqual(response.status_code, 404)

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