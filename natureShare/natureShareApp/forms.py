from django import forms
from .models import *
from django.forms import ModelForm

# Date picker widget
class DateInput(forms.DateInput):
    input_type = 'date'

# https://stackoverflow.com/a/35968816/14263621
# This form is used for class based views in the views.py
class OrganismForm(forms.ModelForm):
    class Meta:
        # grabs our model
        model = Organism
        # all these fields will be rendered on the form, except user which we exclude
        fields = ['picture', 'name', 'edibility', 'ecosystem', 'weather', 'date', 'location', 'user']
        # excluding user prevents users from changing the user
        exclude = ['user']
        # date picker widget
        widgets  = {
            'date': DateInput()
        }