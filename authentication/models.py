from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
import secrets


# Create your models here.


def createCustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    

class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otp_token')
    otp = models.CharField(max_length=6, default=secrets.token_hex(3))
    create_time = models.DateTimeField(auto_now_add=True)
    expier_time = models.DateTimeField(auto_now=True)
    # is_verified = models.BooleanField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
        
    
