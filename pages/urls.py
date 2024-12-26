from django.urls import path
from .views import HomePage, AboutPage, ContactPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),  # Home page
    path('about/', AboutPage.as_view(), name='about'),  # About page
    path('contact/', ContactPage.as_view(), name='contact'),  # Contact page
]
