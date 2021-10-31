from django.db import models
from django.contrib.auth.models import User

class Lk(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя артиста', null=True, blank=True)
    fio = models.CharField(max_length=100, verbose_name='ФИО', null=True, blank=True)
    phone = models.CharField(max_length=12, verbose_name='Телефон', null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    passport = models.CharField(max_length=2048, verbose_name='Паспортные данные', null=True, blank=True)
    telegram = models.CharField(max_length=100, verbose_name='Telegram', null=True, blank=True)
    vk = models.CharField(max_length=100, verbose_name='VK', null=True, blank=True)
    inst = models.CharField(max_length=100, verbose_name='Instagram', null=True, blank=True)
    facebook = models.CharField(max_length=100, verbose_name='Facebook', null=True, blank=True)
    youtube = models.CharField(max_length=100, verbose_name='YouTube', null=True, blank=True)
    tiktok = models.CharField(max_length=100, verbose_name='TikTok', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
