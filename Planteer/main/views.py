from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Contact
from plants.models import Plant

# Create your views here.

def home_view(request:HttpRequest):
    plants = Plant.objects.all()[0:3]
    return render(request, 'main/home.html', {'plants': plants})


def contact_view(request:HttpRequest):
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        return redirect('main:home_view')

    return render(request, 'main/contact.html')

def messages_view(request:HttpRequest):
    msgs = Contact.objects.all().order_by('-created_at')
    return render(request, 'main/messages.html', {'messages': msgs})