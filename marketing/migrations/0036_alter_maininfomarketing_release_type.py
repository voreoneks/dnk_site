# Generated by Django 3.2.5 on 2021-11-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0035_auto_20211109_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfomarketing',
            name='release_type',
            field=models.CharField(choices=[('MAXI_SINGLE', 'Максисингл'), ('ALBUM', 'Альбом / ЕР'), ('CLIP', 'Видеоклип'), ('SINGLE', 'Сингл')], default='SINGLE', max_length=20, verbose_name='Тип релиза'),
        ),
    ]
