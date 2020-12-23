from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Organism
from .forms import *
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views import generic
from django.db.models import Q
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# View for my home page, login_required decorator prevents rendering if user is not logged in, will redirect to login filed if user is not logged in
@login_required(redirect_field_name='login')
def home(request):
    # If the user does a POST method, do the following action
    if request.method == 'POST':
        # creating a variable that is equal to request.POST which is the text content, and request.FILES which is the picture
        form = OrganismForm(request.POST, request.FILES)
        # This line tells us what user is doing the POST
        form.instance.user = request.user
        # https://stackoverflow.com/a/62727319/14263621 --- solution for class based view user model without showing user to customer

        # built in django method --- if form is valid, save it. plural organism is everything from the model
        if form.is_valid():
            form.save()
            plural_organism = Organism.objects.all()
            # takes the request and renders the images page
            return render(request, 'natureShareApp/images.html', {'organism_images' : plural_organism})
    
    else:
        form = OrganismForm()
    return render(request, 'natureShareApp/home.html', {'form' :  form})

# https://www.geeksforgeeks.org/python-uploading-images-in-django/

@login_required(redirect_field_name='login')
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

    # https://stackoverflow.com/a/8595758/14263621
    def get_queryset(self):
        base_qs = super(OrganismUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class OrganismDelete(DeleteView):
    model = Organism
    success_url = '/organism_images'

    def get_queryset(self):
        base_qs = super(OrganismDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)

@login_required(redirect_field_name='login')
def user_organisms(request):
    organisms = Organism.objects.filter(user = request.user)
    return render(request, 'natureShareApp/user_organisms.html', {'organisms' : organisms})
    
    