# Generated by Django 3.2.5 on 2021-11-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lk',
            name='passport',
        ),
        migrations.AddField(
            model_name='lk',
            name='code_pod',
            field=models.CharField(max_length=100, null=True, verbose_name='Код подразделения'),
        ),
        migrations.AddField(
            model_name='lk',
            name='reg',
            field=models.CharField(max_length=2024, null=True, verbose_name='Регистрация'),
        ),
        migrations.AddField(
            model_name='lk',
            name='series_num',
            field=models.CharField(max_length=100, null=True, verbose_name='Серия и номер паспорта'),
        ),
        migrations.AddField(
            model_name='lk',
            name='when_issued',
            field=models.DateField(null=True, verbose_name='Дата выдачи'),
        ),
        migrations.AddField(
            model_name='lk',
            name='who_issued',
            field=models.CharField(max_length=500, null=True, verbose_name='Кем выдан'),
        ),
    ]