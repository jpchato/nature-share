import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q

from .forms import OrganismForm
from .models import Organism

logger = logging.getLogger(__name__)


def home(request):
    """Display the organism gallery and handle new organism creation for authenticated users."""
    # Get all organisms for the gallery
    organisms = Organism.objects.all().order_by('-date')
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrganismForm(request.POST, request.FILES)
            if form.is_valid():
                organism = form.save(commit=False)
                organism.user = request.user
                organism.save()
                messages.success(request, 'Organism created successfully.')
                logger.info('Organism %s created by user %s', organism.name, request.user.username)
                return redirect('organism_images')
            messages.error(request, 'Please correct the errors below.')
        else:
            form = OrganismForm()
    else:
        form = None

    return render(request, 'natureShareApp/home.html', {'form': form, 'organism_images': organisms})


@login_required(login_url='login')
def display_images(request):
    """Render the list of uploaded organism images."""
    organisms = Organism.objects.all().order_by('-date')
    return render(request, 'natureShareApp/images.html', {'organism_images': organisms})


class OrganismDetailView(DetailView):
    """Show full details for a single organism."""
    model = Organism

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GOOGLE_API_KEY'] = settings.GOOGLE_API_KEY
        return context


class SearchResultsView(ListView):
    """Search all organisms by ecosystem or name."""
    model = Organism
    template_name = 'natureShareApp/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if not query:
            return Organism.objects.none()

        return Organism.objects.filter(
            Q(ecosystem__icontains=query) | Q(name__icontains=query)
        )


class UserSearchResultsView(LoginRequiredMixin, ListView):
    """Search the current user's organisms."""
    model = Organism
    template_name = 'natureShareApp/user_search_results.html'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if not query:
            return Organism.objects.none()

        return Organism.objects.filter(user=self.request.user).filter(
            Q(ecosystem__icontains=query) | Q(name__icontains=query)
        )


class OrganismUpdate(LoginRequiredMixin, UpdateView):
    """Allow a user to edit their own organism record."""
    model = Organism
    fields = ['picture', 'name', 'edibility', 'ecosystem', 'weather', 'date', 'location']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('organism_images')
    login_url = 'login'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class OrganismDelete(LoginRequiredMixin, DeleteView):
    """Allow a user to delete their own organism record."""
    model = Organism
    success_url = reverse_lazy('organism_images')
    login_url = 'login'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


@login_required(login_url='login')
def user_organisms(request):
    """Show the requesting user's own organisms."""
    organisms = Organism.objects.filter(user=request.user).order_by('-date')
    return render(request, 'natureShareApp/user_organisms.html', {'organisms': organisms})


def about(request):
    """Render the about page."""
    return render(request, 'natureShareApp/about.html') 
