from django.shortcuts import render, redirect
from django.views.generic import ListView
# Create your views here.
from .forms import RegisterationForm
from django.contrib import messages
from .models import OtpToken
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utils import timezone
from decouple import config
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def signUp(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, "Account created successfully! An OTP was sent to your Email")
            return redirect("verify-email", username=form.cleaned_data['username'])  # Make sure 'username' is a field in your form
    else:
        form = RegisterationForm()  # Create an empty form for GET requests

    context = {"form": form}  # Ensure the context is prepared for rendering
    return render(request, "signup.html", context)  # Always return an HttpResponse


def verify_account(request, username):
    user = get_user_model().object.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()
    
    if request.method == "POST":
        # Validate the token
        if user_otp.otp_code == request.POST['otp_code']:
            # check if otp expired or not
            if user_otp.expier_time > timezone.now():
                user.is_activae = True
                user.save()
                messages.success(request, "otp is valid, verification successful! You can login again")
                return redirect('signin')
            # if OTP expired,
            else:
                messages.warnning(request, "OTP expired or invalid try again")
                return redirect('verify_email', username=user.username)
        
        # if OTP is invalid
        else:
            messages.warnning(request, "Invalid OTP, try again")
            return redirect('verify_email', username=user.username)
    
    context = {}
    return render(request, "verifyToken.html", context)

def resend_token(request):
    if request.method == "POST":
        user_email = request.POST["otp_email"]
        if get_user_model.objects.filter(email= user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp = OtpToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            
            # what are email variables
            subject = "Email ferification"
            message = """
            Hello,      Hi, {user.username}, here is your OTP token
            it expires in 5 minutes, use URL below to redirect to website
            http://127.0.0.1:8000/verify_account/{user.username}
            
            """
            sender = config('EMAIL_HOST_USER')
            reciver = [user.email,]
            
            # send email notification
            send_mail(
                subject,
                message,
                sender,
                reciver,
                fail_silently=False,
            )
            
            messages.success(request, "A new OTP has just been sent to your Email address")
            return redirect('verify_email', username=user.username)
        
        else:
            messages.warnning(request, "Email address does not exist in database")
            return redirect('resend_token')
    
    context = {}
    return render(request, "resendToken.html", context)

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None :
            login(request, user)
            messages.success(request, "Hi, {request.user.username}, You are now logged-in!")
            return redirect('index')
        else:
            messages.warnning(request, "Please enter correct username and password")
            return redirect('signin')
    
    return render(request, "login.html",)