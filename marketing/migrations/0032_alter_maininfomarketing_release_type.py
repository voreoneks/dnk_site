# Generated by Django 3.2.5 on 2021-11-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0031_alter_maininfomarketing_release_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininfomarketing',
            name='release_type',
            field=models.CharField(choices=[('SINGLE', 'Сингл'), ('MAXI_SINGLE', 'Максисингл'), ('CLIP', 'Видеоклип'), ('ALBUM', 'Альбом / ЕР')], default='SINGLE', max_length=20, verbose_name='Тип релиза'),
        ),
    ]
