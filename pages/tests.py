from django.test import TestCase, SimpleTestCase


# Create your tests here.

class HomePageTestCase(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/about/")
        self.assertEqual(responce.status_code, 200)
        