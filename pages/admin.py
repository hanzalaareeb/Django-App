from django.contrib import admin
from .models import Page

# update an app’s admin.py file for it to appear in the admin
admin.site.register(Page)
