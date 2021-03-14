from django import forms
from .import *
from .models import Property


City_choices=[('Lahore','Lahore'),
                ('Islamabad','Islamabad'),
                ('Karachi','Karachi'),
]
Area_choices=[('Marla','Marla'),
              ('Kanal','Kanal'),
            ]
Bedroom_choices=[('1','1'),
                 ('2','2'),
                 ('3','3'),
                 ('4','4'),
                 ('5','5'),
]
Bathroom_choices=[('1','1'),
                 ('2','2'),
                 ('3','3'),
                 ('4','4'),
                 ('5','5'),
]
Categorie_choices=[('House','House'),
                    ('Flat','Flat'),
                    ('Farm','Farm'),
]
class PropertyForm(forms.ModelForm):
    class meta:
        model=Property
        fields=['Citie','Picture','Bathrooms','Bedrooms','Categorie','Area']

class SearchForm(forms.Form):
    City=forms.ChoiceField(choices=City_choices)
    Area=forms.ChoiceField(choices=Area_choices)
    Categorie=forms.ChoiceField(choices=Categorie_choices)
    Bedrooms=forms.ChoiceField(choices=Bedroom_choices)
    Bathrooms=forms.ChoiceField(choices=Bathroom_choices)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000)
    sender = forms.EmailField()

class SubscribeForm(forms.Form):
    Email=forms.EmailField()
    