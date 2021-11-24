# Generated by Django 3.2.5 on 2021-11-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_maininfodocs_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('CLIP', 'Видеоклип'), ('ALBUM', 'Альбом / ЕР'), ('SINGLE', 'Сингл')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
        migrations.AlterField(
            model_name='others',
            name='code_pod',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Код подразделения'),
        ),
        migrations.AlterField(
            model_name='others',
            name='series_num',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Серия и номер паспорта'),
        ),
        migrations.AlterField(
            model_name='others',
            name='when_issued',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='others',
            name='who_issued',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Кем выдан'),
        ),
    ]