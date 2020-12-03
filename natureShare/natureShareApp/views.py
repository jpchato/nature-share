from django.shortcuts import render, redirect
from .models import Organism

# Create your views here.

def home(request):
    return render(request, 'natureShareApp/home.html')