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
        field_placeholders = {
            'age': 'Age in years',
            'alb': 'Albumin Level',
            'alp': 'Alkaline Phosphatase Level',
            'alt': 'Alanine Transaminase Level',
            'ast': 'Aspartame Transaminase Level',
            'bil': 'Bilirubin Level',
            'che': 'Cholinesterase Level',
            'chol': 'Cholesterol Level',
            'crea': 'Creatinine Level',
            'ggt': 'Gamma-Glutamyl Transferase Level',
            'prot': 'Protein Level',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field_placeholders.get(field_name, '')})
        self.fields['gender'].label = 'Gender'
