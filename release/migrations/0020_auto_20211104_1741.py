# Generated by Django 3.2.5 on 2021-11-04 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0019_alter_audio_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='clean_link',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Clean version трека (WAV)'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='timing',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex='/d{2}:/d{2}')], verbose_name='Хронометраж'),
        ),
    ]