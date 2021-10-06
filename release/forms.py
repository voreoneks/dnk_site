from django import forms
from django.db.models import fields
from django.forms import ModelForm, RadioSelect
from .models import *

class MainInfoForm(ModelForm):
    class Meta:
        model = MainInfo
        exclude = ['user',]
        widgets = {
            'is_update_photo': RadioSelect,
            'content_type': RadioSelect,
        }
    
