"""Forms for the Garbage Report and Contact models."""
from django import forms
from .models import GarbageReport, Contact

class GarbageReportForm(forms.ModelForm):
    WASTE_TYPE_CHOICES = [
        ('organic', 'Organic'),
        ('inorganic', 'Inorganic'),
        ('mixed', 'Mixed'),
        ('household', 'Household'),
    ]
    
    wastetype = forms.MultipleChoiceField(
        choices=WASTE_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    class Meta:
        model = GarbageReport
        fields = ['name', 'mobile', 'email', 'wastetype', 'location', 'locationdescription', 'file']
    
    def clean_wastetype(self):
        # Convert selected waste types to comma-separated string
        waste_types = self.cleaned_data.get('wastetype')
        return ','.join(waste_types) + ','

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fname', 'lname', 'contactEmail', 'contactPhone', 'comment']
