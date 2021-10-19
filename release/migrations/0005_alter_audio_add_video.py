# Generated by Django 3.2.5 on 2021-10-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0004_alter_audio_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='add_video',
            field=models.CharField(choices=[('NO', 'Нет'), ('YES', 'Да')], default='NO', max_length=3, verbose_name='Добавить видеоклип'),
        ),
    ]