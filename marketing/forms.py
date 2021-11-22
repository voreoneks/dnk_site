from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from .models import MainInfoMarketing


class MainInfoMarketingForm(ModelForm):
    class Meta:
        model = MainInfoMarketing
        fields = '__all__'
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'inst': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.instagram.com/myaccount.',
            'facebook': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.facebook.com/myaccount.',
            'youtube': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.youtube.com/user/myaccount.',
            'tiktok': 'Укажите полную ссылку на страницу аккаунта. Например: https://www.tiktok.com/@tiktok.',
            'other': 'Укажите полные ссылки на страницы аккаунтов. Например: https://t.me/myaccount.',
            'vk': 'Полная ссылка на личную страницу и на официальное сообщество. Например: https://vk.com/myaccount.',

        }


