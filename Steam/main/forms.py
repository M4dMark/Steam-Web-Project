from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Hry

class add_form(ModelForm):
    class Meta:
        model = Hry
        fields = ('nazev', 'cena_v_eur', 'publisher_idpublisher', 'vyvojar_idvyvojar')

        labels = {
            'nazev': 'Nazev',
            'cena_v_eur': 'Cena v Eurech',
            'publisher_idpublisher': 'Publisher',
            'vyvojar_idvyvojar': 'Vyvojar'
        }

        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'cena_v_eur': forms.NumberInput(attrs={'class': 'form-control'}),
            'publisher_idpublisher': forms.NumberInput(attrs={'class': 'form-control'}),
            'vyvojar_idvyvojar': forms.NumberInput(attrs={'class': 'form-control'})
        }
        

class update_form(ModelForm):
    class Meta:
        model = Hry
        fields = ('nazev', 'cena_v_eur', 'trzby_v_eur', 'prodanych_kusu', 'publisher_idpublisher', 'vyvojar_idvyvojar')

        labels = {
            'nazev': 'Nazev',
            'cena_v_eur': 'Cena v Eurech',
            'trzby_v_eur': 'Trzby v Eurech',
            'prodanych_kusu': 'Prodanych kusu',
            'publisher_idpublisher': 'Publisher',
            'vyvojar_idvyvojar': 'Vyvojar'
        }

        widgets = {
            'nazev': forms.TextInput(attrs={'class': 'form-control'}),
            'cena_v_eur': forms.NumberInput(attrs={'class': 'form-control'}),
            'trzby_v_eur': forms.NumberInput(attrs={'class': 'form-control'}),
            'prodanych_kusu': forms.NumberInput(attrs={'class': 'form-control'}),
            'publisher_idpublisher': forms.NumberInput(attrs={'class': 'form-control'}),
            'vyvojar_idvyvojar': forms.NumberInput(attrs={'class': 'form-control'})
        }

