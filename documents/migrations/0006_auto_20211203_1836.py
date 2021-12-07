# Generated by Django 3.2.5 on 2021-12-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_alter_maininfodocs_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiodocs',
            name='album_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название релиза'),
        ),
        migrations.AlterField(
            model_name='maininfodocs',
            name='release_type',
            field=models.CharField(choices=[('SINGLE', 'Сингл'), ('CLIP', 'Видеоклип'), ('ALBUM', 'Альбом / ЕР')], default='SINGLE', max_length=15, null=True, verbose_name='Тип релиза'),
        ),
    ]