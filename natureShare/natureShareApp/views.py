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
            # return redirect('success')
            plural_organism = Organism.objects.all()
            return render(request, 'natureShareApp/images.html', {'organism_images' : plural_organism})
    
    else:
        form = OrganismForm()
    return render(request, 'natureShareApp/home.html', {'form' :  form})

def success(request):
    return HttpResponse('IT WORKED')

# https://www.geeksforgeeks.org/python-uploading-images-in-django/
def display_images(request):
    if request.method == 'GET':
        plural_organism = Organism.objects.all()
        # return render((request, 'natureShareApp/images.html', {'organism_images' : plural_organism}))
        return render(request, 'natureShareApp/images.html', {'organism_images' : plural_organism})