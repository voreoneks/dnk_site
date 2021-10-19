from django.forms import ModelForm, RadioSelect
from django.forms.widgets import HiddenInput

from .models import *

class MainInfoDocsForm(ModelForm):
    class Meta:
        model = MainInfoDocs
        fields = ('you_are', 'partners_value', 'artist_name', 'artist_fio', 'phone_number', 'email', 'socials', 'user',)
        widgets = {
            'you_are': RadioSelect,
            'user': HiddenInput,
        }
        help_texts = {
            'partners_value': 'Указать сольный артист или группа (количество участников)',
            'artist_name': 'Имя Артиста должно выглядеть так, как оно будет отражено на площадках',
            'artist_fio': 'Полностью',
            'email': 'Для отчётов и дальнейшей коммуникации',
        }
