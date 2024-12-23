from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
#from templates.pages import home.html
# Create your views here.

class HomePage(TemplateView):
    templete_name = "home.html"
    
class AboutPage(TemplateView):
    template_name = "about.html"
    
