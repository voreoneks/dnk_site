import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from transliterate import translit


def update_filename(instance, filename):
    path = 'uploads/' + str(instance.user)
    filename_ = translit(filename, language_code='ru', reversed=True)
    return os.path.join(path, filename_)

class MainInfoDocs(models.Model):
    release_type_choices = {
        ('SINGLE', 'Сингл'),
        ('ALBUM', 'Альбом / ЕР'),
        ('CLIP', 'Видеоклип'),
    }
    org_type_choices = [
        ('IPRF', 'ИП РФ'),
        ('IPIN', 'Иностранная организация или ИП'),
        ('SAM', 'Самозанятый'), 
        ('OOO', 'ООО'),
    ]
    integer_choices = [(i, i) for i in range(1, 21)]

    you_are = models.CharField(max_length=20, choices=org_type_choices, verbose_name='Вы являетесь', default='IPRF')
    partners_value = models.IntegerField(choices=integer_choices, null=True, default=1, verbose_name='Количество участников')
    artist_name = models.CharField(max_length=100, verbose_name='Имя артиста')
    artist_fio = models.CharField(max_length=100, verbose_name='ФИО Артиста')
    phone_number = models.CharField(max_length=12, verbose_name='Телефон для связи')
    email = models.EmailField(verbose_name='E-mail')
    socials = models.CharField(max_length=500, verbose_name='Социальные сети', blank=True, null=True)
    cover = models.ImageField(upload_to = update_filename, verbose_name='Обложка (jpg 3000x3000)', blank=True, null=True)
    release_type = models.CharField(max_length=15, choices=release_type_choices, verbose_name='Тип релиза', null=True, default='SINGLE')
    num_songs = models.IntegerField(choices=integer_choices, null=True, default=1, verbose_name='Количество песен для отправки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class OrgInfoIprf(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    ogrnip = models.CharField(max_length=100, verbose_name='ОГРНИП')
    inn = models.CharField(max_length=100, verbose_name='ИНН')
    bank = models.CharField(max_length=50, verbose_name='Наименование банка')
    r_s = models.CharField(max_length=100, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=100, verbose_name='БИК')
    inn_bank = models.CharField(max_length=100, verbose_name='ИНН Банка')
    k_s = models.CharField(max_length=100, verbose_name='Корреспондентский счет')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class OrgInfoIpin(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    citizen = models.CharField(max_length=100, verbose_name='Гражданство')
    id_number = models.CharField(max_length=100, verbose_name='Идентификационный номер')
    bank = models.CharField(max_length=50, verbose_name='Наименование банка')
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
    reg = models.CharField(max_length=2024, verbose_name='Адрес регистрации')
    inn = models.CharField(max_length=100, verbose_name='ИНН', blank=True, null=True)
    snils = models.CharField(max_length=100, verbose_name='СНИЛС', blank=True, null=True)
    bank = models.CharField(max_length=50, verbose_name='Наименование банка')
    r_s = models.CharField(max_length=100, verbose_name='Расчетный счет')
    bik = models.CharField(max_length=100, verbose_name='БИК')
    inn_bank = models.CharField(max_length=100, verbose_name='ИНН Банка')
    k_s = models.CharField(max_length=100, verbose_name='Корреспондентский счет')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class OrgInfoOoo(models.Model):
    name = CharField(max_length=100, verbose_name='Наименование')
    fio_gen_dir = CharField(max_length=100, verbose_name='ФИО Генерального директора')
    ogrn = models.CharField(max_length=100, verbose_name='ОГРН')
    inn = models.CharField(max_length=100, verbose_name='ИНН')
    kpp = models.CharField(max_length=100, verbose_name='КПП')
    yur_address = models.CharField(max_length=2024, verbose_name='Юридический адрес')
    fact_address = models.CharField(max_length=2024, verbose_name='Фактический адрес')
    bank = models.CharField(max_length=50, verbose_name='Наименование банка')
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


class MusicAuthor(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    citizen = models.CharField(max_length=100, verbose_name='Гражданство')
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта', null=True)
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан', null=True)
    when_issued = models.DateField(verbose_name='Дата выдачи', null=True)
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения', null=True)
    reg = models.CharField(max_length=2024, verbose_name='Адрес регистрации', null=True)
    author_email = models.EmailField(verbose_name='Электронная почта автора музыки')
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с автором музыки')
    number = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class WordsAuthor(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
    birthday = models.DateField(verbose_name='Дата рождения')
    citizen = models.CharField(max_length=100, verbose_name='Гражданство')
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта', null=True)
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан', null=True)
    when_issued = models.DateField(verbose_name='Дата выдачи', null=True)
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения', null=True)
    reg = models.CharField(max_length=2024, verbose_name='Адрес регистрации')
    author_email = models.EmailField(verbose_name='Электронная почта автора слов')
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с автором слов')
    number = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Others(models.Model):
    creative_name = models.CharField(max_length=100, verbose_name='Творческий псевдоним', blank=True, null=True)
    songs = models.CharField(max_length=500, verbose_name='Песня, в которой этот исполнитель учавствует', blank=True, null=True)
    fio = models.CharField(max_length=100, verbose_name='ФИО', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    citizen = models.CharField(max_length=100, verbose_name='Гражданство', blank=True, null=True)
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта', null=True, blank=True)
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан', null=True, blank=True)
    when_issued = models.DateField(verbose_name='Дата выдачи', null=True, blank=True)
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения', null=True, blank=True)
    reg = models.CharField(max_length=2024, verbose_name='Адрес регистрации', blank=True, null=True)
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с соисполнителем', blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class PhonMaker(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО', blank=True, null=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    citizen = models.CharField(max_length=100, verbose_name='Гражданство', blank=True, null=True)
    series_num = models.CharField(max_length=100, verbose_name='Серия и номер паспорта', null=True)
    who_issued = models.CharField(max_length=500, verbose_name='Кем выдан', null=True)
    when_issued = models.DateField(verbose_name='Дата выдачи', null=True)
    code_pod = models.CharField(max_length=100, verbose_name='Код подразделения', null=True)
    reg = models.CharField(max_length=2024, verbose_name='Адрес регистрации', blank=True, null=True)
    author_email = models.EmailField(verbose_name='Электронная почта изготовителя фонограммы', blank=True, null=True)
    fin_conditions = models.CharField(max_length=2024, verbose_name='Финансовые условия с изготовителем фонограммы', blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
