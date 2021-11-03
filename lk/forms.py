from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import HiddenInput, Input, Textarea
from .models import *


class LkForm(ModelForm):
    class Meta:
        model = Lk
        fields = '__all__'
        widgets = {
            'birthday': Input(attrs={'type': 'date'}),
            'user': HiddenInput,
        }
