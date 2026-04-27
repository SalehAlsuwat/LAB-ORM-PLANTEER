from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def sign_up(request:HttpRequest):

    if request.method == "POST":
        
        try:
            new_user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            new_user.save() 
            messages.success(request, "Registered User Successfuly", "alert-success")
            return redirect(request.GET.get("next", "/"))
        except Exception as e:
            print(e)


    return render(request, 'accounts/signup.html', {})


def sign_in(request:HttpRequest):

    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect("main:home_view")
        
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")
    return render(request, 'accounts/signin.html', {})


def log_out(request:HttpRequest):

    logout(request)
    messages.success(request, "Logged out successsfully", "alert-warning")

    return redirect(request.GET.get("next", "/"))