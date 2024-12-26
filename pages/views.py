from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView
#from templates.pages import home.html
from .models import Page
# Create your views here.

class HomePage(ListView):
    model = Page
    template_name = "pages/home.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context['posts'])  # Debug: Print posts to console
        return context

    
class AboutPage(TemplateView):
    template_name = "about.html"
    
class ContactPage(TemplateView):
    template_name = "contact.html"
