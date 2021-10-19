from django.db import models
from django.contrib.auth.models import User

class MainInfoDocs(models.Model):
    org_type_choices = [
        ('IPRF', 'ИП РФ'),
        ('IPIN', 'ИП Иностранный'),
        ('SAM', 'Самозанятый'), 
        ('OOO', 'ООО'),
    ]
    integer_choices = [(i, i) for i in range(1, 31)]

    you_are = models.CharField(max_length=20, choices=org_type_choices, verbose_name='Вы являетесь', default='IPRF')
    partners_value = models.IntegerField(choices=integer_choices, null=True, default=1, verbose_name='Количество участников')
    artist_name = models.CharField(max_length=100, verbose_name='Имя артиста')
    artist_fio = models.CharField(max_length=100, verbose_name='ФИО Артиста')
    phone_number = models.CharField(max_length=10, verbose_name='Телефон для связи')
    email = models.EmailField(verbose_name='E-mail')
    socials = models.CharField(max_length=500, verbose_name='Социальные сети')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class OrgInfoIprf(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    ogrnip = models.IntegerField(max_length=15, verbose_name='ОГРНИП')
    inn = models.IntegerField(max_length=12, verbose_name='ИНН')
    bank = models.CharField(max_length=50, verbose_name='Банк')
    r_s = models.IntegerField(max_length=20, verbose_name='Расчетный счет')
    bik = models.IntegerField(max_length=9, verbose_name='БИК')
    inn_bank = models.IntegerField(max_length=10, verbose_name='ИНН Банка')
    k_s = models.IntegerField(max_length=20, verbose_name='Корреспондентский счет')