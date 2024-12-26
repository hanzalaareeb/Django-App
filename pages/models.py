from django.db import models

# Create your models here.
class Page(models.Model):  # new 
    text = models.TextField()

    def __str__(self):
        return self.text[:50] # new text