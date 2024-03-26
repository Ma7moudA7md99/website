from django import forms
from .models import VirusC, LungCancer

class VirusCForm(forms.ModelForm):
    class Meta:
        model = VirusC
        fields = '__all__'

    gender = forms.ChoiceField(
        choices=VirusC.gender_choices.items(),
        widget=forms.RadioSelect
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


class LungCancerForm(forms.ModelForm):
    class Meta:
        model = LungCancer
        fields = ['SMOKING', 'YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE', 
                  'CHRONIC_DISEASE', 'FATIGUE', 'ALLERGY', 'WHEEZING', 
                  'ALCOHOL_CONSUMING', 'COUGHING', 'SHORTNESS_OF_BREATH', 
                  'SWALLOWING_DIFFICULTY', 'CHEST_PAIN', 'gender', 'age']

    def __init__(self, *args, **kwargs):
        super(LungCancerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'age':
                field.widget = forms.NumberInput(attrs={'type': 'number'})
            elif field_name == 'gender':
                field.widget = forms.RadioSelect(choices=((1, 'Male'), (0, 'Female')))
            else:
                field.widget = forms.RadioSelect(choices=((1, 'Yes'), (0, 'No')))