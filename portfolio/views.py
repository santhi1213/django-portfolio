from django.shortcuts import render
from .models import Contents

def home(request):
    data = Contents.objects.all()
    return render(request, 'portfolio/home.html', {'data':data})


def email(request):
    return render(request, 'portfolio/Email.html')


def mobile(request):
    return render(request, 'portfolio/contact.html')