from django.db import models
from django.contrib.auth.models import User

class MainInfo(models.Model):
    bool_choices = [
        ('NO', 'Нет'),
        ('YES', 'Да'),
    ]
    content_choices = [
        ('SINGLE', 'Сингл'),
        ('ALBUM', 'Альбом'),
        ('CLIP', 'Видеоклип'),
    ]
    integer_choices = [(i, i) for i in range(1, 101)]

    name = models.CharField(max_length=150, verbose_name='Имя артиста')
    phone_number = models.CharField(max_length=10, verbose_name='Телефон')
    email = models.EmailField(verbose_name='E-mail')
    is_update_photo = models.CharField(max_length=4, choices=bool_choices, default='NO', verbose_name='Необходимо ли обновить/добавить фото в карточках артиста на площадках?')
    photo_link = models.URLField(verbose_name='Ссылка на скачивание фото', null=True, blank=True)
    photo = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Прикрепить фото', blank=True, null=True)
    content_type = models.CharField(max_length=9, choices=content_choices, verbose_name='Тип релиза', default='SINGLE')
    cover = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Обложка (jpg 3000x3000)', blank=True, null=True)
    cover_psd = models.FileField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Обложка в слоях (PSD)', blank=True, null=True)
    num_songs = models.IntegerField(choices=integer_choices, null=True, default=1, verbose_name='Количество песен для отправки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Audio(models.Model):
    genre_choices = [
        ('NONE', 'Не выбрано'),
        ('BLUES','BLUES'), ('CHILDREN`S','CHILDREN`S'),
        ('CHRISTIAN','CHRISTIAN'), ('CLASSICAL','CLASSICAL'),
        ('COUNTRY','COUNTRY'), ('EDUCATIONAL','EDUCATIONAL'),
        ('ELECTRONIC','ELECTRONIC'), ('FOLK','FOLK'),
        ('HIP-HOP/RAP','HIP-HOP/RAP'), ('HOLIDAY','HOLIDAY'),
        ('JAZZ','JAZZ'), ('LATIN MUSIC','LATIN MUSIC'),
        ('METAL','METAL'), ('NEW AGE','NEW AGE'),
        ('POP','POP'), ('ALTERNATIVE','ALTERNATIVE'),
        ('R&B','R&B'), ('ROCK','ROCK'),
        ('PUNK','PUNK'), ('WORLD MUSIC','WORLD MUSIC'),
    ]
    exist_choices = [
        ('NONE', 'Не выбрано'),
        ('NO', 'Отсутствует'),
        ('YES', 'Присутствует'),
    ]
    
    songers = models.CharField(max_length=100, verbose_name='Исполнитель')
    song_title = models.CharField(max_length=100, verbose_name='Название песни')
    album_title = models.CharField(max_length=100, verbose_name='Название альбома', blank=True, null=True)
    feat = models.CharField(max_length=100, verbose_name='feat.', blank=True, null=True)
    genre = models.CharField(max_length=11, choices=genre_choices, default='NONE', verbose_name='Жанр')
    fio_songer = models.CharField(max_length=100, verbose_name='ФИО Исполнителя')
    words_author = models.CharField(max_length=100, verbose_name='Автор слов')
    music_author = models.CharField(max_length=100, verbose_name='Автор музыки')
    owner_citizenship = models.CharField(max_length=50, verbose_name='Гражданство изначального владельца авторских прав (артиста)')
    record_country = models.CharField(max_length=100, verbose_name='Страна записи')
    timing = models.CharField(max_length=5, verbose_name='Хронометраж')
    song_preview = models.CharField(max_length=15, verbose_name='Превью песни')
    lexis = models.CharField(max_length=15, choices=exist_choices, default='NONE', verbose_name='Ненормативная лексика в песне')
    audio = models.FileField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Аудио (WAV)', blank=True, null=True)
    audio_link = models.URLField(blank=True, null=True, verbose_name='Аудио (WAV)')
    clean_link = models.URLField(verbose_name='Clean version трека (WAV)')
    song_text = models.FileField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Текст песни', blank=True, null=True)
    release_year = models.CharField(max_length=4, verbose_name='Год выпуска')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Video(models.Model):
    exist_choices = [
        ('NONE', 'Не выбрано'),
        ('NO', 'Отсутствует'),
        ('YES', 'Присутствует'),
    ]

    songers = models.CharField(max_length=100, verbose_name='Исполнитель')
    video_title = models.CharField(max_length=100, verbose_name='Название видео')
    feat = models.CharField(max_length=100, verbose_name='feat.', blank=True, null=True)
    words_author = models.CharField(max_length=100, verbose_name='Автор слов')
    music_author = models.CharField(max_length=100, verbose_name='Автор музыки')
    lexis = models.CharField(max_length=15, choices=exist_choices, default='NONE', verbose_name='Ненормативная лексика в песне')
    director = models.CharField(max_length=100, verbose_name='Режиссер')
    timing = models.CharField(max_length=5, verbose_name='Хронометраж')
    release_year = models.CharField(max_length=4, verbose_name='Год выпуска')
    video_link = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')
    video_preview = models.ImageField(upload_to = 'uploads/%Y/%m/%d/', verbose_name='Превью клипа', blank=True, null=True)
    production_country = models.CharField(max_length=100, verbose_name='Страна производства')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
