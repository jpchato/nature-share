from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Organism
from .forms import *

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = OrganismForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    
    else:
        form = OrganismForm()
    return render(request, 'natureShareApp/home.html', {'form' :  form})

def success(request):
    return HttpResponse('IT WORKED')