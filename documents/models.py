from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField

class MainInfoDocs(models.Model):
    org_type_choices = [
        ('IPRF', 'ИП РФ'),
        ('IPIN', 'ИП Иностранный'),
        ('SAM', 'Самозанятый'), 
        ('OOO', 'ООО'),
    ]
    integer_choices = [(i, i) for i in range(1, 21)]

    you_are = models.CharField(max_length=20, choices=org_type_choices, verbose_name='Вы являетесь', default='IPRF')
    partners_value = models.IntegerField(choices=integer_choices, null=True, default=1, verbose_name='Количество участников')
    artist_name = models.CharField(max_length=100, verbose_name='Имя артиста')
    artist_fio = models.CharField(max_length=100, verbose_name='ФИО Артиста')
    phone_number = models.CharField(max_length=10, verbose_name='Телефон для связи')
    email = models.EmailField(verbose_name='E-mail')
    socials = models.CharField(max_length=500, verbose_name='Социальные сети')
    cover = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Обложка (jpg 3000x3000)', blank=True, null=True)
    num_songs = models.IntegerField(choices=integer_choices, null=True, default=1, verbose_name='Количество песен для отправки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class OrgInfoIprf(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    ogrnip = models.CharField(max_length=100, verbose_name='ОГРНИП')
    inn = models.CharField(max_length=100, verbose_name='ИНН')
    bank = models.CharField(max_length=50, verbose_name='Банк')
    r_s = models.CharField(max_length=100, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=100, verbose_name='БИК')
    inn_bank = models.CharField(max_length=100, verbose_name='ИНН Банка')
    k_s = models.CharField(max_length=100, verbose_name='Корреспондентский счет')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class OrgInfoIpin(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    citizen = models.CharField(max_length=100, verbose_name='Гражданство')
    id_number = models.CharField(max_length=100, verbose_name='Идентификационный номер')
    bank = models.CharField(max_length=50, verbose_name='Банк')
    r_s = models.CharField(max_length=100, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=100, verbose_name='БИК')
    inn_bank = models.CharField(max_length=100, verbose_name='ИНН Банка')
    k_s = models.CharField(max_length=100, verbose_name='Корреспондентский счет')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class OrgInfoSam(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта')
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан')
    when_issued = models.DateField(verbose_name='Дата выдачи')
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения')
    birth_place = models.CharField(max_length=2024, verbose_name='Место рождения')
    reg = models.CharField(max_length=2024, verbose_name='Регистрация')
    bank = models.CharField(max_length=50, verbose_name='Банк')
    r_s = models.CharField(max_length=100, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=100, verbose_name='БИК')
    inn_bank = models.CharField(max_length=100, verbose_name='ИНН Банка')
    k_s = models.CharField(max_length=100, verbose_name='Корреспондентский счет')
    inn = models.CharField(max_length=100, verbose_name='ИНН')
    snils = models.CharField(max_length=100, verbose_name='СНИЛС')
    skan_passport = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Скан паспорта')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class OrgInfoOoo(models.Model):
    name = CharField(max_length=100, verbose_name='Наименование')
    fio_gen_dir = CharField(max_length=100, verbose_name='ФИО Генерального директора')
    ogrn = models.CharField(max_length=100, verbose_name='ОГРН')
    inn = models.CharField(max_length=100, verbose_name='ИНН')
    kpp = models.CharField(max_length=100, verbose_name='КПП')
    yur_address = models.CharField(max_length=2024, verbose_name='Юридический адрес')
    fact_address = models.CharField(max_length=2024, verbose_name='Фактический адрес')
    bank = models.CharField(max_length=50, verbose_name='Банк')
    r_s = models.CharField(max_length=100, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=100, verbose_name='БИК')
    inn_bank = models.CharField(max_length=100, verbose_name='ИНН Банка')
    k_s = models.CharField(max_length=100, verbose_name='Корреспондентский счет')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class AudioDocs(models.Model):
    songers = models.CharField(max_length=100, verbose_name='Исполнитель')
    song_title = models.CharField(max_length=100, verbose_name='Название песни')
    album_title = models.CharField(max_length=100, verbose_name='Название альбома', blank=True, null=True)
    words_author = models.CharField(max_length=100, verbose_name='Автор слов')
    music_author = models.CharField(max_length=100, verbose_name='Автор музыки')
    phon_maker = models.CharField(max_length=100, verbose_name='Изготовитель фонограммы')
    timing = models.CharField(max_length=5, verbose_name='Хронометраж')
    release_year = models.CharField(max_length=4, verbose_name='Год выпуска')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class VideoDocs(models.Model):
    songers = models.CharField(max_length=100, verbose_name='Исполнитель')
    video_title = models.CharField(max_length=100, verbose_name='Название видео')
    words_author = models.CharField(max_length=100, verbose_name='Автор слов')
    music_author = models.CharField(max_length=100, verbose_name='Автор музыки')
    phon_maker = models.CharField(max_length=100, verbose_name='Изготовитель фонограммы')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    timing = models.CharField(max_length=5, verbose_name='Хронометраж')
    release_year = models.CharField(max_length=4, verbose_name='Год выпуска')
    production_country = models.CharField(max_length=100, verbose_name='Страна производства')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Licence(models.Model):
    licence_choice = [
        ('LIC', 'Лицензия'),
        ('ALI', 'Отчуждение'),
    ]

    music_author = models.CharField(max_length=15, choices=licence_choice, verbose_name='Автор музыки передает вам права по лицензии или происходит отчуждение прав?', default='LIC')
    words_author = models.CharField(max_length=15, choices=licence_choice, verbose_name='Автор текста передает вам права по лицензии или происходит отчуждение прав?', default='LIC')
    phon_maker = models.CharField(max_length=15, choices=licence_choice, verbose_name='Изготовитель фонограммы передает вам права по лицензии или происходит отчуждение прав?', default='LIC')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class MusicCitizen(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта')
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан')
    when_issued = models.DateField(verbose_name='Дата выдачи')
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения')
    birth_place = models.CharField(max_length=2024, verbose_name='Место рождения')
    reg = models.CharField(max_length=2024, verbose_name='Регистрация')
    author_email = models.EmailField(verbose_name='Электронная почта автора')
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с автором музыки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class MusicForeign(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    citizen = models.CharField(max_length=100, verbose_name='Гражданство')
    passport = models.CharField(max_length=2024, verbose_name='Паспортные данные')
    author_email = models.EmailField(verbose_name='Электронная почта автора')
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с автором музыки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class WordsCitizen(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта')
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан')
    when_issued = models.DateField(verbose_name='Дата выдачи')
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения')
    birth_place = models.CharField(max_length=2024, verbose_name='Место рождения')
    reg = models.CharField(max_length=2024, verbose_name='Регистрация')
    author_email = models.EmailField(verbose_name='Электронная почта автора')
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с автором музыки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class WordsForeign(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    citizen = models.CharField(max_length=100, verbose_name='Гражданство')
    passport = models.CharField(max_length=2024, verbose_name='Паспортные данные')
    author_email = models.EmailField(verbose_name='Электронная почта автора')
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с автором музыки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)