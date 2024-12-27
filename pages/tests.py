from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from .models import Page

# Create your tests here.


class HomePageTestCase(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        responce = self.client.get(reverse("pages/home"))
        self.assertEqual(responce.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        responce = self.client.get("/about/")
        self.assertEqual(responce.status_code, 200)
    
    def test_url_avilable_by_name(self):
        responce = self.client.get(reverse("about"))
        self.assertEqual(responce.status_code, 200)
        
class PageTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.page = Page.objects.create(text = "this is method test")
        
    def test_model_contents(self):
        self.assertEqual(self.page.text, "this is method test")
        
        """only the functions starting with "test" will be called when 
        ```
        python manage.py test
        ```
        Is run in the terminal.
        """
    def test_urls_exist_at_correct_loccation(self):
        responce = self.client.get("/")
        self.assertEqual(responce.status_code, 200)
    
    def test_url_available_by_name(self):
        responce = self.client.get(reverse("home"))
        self.assertEqual(responce.status_code, 200)
    
    def test_templete_name_correct(self):
        responce = self.client.get("home")
        self.assertTemplateUsed(responce, "home.html")
        
    def test_template_content(self):
        responce = self.client.get(reverse("home"))
        self.assertContains(responce, "this is method test")