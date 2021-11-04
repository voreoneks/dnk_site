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
        help_texts = {
            'telegram': 'Укажите полную ссылку на аккаунт. Например: https://t.me/myaccount.',
            'vk': 'Укажите полную ссылку на аккаунт. Например: https://vk.com/myaccount.',
            'inst': 'Укажите полную ссылку на аккаунт. Например: https://www.instagram.com/myaccount.',
            'facebook': 'Укажите полную ссылку на аккаунт. Например: https://www.facebook.com/myaccount.',
            'youtube': 'Укажите полную ссылку на аккаунт. Например: https://www.youtube.com/user/myaccount.',
            'tiktok': 'Укажите полную ссылку на аккаунт. Например: https://www.tiktok.com/@tiktok.',
        }
