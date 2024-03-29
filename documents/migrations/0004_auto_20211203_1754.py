# Generated by Django 3.2.5 on 2021-12-03 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20211124_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiodocs',
            name='timing',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex='[0-9]{2}:[0-9]{2}')], verbose_name='Хронометраж'),
        ),
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('CLIP', 'Видеоклип'), ('SINGLE', 'Сингл'), ('ALBUM', 'Альбом / ЕР')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]
