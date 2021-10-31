from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import HiddenInput, Textarea
from .models import *


class LkForm(ModelForm):
    class Meta:
        model = Lk
        fields = '__all__'
        widgets = {
            'user': HiddenInput,
        }
