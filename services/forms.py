from django import forms
from .models import VirusC

class VirusCForm(forms.ModelForm):
    class Meta:
        model = VirusC
        fields = '__all__'

    gender = forms.ChoiceField(
        choices=VirusC.gender_choices.items(),
        widget=forms.RadioSelect,
        help_text="Select the gender"
    )

    def __init__(self, *args, **kwargs):
        super(VirusCForm, self).__init__(*args, **kwargs)
        field_help_texts = {
            'age': 'Enter the Age in years',
            'alb': 'Enter the Albumin Level',
            'alp': 'Enter the Alkaline Phosphatase Level',
            'alt': 'Enter the Alanine Transaminase Level',
            'ast': 'Enter the Aspartame Transaminase Level',
            'bil': 'Enter the Bilirubin Level',
            'che': 'Enter the Cholinesterase Level',
            'chol': 'Enter the Cholesterol Level',
            'crea': 'Enter the Creatinine Level',
            'ggt': 'Enter the Gamma-Glutamyl Transferase Level',
            'prot': 'Enter the Protein Level',
        }
        for field_name, field in self.fields.items():
            field.help_text = field_help_texts.get(field_name, '')
        self.fields['gender'].label = 'Gender'
