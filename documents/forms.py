from django.db.models import fields
from django.forms import ModelForm, RadioSelect
from django.forms import widgets
from django.forms.widgets import HiddenInput

from .models import *

class MainInfoDocsForm(ModelForm):
    class Meta:
        model = MainInfoDocs
        fields = ('you_are', 'partners_value', 'artist_name', 'artist_fio', 'phone_number', 'email', 'socials', 'cover', 'num_songs', 'user',)
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

class OrgInfoIprfForm(ModelForm):
    class Meta:
        model = OrgInfoIprf
        fields = ('fio', 'ogrnip', 'inn', 'bank', 'r_s', 'bik', 'inn_bank', 'k_s', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'fio': 'Полностью',
            'bank': 'Можно найти в личном кабинете приложения любого банка.',
            'r_s': 'Можно найти в личном кабинете приложения любого банка.',
            'bik': 'Можно найти в личном кабинете приложения любого банка.',
            'inn_bank': 'Можно найти в личном кабинете приложения любого банка.', 
            'k_s': 'Можно найти в личном кабинете приложения любого банка.',
        }

class OrgInfoIpinForm(ModelForm):
    class Meta:
        model = OrgInfoIpin
        fields = ('fio', 'citizen', 'id_number', 'bank', 'r_s', 'bik', 'inn_bank', 'k_s', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'fio': 'Полностью',
            'id_number': 'Если применимо.',
            'bank': 'Можно найти в личном кабинете приложения любого банка.',
            'r_s': 'Можно найти в личном кабинете приложения любого банка.',
            'bik': 'Можно найти в личном кабинете приложения любого банка.',
            'inn_bank': 'Можно найти в личном кабинете приложения любого банка.', 
            'k_s': 'Можно найти в личном кабинете приложения любого банка.',
        }

class OrgInfoSamForm(ModelForm):
    class Meta:
        model = OrgInfoSam
        fields = ('fio', 'birthday', 'series_num', 'who_issued', 'when_issued', 'code_pod', 'birth_place', 'reg', 'bank', 'r_s', 'bik', 'inn_bank', 'k_s', 'inn', 'snils', 'skan_passport', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'fio': 'Полностью',
            'bank': 'Можно найти в личном кабинете приложения любого банка.',
            'r_s': 'Можно найти в личном кабинете приложения любого банка.',
            'bik': 'Можно найти в личном кабинете приложения любого банка.',
            'inn_bank': 'Можно найти в личном кабинете приложения любого банка.', 
            'k_s': 'Можно найти в личном кабинете приложения любого банка.',
            'skan_passport': 'Скан или фото. Первая страница и регистрация.',
        }

class OrgInfoOooForm(ModelForm):
    class Meta:
        model = OrgInfoOoo
        fields = ('name', 'fio_gen_dir', 'ogrn', 'inn', 'kpp', 'yur_address', 'fact_address', 'bank', 'r_s', 'bik', 'inn_bank', 'k_s', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'name': 'Полностью',
            'fio_gen_dir': 'Полностью',
        }

class AudioDocsForm(ModelForm):
    class Meta:
        model = AudioDocs
        fields = ('songers', 'song_title', 'album_title', 'words_author', 'music_author', 'phon_maker', 'timing', 'release_year', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'songers':'Написать имя исполнителя в том виде, в каком оно будет отражено на площадках. Если в песне несколько основных исполнителей, просьба заполнить всех основных исполнителей через запятую. Пример: "Джиган, Тимати, Егор Крид"',
            'song_title': 'Если в песне присутствует артист на фите, просьба ответить в формате: "_________ (feat. _______)". Пример: МИШКА (feat. KATERINA).',
            'words_author': 'ФИО Автора слов',
            'music_author': 'ФИО Автора музыки',
            'phon_maker': 'ФИО Изготовителя фонограммы',
            'timing': 'Напишите хронометраж песни в формате: 03:12',
        }

class VideoDocsForm(ModelForm):
    class Meta:
        model = VideoDocs
        fields = ('songers', 'video_title', 'words_author', 'music_author', 'phon_maker', 'director', 'timing', 'release_year', 'production_country', 'user',)
        widgets = {
            'user': HiddenInput,
        }
        help_texts = {
            'songers':'Написать имя исполнителя в том виде, в каком оно будет отражено на площадках. Если в песне несколько основных исполнителей, просьба заполнить всех основных исполнителей через запятую. Пример: "Джиган, Тимати, Егор Крид"',
            'video_title': 'Если в песне присутствует артист на фите, просьба ответить в формате: "_________ (feat. _______)". Пример: МИШКА (feat. KATERINA).',
            'words_author': 'ФИО Автора слов',
            'music_author': 'ФИО Автора музыки',
            'phon_maker': 'ФИО Изготовителя фонограммы',
            'director': 'ФИО Режиссёр',
            'timing': 'Напишите хронометраж песни в формате: 03:12',
        }

class LicenceForm(ModelForm):
    class Meta:
        model = Licence
        fields = ('music_author', 'words_author', 'phon_maker', 'user', )
        widgets = {
            'music_author': RadioSelect, 
            'words_author': RadioSelect, 
            'phon_maker': RadioSelect,
            'user': HiddenInput,
        }

class MusicAuthorForm(ModelForm):
    class Meta:
        model = MusicAuthor
        fields = ('fio', 'birthday', 'citizen', 'passport', 'birth_place', 'reg', 'author_email', 'fin_conditions', 'number', 'user', )
        widgets = {
            'user': HiddenInput,
            'number': HiddenInput,
        }
        help_texts = {
            'fio': 'Полностью',
            'fin_conditions': 'Опишите на каких условиях вы работаете с автором музыки. Пример: Он получил фиксированный платёж в размере 6000 тысяч рублей // Мы договорились работать на роялти 50 на 50 // Отдал права бесплатно // Договорились за упоминание в соцсетях.',
        }


class WordsAuthorForm(ModelForm):
    class Meta:
        model = WordsAuthor
        fields = ('fio', 'birthday', 'citizen', 'passport', 'birth_place', 'reg', 'author_email', 'fin_conditions', 'number', 'user', )
        widgets = {
            'user': HiddenInput,
            'number': HiddenInput,
        }
        help_texts = {
            'fio': 'Полностью',
            'fin_conditions': 'Опишите на каких условиях вы работаете с автором текста. Пример: Он получил фиксированный платёж в размере 6000 тысяч рублей // Мы договорились работать на роялти 50 на 50 // Отдал права бесплатно // Договорились за упоминание в соцсетях.',
        }

class OthersForm(ModelForm):
    class Meta:
        model = Others
        fields = ('creative_name', 'songs', 'fio', 'birthday', 'citizen', 'passport', 'birth_place', 'reg', 'fin_conditions', 'number', 'user')
        widgets = {
            'user': HiddenInput,
            'number': HiddenInput,
        }
        help_texts = {
            'id_number': 'Если применимо',
            'fin_conditions': 'Опишите на каких условиях вы работаете с автором текста. Пример: Он получил фиксированный платёж в размере 6000 тысяч рублей // Мы договорились работать на роялти 50 на 50 // Отдал права бесплатно // Договорились за упоминание в соцсетях.',
        }

class PhonMakerForm(ModelForm):
    class Meta:
        model = PhonMaker
        fields = ('fio', 'birthday', 'citizen', 'passport', 'birth_place', 'reg', 'author_email', 'fin_conditions', 'number', 'user', )
        widgets = {
            'user': HiddenInput,
            'number': HiddenInput,
        }
        help_texts = {
            'fio': 'Полностью',
            'fin_conditions': 'Опишите на каких условиях вы работаете с автором текста. Пример: Он получил фиксированный платёж в размере 6000 тысяч рублей // Мы договорились работать на роялти 50 на 50 // Отдал права бесплатно // Договорились за упоминание в соцсетях.',
        }

