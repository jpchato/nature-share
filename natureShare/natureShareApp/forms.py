from django import forms
from .models import *
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

# https://stackoverflow.com/a/35968816/14263621

class OrganismForm(forms.ModelForm):
    class Meta:
        model = Organism
        fields = ['picture', 'name', 'edibility', 'ecosystem', 'weather', 'date', 'location', 'user']
        exclude = ['user']
        widgets  = {
            'date': DateInput()
        }