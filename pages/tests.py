from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HomePageTestCase(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        responce = self.client.get(reverse("home"))
        self.assertEqual(responce.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/about/")
        self.assertEqual(responce.status_code, 200)
    
    def test_url_avilable_by_name(self):
        responce = self.client.get(reverse("about"))
        self.assertEqual(responce.status_code, 200)
        