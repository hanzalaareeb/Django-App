from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.signUp, name="register"),
    path("verify-email/<slug:username>", views.verify_account, name="verify-email"),
    path("resend-otp", views.resend_token, name="resend-token"),
    path("login", views.signin, name="signin")
]