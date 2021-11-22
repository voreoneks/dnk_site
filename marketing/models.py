from django.db import models
from django.contrib.auth.models import User

class MainInfoMarketing(models.Model):
    songers = models.CharField(max_length=100, verbose_name='Исполнитель')
    release_title = models.CharField(max_length=100, verbose_name='Название релиза')
    vk = models.CharField(max_length=100, verbose_name='VK')
    inst = models.CharField(max_length=50, verbose_name='Instagram')
    facebook = models.CharField(max_length=100, verbose_name='Facebook', blank=True, null=True)
    youtube = models.CharField(max_length=100, verbose_name='YouTube', blank=True, null=True)
    tiktok = models.CharField(max_length=100, verbose_name='TikTok', blank=True, null=True)
    other = models.CharField(max_length=500, verbose_name='Другие социальные сети', blank=True, null=True)
    focus_track = models.CharField(max_length=100, verbose_name='Фокус-трек (если у вас альбом или EP)', blank=True, null=True)
    photo_link = models.URLField(verbose_name='Cсылка на качественные фотографии, которые будут отправлены редакторам площадок')
    press_release = models.TextField(verbose_name='Пресс-релиз об артисте (основные музыкальные награды и достижения), пару слов о предстоящем релизе (идея, история создания)')
    pr = models.TextField(verbose_name='PR проработка релиза: информация о радиостанциях, печатных изданиях, онлайн СМИ с вашей стороны')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


