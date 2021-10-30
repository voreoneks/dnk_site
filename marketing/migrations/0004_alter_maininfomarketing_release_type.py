# Generated by Django 3.2.5 on 2021-10-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20211024_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfomarketing',
            name='release_type',
            field=models.CharField(choices=[('CLIP', 'Видеоклип'), ('SINGLE', 'Сингл'), ('MAXI_SINGLE', 'Максисингл'), ('ALBUM', 'Альбом / ЕР')], max_length=20, verbose_name='Тип релиза'),
        ),
    ]