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
    
    # if the request method is not a post, the form will be equal to OrganismForm from our forms.py
    else:
        form = OrganismForm()
    # renders the home page with the form again --- essentially refreshing the page if it's not a POST
    return render(request, 'natureShareApp/home.html', {'form' :  form})

# https://www.geeksforgeeks.org/python-uploading-images-in-django/

# view for the page that displays all images --- decorator that requires login and redirects to login field if user is not logged in
@login_required(redirect_field_name='login')
def display_images(request):
    # if the request method is a get, all the organisms in my model are retrieved and displayed on our images.html page
    if request.method == 'GET':
        plural_organism = Organism.objects.all()
        # return render((request, 'natureShareApp/images.html', {'organism_images' : plural_organism}))
        return render(request, 'natureShareApp/images.html', {'organism_images' : plural_organism})

# Class based view that renders all the details of an organism on the organism_detail.html
class OrganismDetailView(generic.DetailView):
    model = Organism

# Class based view that allows users to search by ecosystem type and render a list view on search_result.html
class SearchResultsView(ListView):
    # Specifying the model
    model = Organism
    # Specifying the template to render our object_list
    template_name = 'natureShareApp/search_results.html'
    
    # Not sure --- I forgot to save the link from stack overflow
    def get_queryset(self):
        # Setting our query using Q that we imported
        query = self.request.GET.get('q')
        # our object list filetered to contain ecosystem
        object_list = Organism.objects.filter(Q(ecosystem__icontains=query))
        return object_list

class UserSearchResultsView(ListView):
    # Specifying the model
    model = Organism
    # Specifying the template to render our object_list
    template_name = 'natureShareApp/user_search_results.html'
    
    # Not sure --- I forgot to save the link from stack overflow
    def get_queryset(self):
        # Setting our query using Q that we imported
        query = self.request.GET.get('q')
        # our object list filetered to contain ecosystem
        object_list = Organism.objects.filter(Q(user__icontains=query))
        return object_list

# Class based view that allows users to edit their own content
class OrganismUpdate(UpdateView):
    # setting the model equal to our organism
    model = Organism
    # specifying the fields to be rendered
    fields = ['name', 'edibility', 'ecosystem', 'weather', 'date', 'location']
    # Not sure why we need this
    template_name_suffix = '_update_form'
    # url to go to if successful
    success_url ="/organism_images"

    # https://stackoverflow.com/a/8595758/14263621
    # This function allows users to edit only their own organisms and not others organisms
    def get_queryset(self):
        # setting the base querys
        # super is a built in python function
        base_qs = super(OrganismUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

# Class based view that allows users to delete their own content
class OrganismDelete(DeleteView):
    # sets the model equal to organism
    model = Organism
    # renders the organism_images url when successfully deleting an organism
    success_url = '/organism_images'

    # Allows users to edit their own organisms and not others organisms
    def get_queryset(self):
        base_qs = super(OrganismDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)

# function based view that allows users to see their own organisms, redirects to login field if user is not logged in
@login_required(redirect_field_name='login')
def user_organisms(request):
    # filtering organisms by the requesting user
    organisms = Organism.objects.filter(user = request.user)
    # rendering the users organisms to user_organisms.html
    return render(request, 'natureShareApp/user_organisms.html', {'organisms' : organisms})
    
    