from django import forms
from .models import *

class OrganismForm(forms.ModelForm):
    class Meta:
        model = Organism
        fields = ['picture', 'name', 'edibility', 'ecosystem', 'weather', 'date', 'location', 'user']
        exclude = ['user']