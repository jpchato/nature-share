from django import forms
from .models import Organism

# Date picker widget
class DateInput(forms.DateInput):
    input_type = 'date'

class OrganismForm(forms.ModelForm):
    """Form for creating or editing organism records."""

    class Meta:
        model = Organism
        fields = ['picture', 'name', 'edibility', 'ecosystem', 'weather', 'date', 'location']
        widgets = {
            'date': DateInput(),
        }