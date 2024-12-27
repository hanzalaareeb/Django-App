from django.shortcuts import render, redirect
from django.views.generic import ListView
# Create your views here.
from .forms import RegisterForm
from django.contrib import messages
from .models import OtpToken
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.utlis import TimeZone

def index(request):
    return render(request, 'index.html')

def signUp(request):
    FORM = RegisterForm()
    
    if request.method == 'POST':
        FORM = RegisterForm(request.post)
        if FORM.is_valid():
            FORM.save()
            messages.success(request, 'Account created successfully! OTP sent to your email address.')    
            return redirect("verify_account", usernmae=request.POST['username'])
        context = {'form': FORM}
        return render(request, 'signup.html', context)


def verify_account(request, username):
    user = get_user_model().object.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()
    
    if request.method == "POST":
        # Validate the token
        if user_otp.otp_code == request.POST['otp_code']:
            # check if otp expired or not
            if user_otp.expier_time > TimeZone.now():
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
            otp = OtpToken.objects.create(user=user, otp_expires_at=TimeZone.now() + TimeZone.timedelta(minutes=5))
            