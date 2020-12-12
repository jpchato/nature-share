from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Organism
from .forms import *
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = OrganismForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            plural_organism = Organism.objects.all()
            return render(request, 'natureShareApp/images.html', {'organism_images' : plural_organism})
    
    else:
        form = OrganismForm()
    return render(request, 'natureShareApp/home.html', {'form' :  form})

# https://www.geeksforgeeks.org/python-uploading-images-in-django/

def display_images(request):
    if request.method == 'GET':
        plural_organism = Organism.objects.all()
        # return render((request, 'natureShareApp/images.html', {'organism_images' : plural_organism}))
        return render(request, 'natureShareApp/images.html', {'organism_images' : plural_organism})

class OrganismDetailView(generic.DetailView):
    model = Organism

class SearchResultsView(ListView):
    model = Organism
    template_name = 'natureShareApp/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Organism.objects.filter(Q(ecosystem__icontains=query))
        return object_list

class OrganismUpdate(UpdateView):
    model = Organism
    fields = ['name', 'edibility', 'ecosystem', 'weather', 'date', 'location']
    template_name_suffix = '_update_form'
    success_url ="/organism_images"

class OrganismDelete(DeleteView):
    model = Organism

    success_url = '/organism_images'